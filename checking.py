all_cards = [{"rank": "4", "suit": "hearts" },
{"rank": "6", "suit": "hearts" },
{"rank": "Q", "suit": "spades" },
{"rank": "9", "suit": "clubs" },
{"rank": "2", "suit": "hearts" },
{"rank": "A", "suit": "clubs" },
{"rank": "4", "suit": "spades" },
]

def sort(card_list):
    for card in card_list:
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
    return all_cards_sorted

def find_pair(card_list):
    pairs = []
    result = 0
    for card in card_list:
        for another_card in card_list:
            if card['rank'] == another_card['rank']:
                if card['suit'] != another_card['suit']:
                    pairs.append(card['rank'])
                    # result += int(card['rank'])/2
    print(pairs) 
    if len(pairs) >4:
        result = sum(pairs[2:])/2*25
    else:
        result = sum(pairs)/2*8
    return int(result)

def find_max(card_list):
    result = sort(card_list)[-1]['rank']
    print(result)
    return int(result)

find_max(all_cards)