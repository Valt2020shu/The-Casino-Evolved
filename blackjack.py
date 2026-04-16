import random

base_deck = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
remaining_cards = []

class player:
    def __init__(self,user_type,username):
        self.user_type = user_type
        self.current_points =  0
        self.username = username
        self.cards_held = []
    
    

def weight(current_points, remaining_cards):
    chance = 0.5
    for i in remaining_cards:
        if i + current_points < 21:
            chance += 0.1
        elif i + current_points > 21:
            chance -= 0.1
        else:
            chance += 0.2
    
    if chance > 1:
        chance = 1

    return chance


def pull(user, remaining_cards, forced = False):
    if user.user_type == 'Challenger' or forced:
        card_pulled = remaining_cards[random.randint(0,len(remaining_cards)-1)]
        remaining_cards.remove(card_pulled)
        user.cards_held.append(card_pulled)
        user.current_points += (base_deck.index(card_pulled) + 1)
        if not forced:
            print(user.username, f'pulled {card_pulled}')

        return True
    
    if user.user_type == 'Computer' and not forced:
        
        if random.random() <= weight(user.current_points, remaining_cards):
            card_pulled = remaining_cards[random.randint(0,len(remaining_cards)-1)]
            remaining_cards.remove(card_pulled)
            user.cards_held.append(card_pulled)
            user.current_points += (base_deck.index(card_pulled) + 1)
            if not forced:
                print(user.username, f'pulled {card_pulled}')

            return True
        else:
            return False



    



House = player('Computer','The Dealer')
player_name = input("Enter user: ")
Challenger = player('Challenger', player_name)

def game(Challenger, House, remaining_cards):
    remaining_cards = list(base_deck)
    pull(Challenger, remaining_cards,True)
    pull(House, remaining_cards,True)
    pull(Challenger, remaining_cards,True)
    pull(House, remaining_cards,True)

    turn_end(House, Challenger)
    while True:
        while True:
            user_input = input("Do you want to Hit (Draw) or Stand (Don't Draw): ").strip().title()
            if user_input in ('Hit', 'Draw'):
                break
            else:
                print("Please choose a valid option")

        if user_input == 'Hit':
            pull(Challenger, remaining_cards)
        else:
            print(Challenger.username, 'chose to stand')
        
        if not pull(House, remaining_cards) and user_input == 'Stand':
            print("Game Over")
            game_end(House,Challenger)
            break
        
        turn_end(House,Challenger)
        game_end(House,Challenger)
        



def turn_end(House, Challenger):
        print(House.username, f'has',end= ' ')
        for i in House.card_held:
            print(i,end=' ')

        print(Challenger.username, f'has',end= ' ')
        for i in Challenger.card_held:
            print(i,end=' ')

def game_end(House, Challenger): 
    house_current_points = House.current_points
    challenger_current_points = Challenger.current_points

    if house_current_points == 21:
        if challenger_current_points == 21:
            print("Draw")
        else:
            print("House Wins!")
    
    elif challenger_current_points == 21:
        print(f"{Challenger.username} Wins!")
    
    elif challenger_current_points > 21:
        if house_current_points > 21:
            if challenger_current_points == house_current_points:
                print("Draw")
            elif challenger_current_points > house_current_points:
                print("House Wins!")
            else:
                print(f"{Challenger.username} Wins!")
        else:
            print("House Wins!")
    elif house_current_points > 21:
        print(f"{Challenger.username} Wins!")
    
    elif challenger_current_points < 21:
        if house_current_points < 21:
            if challenger_current_points == house_current_points:
                print("Draw")
            elif challenger_current_points > house_current_points:
                print(f"{Challenger.username} Wins!")
            else:
                print("House Wins!")
    
        else:
            print(f"{Challenger.username} Wins!")
        
    