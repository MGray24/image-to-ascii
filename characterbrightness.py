from PIL import Image, ImageFont, ImageDraw
import sys
from main import get_region_brightness, crop

ASCII_CHARACTERS = "B%8&WM#*oahkbdwmZO0LCJUYXzcvunxrt1?-+~<>!I:."
FONT_PATH = "FiraCode-Regular.ttf"
FONT_SIZE = 26


def main():
    if len(sys.argv) < 2:
        raise IndexError(
            "Missing input image, usage should look like "
            "`python characterbrightness.py input.png`"
        )

    font = ImageFont.truetype(FONT_PATH, size=FONT_SIZE)

    with Image.open(sys.argv[1]) as image:
        width = 10 * font.getlength("B")
        image = crop(image, width, 400)
        draw_character(image, font)


def draw_character(image, font):
    draw = ImageDraw.Draw(image)

    char_width = int(font.getlength("B"))
    ascent, _ = font.getmetrics()
    char_height = ascent

    # Draw characters onto the image
    index = 0
    for y in range(0, image.height, char_height):
        for x in range(0, image.width, char_width):
            char = ASCII_CHARACTERS[index % len(ASCII_CHARACTERS)]
            draw.text((x, y), char, font=font, fill=(255, 255, 255))
            index += 1

    # Measure brightness and print dictionary entries
    pixels = image.load()
    index = 0

    print("{")
    for j in range(image.height // char_height):
        for i in range(image.width // char_width):
            if index >= len(ASCII_CHARACTERS):
                break

            brightness = get_region_brightness(
                pixels, i*char_width, j*char_height, char_width, char_height
            )

            print(f"'{ASCII_CHARACTERS[index]}':{brightness},")
            index += 1

    print("}")
    image.show()


if __name__ == "__main__":
    main()