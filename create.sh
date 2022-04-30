#!/bin/bash

if [ ! -d ~/tmp/files ]; then
  mkdir -p ~/tmp/files
fi

cd ~/tmp/files
rm -Rf ~/tmp/files/*
mkdir sub1 sub2
COUNTER=1

for x in txt photoslibrary jpg jpeg JPG png key jpg jpeg jpe jif jfif jfi png gif webp tiff tif psd raw arw cr2 nrw k25 bmp dib heif heic ind indd indt jp2 j2k jpf jpx jpm mj2 svg svgz ai eps; do
    touch $COUNTER.$x sub1/sub1-$COUNTER.$x sub2/sub2-$COUNTER.$x
    ((COUNTER=COUNTER+1))
done

