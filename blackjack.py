
from p1_random import P1Random

# sets the varibales for the game equal to zero
rng = P1Random()
player_wins = 0
dealer_wins = 0
tied_games = 0
games_played = 1

# list is created to hold users card values and dealer card values
rand_list = [0]
rand_dealer = [0]

# sets condition for loop equal to 0
game = True
action = True
menu = "\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit"

# while loop iterates every time a new game is started
while game == True:

    # card is drawn and start game is printed
    user_card = rng.next_int(13) + 1
    print(f"\nSTART GAME #{games_played}")

    # runs if user card is in the range 1-11, prints card value and hand value by adding card value to the list
    if 1 < user_card < 11:
        print(f"\nYour card is a {user_card}!")
        rand_list.append(user_card)
        print(f"Your hand is: {sum(rand_list)}")

    # runs if the users card is 1
    if user_card == 1:
        print(f"Your card is a ACE!")
        rand_list.append(user_card)
        print(f"Your hand is: {sum(rand_list)}")

    # runs if the users card is 11
    if user_card == 11:
        print(f"Your card is a JACK!")
        rand_list.append(user_card - 1)
        print(f"Your hand is: {sum(rand_list)}")

    # runs if the users card is 12
    if user_card == 12:
        print(f"Your card is a QUEEN!")
        rand_list.append(user_card - 2)
        print(f"Your hand is: {sum(rand_list)}")

    # runs if the users card is 13
    if user_card == 13:
        print(f"Your card is a KING!")
        rand_list.append(user_card - 3)
        print(f"Your hand is: {sum(rand_list)}")

    # runs throughout each game, breaks out when the game is done
    while action == True:

        # runs when the sum of the users cards is equal to 21 and breaks out of loop
        if sum(rand_list) == 21:
            print("BLACKJACK! You win!")
            games_played += 1
            player_wins += 1
            rand_list.clear()
            break

        # if the sum of the users cards is greater than 21 if breaks out of the loop
        if sum(rand_list) > 21:
            print("You exceeded 21! You lose.")
            games_played += 1
            dealer_wins += 1
            rand_list.clear()
            break

        # prints the menu options and prompts user for input
        print(menu)
        user_option = int(input("\nChoose an option: "))

        # if the users menu option is between 0-4 it will request valid input and go to the start of the loop
        if user_option <= 0 or user_option > 4:
            print("\nInvalid input!\nPlease enter an integer value between 1 and 4.")
            continue

        # if users menu option is equal to 1 statement will run
        if user_option == 1:

            # draws card
            user_card = rng.next_int(13) + 1

            # if users card is 2-10, card value will print and be added to the rest of the #'s in list to output their hand
            if 1 < user_card < 11:
                print(f"\nYour card is a {user_card}!")
                rand_list.append(user_card)
                print(f"Your hand is: {sum(rand_list)}")

            # if users card is 1 card value will print and be added to the rest of the #'s in list to output their hand
            if user_card == 1:
                print(f"Your card is a ACE!")
                rand_list.append(user_card)
                print(f"Your hand is: {sum(rand_list)}")

            # if users card is 11 card value will print and be added to the rest of the #'s in list to output their hand
            if user_card == 11:
                print(f"Your card is a JACK!")
                rand_list.append(user_card - 1)
                print(f"Your hand is: {sum(rand_list)}")

            # if users card is 12 card value will print and be added to the rest of the #'s in list to output their hand
            if user_card == 12:
                print(f"Your card is a QUEEN!")
                rand_list.append(user_card - 2)
                print(f"Your hand is: {sum(rand_list)}")

            # if users card is 13 card value will print and be added to the rest of the #'s in list to output their hand
            if user_card == 13:
                print(f"Your card is a KING!")
                rand_list.append(user_card - 3)
                print(f"Your hand is: {sum(rand_list)}")

        # if users option is 2
        elif user_option == 2:

            # dealers hand will be drawn and printed and added to list along with the users hand
            dealer_hand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Your hand is: {sum(rand_list)}")
            rand_dealer.append(dealer_hand)

            # before the program exits the loop one is added to the # of games played and lists are cleared

            # if dealers hand stored in the list is greater than 21 user wins
            if sum(rand_dealer) > 21:
                print("\nYou win!")
                player_wins += 1            # one is added to the games player has won
                games_played += 1
                rand_dealer.clear()
                rand_list.clear()
                break

            # if the dealer hand is equal to the users hand
            if sum(rand_dealer) == sum(rand_list):
                print("\nIt's a tie! No one wins!")
                tied_games += 1             # one is added to amount of tied games
                games_played += 1
                rand_dealer.clear()
                rand_list.clear()
                break

            # if of dealers hand is 21 or less & dealers hand is greater that users hand, dealer wins
            if sum(rand_dealer) <= 21 and sum(rand_dealer) > sum(rand_list):
                print("\nDealer wins!")
                dealer_wins += 1            # one is added to the number of dealer wins
                games_played += 1
                rand_dealer.clear()
                rand_list.clear()
                break

            # if dealers hand is 21 or less & users hand is greater than dealers hand user wins
            if sum(rand_dealer) <= 21 and sum(rand_list) > sum(rand_dealer):
                print("\nYou win!")
                player_wins += 1            # one is added to the number of games player has won
                games_played += 1
                rand_dealer.clear()
                rand_list.clear()
                break

        # if user option is equal to 3, game stats will be printed
        elif user_option == 3:
            print(f"\nNumber of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {tied_games}")
            print(f"Total # of games played is: {games_played - 1}")        # counts number of games completed
            per_player_wins = 100 * (player_wins / (player_wins + dealer_wins + tied_games))        # calculates %
            per_player_wins = round(per_player_wins, 1)         # rounds % to 1 decimal place
            print(f"Percentage of Player wins: {per_player_wins}%")

        # if user menu option is 4 game and action are equal to False so the loops becomes false and are broken out of
        else:
            game = False
            action = False
