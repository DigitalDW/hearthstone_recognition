from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter
import json
import os
from create_train_images import freeze, freeze_card

DIRECTORY = "../../images/raw/crops/"
FILES = os.listdir(DIRECTORY)

OUTPUT_DIRECTORY = "../../images/test/"


def main():
    img_n = range(3)
    images = [None for _ in img_n]
    for e in range(5):
        filename = FILES[e]

        og = Image.open(DIRECTORY + filename)
        width, height = og.size

        resized1 = og.resize(
            (int(width/3.2), int(height/3.2)), Image.ANTIALIAS)
        resized2 = og.resize(
            (int(width/3.5), int(height/3.5)), Image.ANTIALIAS)

        frozen_filter = freeze(width, height)
        resized_f = freeze_card(og, frozen_filter)

        for i in img_n:
            bg = Image.open("../../images/raw/bg/bg.png")
            if i == 0:
                bg.paste(resized1, (679, 195), resized1)
            elif i == 1:
                bg.paste(resized_f, (164, 180), resized_f)
            else:
                bg.paste(resized2, (679, 195), resized2)
            images[i] = bg

        output = filename.split(".")
        for i in img_n:
            images[i].save(OUTPUT_DIRECTORY + output[0] +
                           "_" + str(i) + "." + output[1])


if __name__ == "__main__":
    main()
