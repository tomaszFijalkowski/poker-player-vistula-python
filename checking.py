all_cards = [{"rank": "4", "suit": "hearts" },
{"rank": "K", "suit": "diaonds" },
{"rank": "Q", "suit": "spades" },
{"rank": "K", "suit": "clubs" },
{"rank": "A", "suit": "hearts" },
{"rank": "A", "suit": "clubs" },
{"rank": "4", "suit": "spades" },
]

def sor(list):
    for card in list:
        if card['rank'] == 'J':
            card['rank'] = 11
        elif card['rank'] == "Q":
            card['rank'] = 12
        elif card['rank'] == "K":
            card['rank'] = 13
        elif card['rank'] == "A":
            card['rank'] = 14
        else:    
            card['rank'] = int(card['rank'])

    all_cards_sorted = sorted(all_cards, key=lambda k: k['rank'])
    return all_cards_sorteds