#!/bin/bash

# Define variables
FRAMER_SITE_URL="https://your-framer-site-url.com"
DOWNLOAD_DIR="framer-site"

# Remove old files
rm -rf $DOWNLOAD_DIR

# Download Framer site
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent $FRAMER_SITE_URL -P $DOWNLOAD_DIR

# Move into the directory
cd $DOWNLOAD_DIR

# Push to GitHub
git add .
git commit -m "Auto-update from Framer"
git push origin main#!/bin/bash

# Define variables
FRAMER_SITE_URL="https://astra-ipsum.framer.website"
DOWNLOAD_DIR="framer-site"

# Remove old files
rm -rf $DOWNLOAD_DIR

# Download Framer site
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent $FRAMER_SITE_URL -P $DOWNLOAD_DIR

# Move into the directory
cd $DOWNLOAD_DIR

# Push to GitHub
git add .
git commit -m "Auto-update from Framer"
git push origin main

