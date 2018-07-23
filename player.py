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

            self.straight(sortedCards)



            # print("_______________________________________________________________________________:")
            # print(game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"])
            # print("commonCards: ", commonCards)
            # print("playerHand: ", playerHand)
            # print("allCards: ", allCards)
            # print("_______________________________________________________________________________XXXXX")

            #return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"]
            return game_state["players"][game_state["in_action"]]["stack"]
        except:
            return 900
            #return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"]


    def straight(self, card_list):
        ammoutOfCards = len(card_list)
        if ammoutOfCards == 5:
            if (cards_list[-1]["rank"] - ammoutOfCards) == cards_list[0]["rank"]+1:
                return cards_list[-1]["rank"] * 4000
        elif ammoutOfCards == 6:
            if (cards_list[-2]["rank"] - 5 == cards_list[1]["rank"]+1):
                return cards_list[-2]["rank"] *  4000
            elif (cards_list[-1]["rank"] - 5 == cards_list[2]["rank"]+1):
                return cards_list[-1]["rank"] *  4000
        elif ammoutOfCards == 6:
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

    def showdown(self, game_state):
        pass