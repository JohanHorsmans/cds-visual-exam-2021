#! /bin/sh

# This script will download: Map of Denmark (region based), nitrate layer (points), farm areas (polygons), organic farms (polygons)

# Install gdown for download from drive folder
pip install gdown

###### ASSIGNMENT 5 DATA ######

# Go to new data folder
cd assignment_5

mkdir './data'

# For each link in list of links, download to current folder
for f in https://drive.google.com/uc?id=1eg-rR8PgOxRjEDgUG82p1ZPQbd5bkJqX; do gdown $f; done

unzip impressionist_painters.zip

###### SELF ASSIGNED DATA ######

# Go back to parent directory
cd ../self_assigned/raw_data

cp -a monet/. ../mangled_data/monet/

cd content_images

for f in https://drive.google.com/uc?id=1jS9zVVKdPuM3MFs3yQqyIV_kD1-JnoIS; do gdown $f; done

unzip landscape_images.zip

# Give information on the success of the script in the terminal
echo "The required data has been downloaded successfully"
