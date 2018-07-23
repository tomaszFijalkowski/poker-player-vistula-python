class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            self.logGameState(game_state)
        except:
            pass
        finally:
            print('DZIALA')
            return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"]

    def logGameState(self, game_state):
        print("_______________________________________________________________________________:")
        print(game_state["current_buy_in"])
        print(game_state["players"][game_state["in_action"]]["bet"]) 
        print(game_state["minimum_raise"])
        print(game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"] + game_state["minimum_raise"])
        print(game_state["players"][game_state["in_action"]]["hole_cards"])
        print("_______________________________________________________________________________XXXXX")


    def showdown(self, game_state):
        pass