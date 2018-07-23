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

            print("_______________________________________________________________________________:")
            print(game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"])
            print("commonCards: ", commonCards)
            print("playerHand: ", playerHand)
            print("allCards: ", allCards)
            print("_______________________________________________________________________________XXXXX")
            
            return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"]
        except:
            return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"]

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

    def showdown(self, game_state):
        pass