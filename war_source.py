import random
#make tuples for cards ranks and suits and a dictionary for the power of each card
card_ranks = ('Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
card_values = {'Deuce':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, "Ten": 10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#class Card to create card for each rank and suit
class Cards():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#class Deck inherits Cards to create the whole deck of 52 cards so they can be shuffled and dealt
class Deck(Cards):
    def __init__(self):
        self.all_cards = []
        for i in card_ranks:
            for j in card_suits:
                card_created = Cards(j, i)
                self.all_cards.append(card_created)
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        print("Deck is shuffled and ready to play")
    
    def deal_cards(self):
        return self.all_cards.pop(0)

#class Player inherits Deck so a new player could draw cards for himself, then put cards on the table and collect them
class Player(Deck):
    def __init__(self, name):
        self.name = name
        self.player_cards = []

    def remove_one(self):
        return self.player_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.player_cards.extend(new_cards)
        else:
            self.player_cards.append(new_cards)

    def __str__(self):
        return "Player {} has {} cards".format(self.name, len(self.player_cards))

#the game logic
def run_game(pl1, pl2):
    #players cards
    player1_card = 'Default'
    player2_card = 'Default'
    #run the game while both players have cards, if one of them runs out of cards, the other wins
    while pl1.player_cards and pl2.player_cards:
        #draw next card for eact player by pressing enter key
        press_enter = 'Default'
        while press_enter != "":
            press_enter = input('Press Enter to draw card for player {}'.format(pl1.name))
            if press_enter == "":
                next_draw = pl1.remove_one()
                print('Player {} drew {}'.format(pl1.name, next_draw))
                break
            else:
                print('Enter is expected')
        player1_card = next_draw
        press_enter = 'Default'
        while press_enter != "":
            press_enter = input('Press Enter to draw card for player {}'.format(pl2.name))
            if press_enter == "":
                next_draw = pl2.remove_one()
                print('Player {} drew {}'.format(pl2.name, next_draw))
                break
            else:
                print('Enter is expected')
        player2_card = next_draw
        #end of draw
        #compare both players card values, higher value wins, if there is a draw they draw another 3 cards
        if player1_card.value > player2_card.value:
            pl1.add_cards(player1_card)
            pl1.add_cards(player2_card)
            print("player1 won {}\n------End of round-------".format(player2_card))
        elif player2_card.value > player1_card.value:
            pl2.add_cards(player2_card)
            pl2.add_cards(player1_card)
            print("player2 won {}\n------End of round-------".format(player1_card))
        elif player2_card.value == player1_card.value:
            have_winner = False
            pl1_draw_three_cards = []
            pl2_draw_three_cards = []
            #draw 3 cards in case of draw
            while pl1.player_cards and pl2.player_cards and have_winner == False:
                for card in range(0,3):
                    #check if one of the players doesnt have enough cards set have_winner to True, break, and the other wins
                    if not pl1.player_cards:
                        have_winner = True
                        break
                    if not pl2.player_cards:
                        have_winner = True
                        break                    
                    pl1_draw_three_cards.append(pl1.remove_one())
                    pl2_draw_three_cards.append(pl2.remove_one())
                #if they both have enough cards compare the last last card drawn, higher value wins, winner collect all
                if pl1_draw_three_cards[-1].value > pl2_draw_three_cards[-1].value and have_winner == False:
                    have_winner = True
                    pl1.add_cards(player1_card)
                    pl1.add_cards(player2_card)
                    pl1.add_cards(pl1_draw_three_cards)
                    pl1.add_cards(pl2_draw_three_cards)
                elif pl1_draw_three_cards[-1].value < pl2_draw_three_cards[-1].value and have_winner == False:
                    have_winner = True
                    pl2.add_cards(player2_card)
                    pl2.add_cards(player1_card)
                    pl2.add_cards(pl1_draw_three_cards)
                    pl2.add_cards(pl2_draw_three_cards)

    #call the winner
    if not pl1.player_cards:
        print("Winner is {}".format(pl2.name))
    else:
        print("Winner is {}".format(pl1.name))

#get number of players from user input
def get_num_players():
    num = 'Default'
    while num not in range(2,5):
        num = int(input("Enter number of players for war game(2-4): "))
    return num

new_deck = Deck()
new_deck.shuffle_deck()
#get number of players from user input
num_of_players = get_num_players()
print(num_of_players)
player1 = Player('Kris')
player2 = Player('Mris')
for i in range(0,26):
    player1.add_cards(new_deck.deal_cards())
    player2.add_cards(new_deck.deal_cards())

run_game(player1,player2)
