from PIL import Image, ImageDraw
import json

with open("../data/hearthstone_clean_cards_data.json", "r") as f:
    cards = json.load(f)

for card in cards:
    og = Image.open('../images/raw/512x/{}.png'.format(card["id"]))
    bigsize = (og.size[0] * 3, og.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    shape = (347, 210, 1173, 1323)
    draw.ellipse(shape, fill=255)
    mask = mask.resize(og.size, Image.ANTIALIAS)
    og.putalpha(mask)
    new = og.crop([i/3 for i in shape])
    new.save("../images/raw/crops/{}.png".format(card["id"]))
