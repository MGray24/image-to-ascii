from PIL import Image, ImageFont, ImageDraw
import sys

CHARACTER_W_TO_H_RATIO = 1/2

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

def find_new_height(height, new_width, ascii_columns):
    "Find the new height the image should be based on its new width, and how many columns we want"
    character_width = new_width//ascii_columns
    character_height = character_width*(1/CHARACTER_W_TO_H_RATIO)
    return (height//character_height)*character_height

if __name__ == "__main__":
    main()

