#!/usr/bin/env bash
cd model

echo "Downloading Pix2Pix Trained Model:"
fileid="1da0Ral-neSgAnEOr0Ck0WCuB0hR6T2z5"
filename="gen.pth.tar"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}

cd ../../

pwd
ls
echo "Pix2Pix : Models downloaded"
echo "Start server or Run Docker Image"
