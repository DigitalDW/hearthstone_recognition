from PIL import Image, ImageChops, ImageDraw, ImageColor, ImageFilter
import json
import os

DIRECTORY = "../images/raw/crops/"
FILES = os.listdir(DIRECTORY)

OUTPUT_DIRECTORY = "../images/train/"


def main():
    img_n = range(10)
    images = [None for _ in img_n]
    filename = FILES[4]

    og = Image.open(DIRECTORY + filename)
    width, height = og.size

    resized = og.resize((int(width/3.2), int(height/3.2)), Image.ANTIALIAS)

    frozen_filter = freeze(width, height)
    resized_f = freeze_card(og, frozen_filter)

    for i in img_n:
        bg = Image.open("../images/raw/bg/bg.png")
        r45 = resized.rotate(45, expand=True)
        r180 = resized.rotate(180, expand=True)
        r90 = resized.rotate(90, expand=True)
        rm90 = resized.rotate(-90, expand=True)
        r270 = resized.rotate(270, expand=True)
        fm45 = resized_f.rotate(-45, expand=True)
        f90 = resized_f.rotate(90, expand=True)
        bg.paste(resized, (379, 195), resized) if i == 0 else (
            bg.paste(r45, (600, 50), r45) if i == 1 else (
                bg.paste(r180, (575, 238), r180) if i == 2 else (
                    bg.paste(r270, (130, 60), r270) if i == 3 else (
                        bg.paste(resized_f, (420, 50), resized_f) if i == 4 else (
                            bg.paste(r45, (300, 60), r45) if i == 5 else (
                                bg.paste(r90, (600, 240), r90) if i == 6 else (
                                    bg.paste(rm90, (300, 240), rm90) if i == 7 else (
                                        bg.paste(fm45, (200, 220), fm45) if i == 8 else (
                                            bg.paste(f90, (470, 238), f90)
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
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
    frozen_card.paste(frozen, (0, 0), frozen)
    return frozen_card.resize(
        (int(width/2.6), int(height/2.6)),
        Image.ANTIALIAS
    )


if __name__ == "__main__":
    main()
