from PIL import Image


image = Image.open("./kedi.jpg");

image.show()

for i in range(0, image.size[0] - 1):

    for j in range(0, image.size[1] - 1):
        pixelColorVals = image.getpixel((i, j));

        redPixel = 255 - pixelColorVals[0];

        greenPixel = 255 - pixelColorVals[1];

        bluePixel = 255 - pixelColorVals[2];

        image.putpixel((i, j), (redPixel, greenPixel, bluePixel));

image.show();