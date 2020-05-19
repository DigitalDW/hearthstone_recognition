import requests
import shutil
import json

with open("../data/hearthstone_clean_cards_data.json", "r") as f:
    cards = json.load(f)

t = len(cards)
for card in cards:
    t -= 1
    _id = card["id"]
    url256 = "https://art.hearthstonejson.com/v1/render/latest/enUS/256x/{}.png".format(
        _id)
    url512 = "https://art.hearthstonejson.com/v1/render/latest/enUS/256x/{}.png".format(
        _id)

    try:
        r256 = requests.get(url256, stream=True)
        r256.raw.decode_content = True
        with open("../images/raw/256x/{}.png".format(_id), 'wb') as f:
            shutil.copyfileobj(r256.raw, f)

        r512 = requests.get(url256, stream=True)
        r512.raw.decode_content = True
        with open("../images/raw/512x/{}.png".format(_id), 'wb') as f:
            shutil.copyfileobj(r512.raw, f)

        print("success! {}.png saved! {} to go".format(_id, t))
    except:
        print("failed")
        break
