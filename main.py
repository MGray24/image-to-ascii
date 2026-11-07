from PIL import Image, ImageFont, ImageDraw
from brightness_map import char_to_brightness
import sys
import numpy as np

def main():
    if len(sys.argv) < 2:
        raise ValueError("Usage: python main.py input.png [font_size]")

    filename = sys.argv[1]
    font_size = int(sys.argv[2]) if len(sys.argv) > 2 else 26

    if font_size <= 0:
        raise ValueError("Font size must be positive")

    font = ImageFont.truetype("FiraCode-Regular.ttf", size=font_size)

    with Image.open(filename) as image:
        image, columns, rows, char_width, char_height = prepare_image(
            image, font
        )

        #this is the black image we will draw on, this is not the input image
        #it will be the same width and height as the image passed in after cropping
        output_image = Image.new("RGB", (image.width, image.height), "black")
        draw = ImageDraw.Draw(output_image)

        pixels = image.load()

        for row in range(rows):
            for col in range(columns):
                brightness = get_region_brightness(
                    pixels,
                    col * char_width,
                    row * char_height,
                    char_width,
                    char_height
                )
                #print(f"{row=} {col=} {brightness=}")
                # Select ASCII character based on brightness
                best_character = matching_brightness(brightness)
                draw.text((col*char_width,row*char_height), best_character, font=font, fill=(255, 255, 255))
        output_image.show()
def crop(image, x, y):
    width, height = image.size

    if x > width or y > height:
        raise IndexError("x or y value too big")
    else:
        box = (0, 0, x, y)
        cropped_img = image.crop(box)
        return cropped_img


def calculate_grid(image, font):
    char_width = round(font.getlength("B"))
    ascent, descent = font.getmetrics()
    char_height = ascent

    columns = image.width // char_width
    rows = image.height // char_height

    return columns, rows, char_width, char_height


def prepare_image(image, font):
    columns, rows, char_width, char_height = calculate_grid(image, font)

    if columns == 0 or rows == 0:
        raise ValueError("Font is too large for the image")

    new_width = columns * char_width
    new_height = rows * char_height

    cropped_image = crop(image, new_width, new_height)

    return cropped_image, columns, rows, char_width, char_height

def get_brightness(pixels,x,y):
    pixel = pixels[x,y]
    r, g, b, a = pixel[0], pixel[1], pixel[2], pixel[3]
    if a == 0:
        return 0
    return (0.2126 * r) + (0.7152 * g) + (0.0722 * b)

def get_region_brightness(pixels,x,y,width,height):
    " Assuming that the width and height are measured in pixels"
    avr_brightness = 0
    for j in range(height):
        for i in range(width):
            avr_brightness += get_brightness(pixels, x+i, y+j)

    return avr_brightness/(width*height)

def matching_brightness(brightness):
    char = None
    pair_list = list(char_to_brightness.items())
    diff_to_beat = abs((brightness- list(char_to_brightness.values())[0]))
    for key, val in pair_list:
        diff = abs(brightness - val)
        if diff <= diff_to_beat:
            char = key
            diff_to_beat=diff
    return char


if __name__ == "__main__":
    main()

