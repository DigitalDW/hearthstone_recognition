import requests
import shutil
import json

with open("../data/hearthstone_clean_cards_data.json", "r") as f:
    cards = json.load(f)

t = len(cards)
for card in cards:
    t -= 1
    _id = card["id"]
    url = "https://art.hearthstonejson.com/v1/render/latest/enUS/256x/{}.png".format(
        _id)
    try:
        r = requests.get(url, stream=True)
        r.raw.decode_content = True
        with open("../images/raw/256x/{}.png".format(_id), 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print("success! {}.png saved! {} to go".format(_id, t))
    except:
        print("failed")
        break
