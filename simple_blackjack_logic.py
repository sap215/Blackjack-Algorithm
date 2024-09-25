import random

cards = ['2','4','5','6','7','8','9','10','J','Q','K','A']
cards_in_deck = cards * 4
opponent_hand = []
your_hand = []

def points_calculator(hand):
    points = 0

    for card in hand:
        if card in ['J', 'Q', 'K']:
            points += 10
        elif card == 'A' and (points + 11) < 21:
            points += 11
        elif card == 'A' and (points + 21) > 21:
            points += (21 - points)
        else: 
            points += int(card)

    return points

def stand():
    print("Standing")
    return 0

def hit():
    new_card = random.choice(cards_in_deck)
    cards_in_deck.remove(new_card) 
    your_hand.append(new_card)
    print("You drew:", new_card)

def hit_or_stand():
    while True:
        print("Hit or Stand? (H/S): ")
        user_input = input().upper()  
        
        if user_input == 'H':
            hit()
            player_points = points_calculator(your_hand)
            print("Your hand:", your_hand)
            print("Your points:", player_points)
            if points_calculator(your_hand) > 21:
                print("You busted!")
                break  
        elif user_input == 'S':
            stand()
            break  
        else:
            print("Invalid input. Please type 'H' for Hit or 'S' for Stand.")
    

def starting_hand(hand):
    for _ in range(2):
        new_card = random.choice(cards_in_deck)
        cards_in_deck.remove(new_card) 
        hand.append(new_card)
        
def main():
    starting_hand(opponent_hand)
    starting_hand(your_hand)
    
    print("Opponent's hand:", opponent_hand)
    print("Opponent's points (visible):", points_calculator(opponent_hand[:1])) 
    
    print("Your hand:", your_hand)
    print("Your points:", points_calculator(your_hand))

    hit_or_stand()

    your_points = points_calculator(your_hand)
    opponent_points = points_calculator(opponent_hand)

    print("------------------------------------")

    if your_points == 21:
        print("You got 21 points. You win!")
    elif your_points > 21:
        print("You lose! You busted with", your_points, "points")
    else:
        print("Opponent's hand:", opponent_hand)
        print("Opponent's points:", opponent_points)
        
        if opponent_points == 21:
            print("Opponent wins with a blackjack!")
        elif opponent_points > 21:
            print("Opponent busted! You win!")
        elif your_points > opponent_points:
            
            print("You win!")
        elif your_points < opponent_points:
            print("You lose!")
        else:
            print("It's a tie!")

#   TEST CASES
#    print(points_calculator(['A', '2', '6', '6']))  # Output: 25
#    print(points_calculator(['A', '2', '3']))  # Output: 16
#    print(points_calculator(['1', '6']))  # Output: 16
#    print(points_calculator(['J', 'Q']))  # Output: 20h

if __name__ == "__main__":
    main()
