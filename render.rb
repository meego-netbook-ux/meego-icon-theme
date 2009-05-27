#!/usr/bin/env ruby

require "rexml/document"
require "ftools"
include REXML
INKSCAPE = '/usr/bin/inkscape'
SRC = "."

def renderit(file)

	# Open SVG file.
	svg = Document.new(File.new("#{SRC}/#{file}", 'r'))

	# Go through every layer.
	svg.root.each_element("/svg/g[@inkscape:groupmode='layer']") do |type| 

		type_name = type.attributes.get_attribute("inkscape:label").value  

		puts type_name

		svg.root.each_element("/svg/g[@inkscape:label='#{type_name}']/g") do |icon|

			icon_node = icon.attributes.get_attribute("inkscape:label")

			if (icon_node) 
				icon_name = icon_node.value
				puts "    " + icon_name
				svg.root.each_element("/svg/g[@inkscape:label='#{type_name}']/g[@inkscape:label='#{icon_name}']/rect']") do |rect|
					rect_node = rect.attributes.get_attribute("id")

					if (rect_node) 
						rect_name = rect_node.value
						rect_width = rect.attributes.get_attribute("width").value
						rect_height = rect.attributes.get_attribute("height").value

						if (rect_width == '48' and rect_height == '48')
							puts "        " + rect_name + "(" + rect_width + ", " + rect_height + ")"
                            dir = "48x48/#{type_name}/"
                            File.makedirs(dir) unless File.exists?(dir)
                            cmd = "#{INKSCAPE} -i #{rect_name} -e #{dir}/#{icon_name}.png #{SRC}/#{file} > /dev/null 2>&1"
                            system(cmd)
						end
						
						if (rect_width == '24' and rect_height == '24')
							puts "        " + rect_name + "(" + rect_width + ", " + rect_height + ")"
                            dir = "24x24/#{type_name}/"
                            File.makedirs(dir) unless File.exists?(dir)
                            cmd = "#{INKSCAPE} -i #{rect_name} -e #{dir}/#{icon_name}.png #{SRC}/#{file} > /dev/null 2>&1"
                            system(cmd)
						end
						
						if (rect_width == '16' and rect_height == '16')
							puts "        " + rect_name + "(" + rect_width + ", " + rect_height + ")"
                            dir = "16x16/#{type_name}/"
                            File.makedirs(dir) unless File.exists?(dir)
                            cmd = "#{INKSCAPE} -i #{rect_name} -e #{dir}/#{icon_name}.png #{SRC}/#{file} > /dev/null 2>&1"
                            system(cmd)
						end
						
					end

				end


			end

		end # End of layer loop.    


	end # End of layer loop.  
    

end # End of function.


if (ARGV[0].nil?) #render all SVGs
  puts "Rendering from SVGs in #{SRC}"
  Dir.foreach(SRC) do |file|
    renderit(file) if file.match(/svg$/)
  end
  puts "\nrendered all SVGs"
else #only render the SVG passed
  file = "#{ARGV[0]}.svg"
  if (File.exists?("#{SRC}/#{file}"))
    renderit(file)
    puts "\nrendered #{file}"
  else
    puts "[E] No such file (#{file})"
  end
end
