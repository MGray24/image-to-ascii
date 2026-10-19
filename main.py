from argparse import ArgumentError

from PIL import Image
import sys

def main():
    '''
    When the user calls the program like python main.py file.png,
    sys.argv[0] will be the name of the script, so main.py
    sys.argv[1] will be the name of the file, in this case file.png
    '''
    if len(sys.argv) < 2:
        raise IndexError("Missing input image, usage should look like `python main.py input.png`")
    filename = sys.argv[1]
    #open image file
    with Image.open(filename) as img:
        #get pixel access, this returns a PixelAccess object
        pixels = img.load()

        width, height = img.size

        #example of how to access top left pixel
        top_left_pixel = pixels[0, 0]
        r, g, b = top_left_pixel[0], top_left_pixel[1], top_left_pixel[2]
        print(r, g, b)
        # for test image if > 400 should raise error
        crop(img,400, 400)

def crop(image, x, y):

    width, height = image.size

    if x > width or y > height:
        raise IndexError("x or y value too big")
    # set the crop size (left,top,right,bottom)
    else:
        box = (0,0,x,y)
        cropped_img = image.crop(box)

        cropped_img.show()

if __name__ == "__main__":
    main()
