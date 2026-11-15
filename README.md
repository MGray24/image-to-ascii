# Project Title

A program that converts images to ascii art.

## Description

What this essentially does is take in any image and by looking at the brightness of each pixel determines the most suitable ascii character to take its place .

## Getting Started

### Dependencies

To get all required libraries run
```commandline
pip install -r requirements.txt
```

### Installing

## Executing program

To run the program follow the following steps.
* Go to your terminal and run
```
python main.py (image you want to convert) (optional font size)
```
* example for an already existing image.
```
python main.py test-images/sphere.png 12
```
In the above example
* 12 is the optional font size without it the code still runs and uses the base font size.
* "test-images/sphere.png" is my image located inside the "test-images" folder.
* If your image is in the same folder as "main" just call the image directly.Example.
```
python main.py sphere.png 12
```
* Finally, when you run the code you will be asked whether you would like a colored image. Simply write "no" for a black and white image and leave blank or write anything else for a colored one.

## Authors

Mason Gray

Chris Adera
