class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            playerHand = game_state["players"][game_state["in_action"]]["hole_cards"]
            commonCards = game_state["community_cards"]
            allCards = []
            for dict_ in playerHand:
                allCards.append(dict_)

            for dict_ in commonCards:
                allCards.append(dict_)

            sortedCards = self.sort(allCards)
            multiply = self.find_set(sortedCards)


            
            return game_state["players"][game_state["in_action"]]["stack"] * self.percent(multiply)
        except:
            return 900

    def percent(self, multiply):
        if multiply >= 500:
            return 1
        elif multiply >= 113:
            return 0.7
        elif multiply >= 60:
            return 0.4
        elif multiply >= 16:
            return 0.1
        else:
            return 0


    def straight(self, cards_list):
        ammoutOfCards = len(cards_list)
        if ammoutOfCards == 5:
            if (cards_list[-1]["rank"] - ammoutOfCards) == cards_list[0]["rank"]+1:
                return cards_list[-1]["rank"] * 4000
        elif ammoutOfCards == 6:
            if (cards_list[-2]["rank"] - 5 == cards_list[1]["rank"]+1):
                return cards_list[-2]["rank"] *  4000
            elif (cards_list[-1]["rank"] - 5 == cards_list[2]["rank"]+1):
                return cards_list[-1]["rank"] *  4000
        elif ammoutOfCards == 7:
            if (cards_list[-3]["rank"] - 5 == cards_list[1]["rank"]+1):
                return cards_list[-3]["rank"] * 4000
            elif (cards_list[-2]["rank"] - 5 == cards_list[2]["rank"]+1):
                return cards_list[-2]["rank"] * 4000
            elif (cards_list[-1]["rank"] - 5 == cards_list[3]["rank"]+1):
                return cards_list[-1]["rank"] * 4000
    
    
    def sort(self, card_list):
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

        all_cards_sorted = sorted(card_list, key=lambda k: k['rank'])
        return all_cards_sorted

    def find_pair(self, card_list):
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

    def find_max(self, card_list):
        result = self.sort(card_list)[-1]['rank']
        return int(result)

    def find_set(self, card_list):
        return max(self.find_max(card_list), self.find_pair(card_list), self.straight(card_list))

    def showdown(self, game_state):
        pass