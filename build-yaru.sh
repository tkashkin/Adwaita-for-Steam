#! /bin/bash

info() {
  echo [+] $@
}

fatal() {
  echo [!] $@
  exit 1
}

###################################################
# CHECKS
###################################################

# current workding directory expected to be Yaru-For-Steam/Yaru
if [[ ! -d "Yaru" ]]; then
  fatal "Yaru folder isn't exist. Please create Yaru folder."
fi
info "working directory OK."

command -v cairosvg 1>&2>/dev/null
if [[ $? == 1 ]]; then
  fatal "missing dependency: cairosvg"
fi
info "dependencies OK."

###################################################
# MAIN
###################################################

cp -rf Yaru/* Adwaita/

for f in $(find Adwaita -type f -name '*.svg')
do
  info "Processing $f file..."

  cairosvg -o "${f%.*}.png" $f
  convert "${f%.*}.png" -flip "${f%.*}.tga"
  if [[ -f "${f%.*}_backdrop.tga" ]]; then
    convert "${f%.*}.png" -flip -matte -channel A +level 0,50% +channel "${f%.*}_backdrop.tga"
  fi
  if [[ -f "${f%.*}_disabled.tga" ]]; then
    convert "${f%.*}.png" -flip -matte -channel A +level 0,30% +channel "${f%.*}_disabled.tga"
  fi
  rm "${f%.*}.png"

  cairosvg -s 2 -o "${f%.*}@2x.png" $f
  convert "${f%.*}@2x.png" -flip "${f%.*}@2x.tga"
  if [[ -f "${f%.*}_backdrop@2x.tga" ]]; then
    convert "${f%.*}@2x.png" -flip -matte -channel A +level 0,50% +channel "${f%.*}_backdrop@2x.tga"
  fi
  if [[ -f "${f%.*}_disabled@2x.tga" ]]; then
    convert "${f%.*}@2x.png" -flip -matte -channel A +level 0,30% +channel "${f%.*}_disabled@2x.tga"
  fi
  rm "${f%.*}@2x.png"

  rm $f
done
