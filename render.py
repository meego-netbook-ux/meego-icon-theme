#!/usr/bin/python
# coding=utf-8
"""render-application-icons

A small script to generate Moblin icons for applications.

Usage: render-applications-icons [options] filename

Options:
    -o, --output    directory        where to put the generated files
    -h, --help                       print this help
    -v, --verbose                    verbose output"""

import getopt
import libxml2
import os
import re
import string
import shutil
import sys
import tempfile

__author__    = 'Damien Lespiau <damien.lespiau@intel.com'
__version__   = '0.1'
__date__      = '20091209'
__copyright__ = 'Copyright (©) 2009 Intel Corporation'
__license__   = 'GPL v2'

verbose = 0

class RendererException(Exception):
    pass

class FatalError(RendererException):
    '''An error not related to the user input'''

class ParseError(RendererException):
    '''Could not parse the icon theme SVG file'''

def note(message):
    if verbose:
        print message

def debug(message):
    if verbose > 1:
        print message

class ImageMagick:
    def __init___(self):
        pass

    def composite(self, file1, fil2, output):
        cmd = "composite -gravity center %s %s %s" % (file1, fil2, output)
        os.system(cmd)

class Inkscape:
    def __init__(self, filename):
        self.binary = 'inkscape'
        self.svg = filename

    def export(self, id, output, witdh, height):
        global verbose

        redirect = ""
        if verbose < 2:
            redirect = "1> /dev/null 2> /dev/null"

        cmd = "%s -i %s -e %s -w %d -h %d %s %s" % (self.binary,
                                                    id,
                                                    output,
                                                    witdh,
                                                    height,
                                                    self.svg, redirect)
        os.system(cmd)

class SVGFile:
    def __init__(self, filename):
        self.filename = filename
        self.doc = libxml2.parseFile(filename)
        if self.doc.name != filename:
            raise ParseError("Error parsing %s" % filename)
        self.ctx = self.doc.xpathNewContext()

        self.ctx.xpathRegisterNs('svg', 'http://www.w3.org/2000/svg')
        self.ctx.xpathRegisterNs('sodipodi',
                                 'http://sodipodi.sourceforge.net/DTD/'
                                 'sodipodi-0.dtd')
        self.ctx.xpathRegisterNs('inkscape',
                                 'http://www.inkscape.org/namespaces/inkscape')

    def xpath_eval(self, xpath):
        return self.ctx.xpathEval(xpath)

    def change_stroke(self, color):
        res = self.xpath_eval("/svg:svg"
                              "/svg:g[@inkscape:groupmode='layer' and "
                              "       @inkscape:label='Artwork']"
                              "/svg:g[@inkscape:groupmode='layer' and "
                              "       @inkscape:label='Applications']"
                              "/descendant::*")

        for node in res:
            style = node.prop('style')
            if not style:
                continue
            style = re.sub(r'stroke:.*?;', 'stroke:%s;' % color, style)
            node.setProp('style', style)

    def change_stroke_width(self, width):
        res = self.xpath_eval("/svg:svg"
                              "/svg:g[@inkscape:groupmode='layer' and "
                              "       @inkscape:label='Artwork']"
                              "/svg:g[@inkscape:groupmode='layer' and "
                              "       @inkscape:label='Applications']"
                              "/descendant::*")
        re_stroke_width = re.compile(r'stroke-width:(.*?);')

        for node in res:
            style = node.prop('style')
            if not style:
                continue
            found_stroke_width = re_stroke_width.search(style)
            if not found_stroke_width:
                continue
            old_width = float(found_stroke_width.group(1))
            # we assume that the original number represents 2px (whatever the
            # transform matrix used. If that assumption changes, this code has
            # to change to take the transform matrix into account
            new_width = width * old_width / 2
            style = re.sub('stroke-width:.*?;',
                           "stroke-width:%0.8f;" % new_width,
                           style)
            node.setProp('style', style)

    def write(self):
        self.doc.saveFile(self.filename)

class IconTheme:
    def __init__(self, filename, output_dir='.'):
        self.file = SVGFile(filename)
        self.set_output_directory(output_dir)

    def set_output_directory(self, directory):
        self.output_dir = directory
        if not os.path.exists(directory):
            os.makedirs(directory)



    def generate_app_svg(self, filename):
        doc = libxml2.newDoc("1.0")

        # add the root element
        res = self.file.xpath_eval("/svg:svg")
        svg = res[0].copyNode(2)
        doc.setRootElement(svg)

        # rectangle layer
        res = self.file.xpath_eval("/svg:svg"
                                   "/svg:g[@inkscape:groupmode='layer' and "
                                   "       @id='Rectangles']")
        rectangles_layer = res[0].copyNode(2)
        svg.addChild(rectangles_layer)

        # rectangles
        res = self.file.xpath_eval("/svg:svg"
                                   "/svg:g[@inkscape:groupmode='layer' and "
                                   "       @id='Rectangles']"
                                   "/svg:rect[starts-with(@id,'moblin-')]")
        for rect in res:
            rectangle = rect.copyNode(2)
            rectangles_layer.addChild(rectangle)

        # Artwork layer
        res = self.file.xpath_eval("/svg:svg"
                                   "/svg:g[@inkscape:groupmode='layer' and "
                                   "       @inkscape:label='Artwork']")
        artwork_layer = res[0].copyNode(2)
        svg.addChild(artwork_layer)

        # Applications layer (and its whole subtree)
        res = self.file.xpath_eval("/svg:svg"
                                   "/svg:g[@inkscape:groupmode='layer' and "
                                   "       @inkscape:label='Artwork']"
                                   "/svg:g[@inkscape:groupmode='layer' and "
                                   "       @inkscape:label='Applications']")
        applications_layer = res[0].copyNode(1)
        artwork_layer.addChild(applications_layer)

        doc.saveFile(filename)
        return SVGFile (filename)

    def create_output_dir(self, size, name):
        output_dir = os.path.join(self.output_dir,
                                  "%dx%d" % (size, size),
                                  name)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        return output_dir

    def generate_icons(self):
        res = self.file.xpath_eval("/svg:svg"
                                   "/svg:g[@inkscape:groupmode='layer' and "
                                   "       @id='Rectangles']"
                                   "/svg:rect")
        re_default_rect_id = re.compile(r'rect[0-9]+')
        inkscape = Inkscape(self.file.filename)

        output_dir_16 = self.create_output_dir(16, 'icons')
        output_dir_24 = self.create_output_dir(24, 'icons')
        output_dir_48 = self.create_output_dir(48, 'icons')
        dirs = { '16': output_dir_16, '24': output_dir_24 }

        for rect in res:
            id = rect.prop('id')
            width = rect.prop('width')
            height = rect.prop('height')

            if re_default_rect_id.match(id):
                debug("Dropping " + id)
                continue

            if not((width == '16' and height == '16') or
                   (width == '24' and height == '24')):
                debug("Dropping " + id)
                continue

            file = os.path.join(dirs[width], id + '.png')
            print('Generating ' + file)
            inkscape.export(id, file, int(width), int(height))

            # generate 48x48 icons with the 24x24 rects
            if width == '24':
                file_48 = os.path.join (output_dir_48, id + '.png')
                print('Generating ' + file_48)
                inkscape.export(id, file_48, 48, 48)

    def generate_app_icons(self, tile_size, fg_size):
        # that a way to say: "Don't try with any other size"
        if tile_size != 32 and tile_size != 48:
            return

        # create the output directory if necessary
        output_dir = os.path.join(self.output_dir,
                                  "%dx%d" % (tile_size, tile_size),
                                  'apps')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # temporary directory to store the foreground of the icons
        tmp_dir = tempfile.mkdtemp(dir='.')
        # let's invoke the power of image magick
        magick = ImageMagick()

        # generate a svg with the app icons to manipulate the xml
        app_svg_filename = os.path.join(tmp_dir, "apps-%d.svg" % tile_size)
        app_svg = self.generate_app_svg(app_svg_filename)
        app_svg.change_stroke('white')
        if tile_size == 48:
            app_svg.change_stroke_width(1.7)
        app_svg.write()

        inkscape = Inkscape(app_svg_filename)

        # look for the applications' rectangles
        res = app_svg.xpath_eval("/svg:svg"
                                 "/svg:g[@inkscape:groupmode='layer' and "
                                 "       @id='Rectangles']"
                                 "/svg:rect")

        for node in res:
            fg_name = node.prop('id')
            fg_file = os.path.join(tmp_dir, fg_name + '.png')

            tile_name = node.prop('label')
            tile_file = os.path.join('tiles',
                                     "%dx%d" % (tile_size, tile_size),
                                     tile_name + '.png')

            icon_file = os.path.join (output_dir, fg_name + '.png')

            print('Generating ' + icon_file)

            inkscape.export(fg_name, fg_file, fg_size, fg_size)
            magick.composite(fg_file, tile_file, icon_file)

        # remove the temporary directory
        shutil.rmtree(tmp_dir)

def usage():
    print(__doc__)
    sys.exit(1)

def main(argv):
    opt_output = "."

    try:
        opts, args = getopt.getopt(argv, 'hvo:', ('help',
                                                  'verbose',
                                                  'output=',
                                                  'extra-verbose'))
    except getopt.GetoptError:
        usage()
    for opt, arg, in opts:
        global verbose
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--verbose'):
            verbose = 1
        elif opt in ('--extra-verbose'):
            verbose = 2
        elif opt in ('-o', '--output'):
            opt_output = arg
        else:
            assert False, "Unhandled option"

    if len(args) != 1:
        usage()

    xml_file = args[0]
    note("Using %s" % xml_file)
    icon_theme = IconTheme(xml_file)
    icon_theme.set_output_directory(opt_output)
    icon_theme.generate_icons()
    icon_theme.generate_app_icons(32, 24)
    icon_theme.generate_app_icons(48, 36)

if __name__ == '__main__':
    main(sys.argv[1:])
