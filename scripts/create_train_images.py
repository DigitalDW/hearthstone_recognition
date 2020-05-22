from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter
import json
import os

DIRECTORY = "../images/raw/crops/"
FILES = os.listdir(DIRECTORY)

OUTPUT_DIRECTORY = "../images/train/"


def main():
    img_n = range(10)
    images = [None for _ in img_n]
    for e in range(5):
        filename = FILES[e]

        og = Image.open(DIRECTORY + filename)
        width, height = og.size

        resized = og.resize((int(width/3.2), int(height/3.2)), Image.ANTIALIAS)

        frozen_filter = freeze(width, height)
        resized_f = freeze_card(og, frozen_filter)

        for i in img_n:
            bg = Image.open("../images/raw/bg/bg.png")
            r180 = resized.rotate(180, expand=True)
            f180 = resized_f.rotate(180, expand=True)
            if i == 0:
                bg.paste(resized, (379, 195), resized)
            elif i == 1:
                bg.paste(resized, (600, 50), resized)
            elif i == 2:
                bg.paste(r180, (575, 238), r180)
            elif i == 3:
                bg.paste(resized, (130, 60), resized)
            elif i == 4:
                bg.paste(resized_f, (420, 50), resized_f)
            elif i == 5:
                bg.paste(resized, (300, 60), resized)
            elif i == 6:
                bg.paste(resized, (600, 240), resized)
            elif i == 7:
                bg.paste(r180, (300, 240), r180)
            elif i == 8:
                bg.paste(resized_f, (200, 220), resized_f)
            else:
                bg.paste(f180, (470, 238), f180)
            images[i] = bg

        output = filename.split(".")
        for i in img_n:
            images[i].save(OUTPUT_DIRECTORY + output[0] +
                           "_" + str(i) + "." + output[1])


def freeze(width, height):
    width = width + 60
    height = height + 60
    # Filtre pour les cartes gelées
    outside_circle = Image.new("RGBA", (width, height))
    image_to_composite = Image.new("RGBA", (width, height))
    mask = Image.new("L", (width, height), 0)
    circle = ImageDraw.Draw(outside_circle, "RGBA")
    circle.ellipse(
        [(30, 30), (width-30, height-30)], "#b0fcff", None)
    inside_circle = ImageDraw.Draw(mask, "L")
    inside_circle.ellipse(
        [(45, 45), (width-45, height-60)], 255, None)
    frozen_circle = Image.composite(image_to_composite, outside_circle, mask)

    # Quelques formes pour imiter la glace
    ice = Image.new("RGBA", (width, height))
    draw_ice = ImageDraw.Draw(ice, "RGBA")
    draw_ice.polygon((
        (170, 380),
        (150, 360),
        (105, 370),
        (100, 430)), fill="#b0fcff")
    draw_ice.polygon((
        (90, 360),
        (130, 370),
        (85, 400)), fill="#b0fcff")
    draw_ice.polygon((
        (140, 380),
        (180, 380),
        (160, 420)), fill="#b0fcff")
    draw_ice.polygon((
        (2, 220),
        (40, 200),
        (60, 220),
        (40, 240)), fill="#b0fcff")
    draw_ice.polygon((
        (30, 100),
        (60, 115),
        (50, 125)), fill="#b0fcff")
    draw_ice.polygon((
        (45, 65),
        (80, 80),
        (90, 100),
        (60, 110)), fill="#b0fcff")
    draw_ice.polygon((
        (230, 50),
        (260, 28),
        (250, 75)), fill="#b0fcff")
    draw_ice.polygon((
        (290, 150),
        (310, 155),
        (300, 170)), fill="#b0fcff")
    draw_ice.polygon((
        (280, 175),
        (315, 175),
        (335, 200),
        (300, 205)), fill="#b0fcff")
    draw_ice.polygon((
        (295, 275),
        (315, 300),
        (280, 305)), fill="#b0fcff")
    frozen_circle.paste(ice, (0, 0), ice)
    return frozen_circle


def freeze_card(og, frozen):
    width, height = og.size
    width_f, height_f = frozen.size
    frozen_card = Image.new("RGBA", (width_f, height_f))
    frozen_card.paste(og, (int((width_f - width)/2),
                           int((height_f - height)/2)), og)

    # Augmenter la luminosité et le contraste
    brightness = ImageEnhance.Brightness(frozen_card)
    frozen_card = brightness.enhance(1.33)
    contrast = ImageEnhance.Contrast(frozen_card)
    frozen_card = contrast.enhance(1.33)

    """
    # Add light blue filter
    image_to_composite = Image.new("RGBA", (width_f, height_f))
    hue = Image.new("RGBA", (width_f, height_f))
    mask = Image.new("L", (width_f, height_f), 0)

    hue_circle = ImageDraw.Draw(hue, "RGBA")
    hue_circle.ellipse(
        [(30, 30), (width+30, height_f-30)], "#14b6e3", None)

    hue_mask_circle = ImageDraw.Draw(mask, "L")
    hue_mask_circle.ellipse(
        [(30, 30), (width+30, height_f-30)], 255, None)

    hue.putalpha(128)

    hue = Image.composite(hue, image_to_composite, mask)

    frozen_card.paste(hue, (0, 0), hue)"""
    frozen_card.paste(frozen, (0, 0), frozen)
    return frozen_card.resize(
        (int(width/2.6), int(height/2.6)),
        Image.ANTIALIAS
    )


if __name__ == "__main__":
    main()
