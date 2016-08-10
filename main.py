__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'

"""
Image Metadata Viewer

GitHub Repo <https://github.com/Shokr/Image-Metadata-Viewer>
"""

from PIL import Image
from PIL.ExifTags import TAGS

import exifread

def main():
    print("## Image Info ##")

    # write full image name
    photo=input("Photo Name : ")

    # open image
    img =Image.open(photo)

    # get all info
    exif = img._getexif()

    # loop to view info
    for tag in exif:
        tagname= TAGS.get(tag,tag)
        value=exif[tag]
        print (str(tagname) +" : "+str(value))

    print("################################## More ########################################################")

    # open image file as binary
    f = open(photo, 'rb')

    # get info by exifread
    tags = exifread.process_file(f)

    ## loop to view info
    for tag in tags:
        value=tags[tag]
        if tag not in ['JPEGThumbnail']:
            print (str(tag) +" : "+str(value))

if __name__ == "__main__":
  #Run as main program
  main()