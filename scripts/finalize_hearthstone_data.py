import json


def clean_data(cards_data):
    new_cards_data = list()
    for card in cards_data:
        if "collectible" in card.keys():
            if card.get('type') == "MINION":
                new_cards_data.append({
                    "id": card["id"],
                    "name": card["name"],
                    "attack": card["attack"],
                    "cost": card["cost"],
                    "health": card["health"],
                })

    with open('../data/hearthstone_clean_cards_data.json', 'w', encoding='utf-8') as f:
        json.dump(new_cards_data, f, ensure_ascii=False, indent=4)


def main():
    cards_data = None
    with open('../data/hearthstone_raw_cards_data.json') as f:
        cards_data = json.load(f)

    clean_data(cards_data)


if __name__ == "__main__":
    main()
