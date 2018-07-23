class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            playerHand = game_state["players"][game_state["in_action"]]["hole_cards"]
            commonCards = game_state["community_cards"]
            allCards = []
            for dict in playerHand:
                allCards.append(dict)

            for dict in commonCards:
                allCards.append(dict)

            print("_______________________________________________________________________________:")
            print(game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"])
            print("commonCards: ", commonCards)
            print("playerHand: ", playerHand)
            print("allCards: ", allCards)
            print("_______________________________________________________________________________XXXXX")
            
            return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"]
        except:
            return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"]


    def showdown(self, game_state):
        pass