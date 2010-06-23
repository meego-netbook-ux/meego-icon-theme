rm -rf output
./create-icon-theme.sh netbook
cd output/netbook
autoreconf -if && ./configure && make distcheck || exit 1
mv *tar.gz ../..
cd -
