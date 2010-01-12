rm -rf output
./create-icon-theme.sh moblin
cd output/moblin
autoreconf -if && ./configure && make distcheck || exit 1
mv *tar.gz ../..
cd -
