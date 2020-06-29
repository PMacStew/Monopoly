from time import sleep
from random import randint
from typing import Tuple

space_order = ["Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax", "Reading Railroad",
               "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue", "Jail", "St.Charles Place",
               "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad", "St. James Place",
               "Community Chest", "Tennessee Avenue", "New York Avenue", "Free Parking", "Kentucky Avenue", "Chance",
               "Indiana Avenue", "Illinois Avenue", "B. & O. Railroad", "Atlantic Avenue", "Vermont Avenue",
               "Water Works", "Marvin Gardens", "Go To Jail", "Pacific Avenue", "North Carolina Avenue",
               "Community Chest", "Pennsylvania Avenue", "Short Line", "Chance", "Park Place", "Luxury Tax",
               "Boardwalk"]
property_details = [
    "Go", 200, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, "Mediterranean Avenue", 60, "brown", 2, 4, 10, 30, 90, 160,
    250, 50, 0, 0, "Community Chest", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, "Baltic Avenue", 60, "brown", 4, 8, 20,
    60, 180, 320, 450, 50, 0, 0, "Income Tax", 200, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, "Reading Railroad", 200,
    "railroad", 25, 50, 100, 200, 8, 9, 10, 11, 0, 0,
    "Oriental Avenue", 100, "lightBlue", 6, 12, 30, 90, 270, 400, 550, 50, 0, 0, "Chance", 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 0, 0, "Vermont Avenue", 100, "lightBlue", 6, 12, 30, 90, 270, 400, 550, 50, 0, 0,
    "Connecticut Avenue", 120, "lightBlue", 8, 16, 40, 100, 300, 450, 600, 50, 0, 0, "Jail", 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 0, 0, "St.Charles Place", 140, "pink", 10, 20, 50, 150, 450, 625, 750, 100,
    0, 0, "Electric Company", 150, "utility", 4, 10, 6, 7, 8, 9, 10, 11, 0, 0, "States Avenue", 140, "pink", 10, 20,
    50, 150, 450, 625, 750, 100, 0, 0, "Virginia Avenue", 160, "pink", 12, 24, 60, 180, 500, 700, 900, 100,
    0, 0, "Pennsylvania Railroad", 200, "railroad", 25, 50, 100, 200, 8, 9, 10, 11, 0, 0, "St. James Place", 180,
    "orange", 14, 28, 70, 200, 550, 750, 950, 100, 0, 0, "Community Chest", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    0, 0, "Tennessee Avenue", 180, "orange", 14, 28, 70, 200, 550, 750, 950, 100, 0, 0, "New York Avenue", 200,
    "orange", 16, 32, 80, 220, 600, 800, 1000, 100, 0, 0, "Free Parking", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    0, 0, "Kentucky Avenue", 220, "red", 18, 36, 90, 250, 700, 875, 1050, 150, 0, 0, "Chance", 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 0, 0, "Indiana Avenue", 220, "red", 18, 36, 90, 250, 700, 875, 1050, 150, 0, 0, "Illinois Avenue",
    240, "red", 20, 40, 100, 300, 750, 925, 1100, 150, 0, 0, "B. & O. Railroad", 200, "railroad", 25, 50, 100,
    200, 8, 9, 10, 11, 0, 0, "Atlantic Avenue", 260, "yellow", 22, 44, 110, 330, 800, 975, 1150, 150,
    0, 0, "Ventnor Avenue", 260, "yellow", 22, 44, 110, 330, 800, 975, 1150, 150, 0, 0, "Water Works", 150,
    "utility", 4, 10, 6, 7, 8, 9, 10, 11, 0, 0, "Marvin Gardens", 280, "yellow", 24, 48, 120, 360, 850, 1025,
    1200, 150, 0, 0, "Go To Jail", 10, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, "Pacific Avenue", 300, "green", 26, 52,
    130, 390, 900, 1100, 1275, 200, 0, 0, "North Carolina Avenue", 300, "green", 26, 52, 130, 390, 900, 1100,
    1275, 200, 0, 0, "Community Chest", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, "Pennsylvania Avenue", 320, "green",
    28, 56, 150, 450, 1000, 1200, 1400, 200, 0, 0, "Short Line", 200, "railroad", 25, 50, 100, 200, 8, 9, 10,
    11, 0, 0, "Chance", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, "Park Place", 350, "darkBlue", 35, 70, 175, 500, 1100,
    1300, 1500, 200, 0, 0, "Luxury Tax", 100, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, "Boardwalk", 400, "darkblue", 50,
    100, 200, 600, 1400, 1700, 2000, 200, 0, 0]

# 1. property 2. price 3. color 4. rent 5. rent with color set. 6. 1 house rent 7. 2 house rent 8. 3 house rent
# 9. 4 house rent 10. hotel rent 11. house cost 12. Who owns it 13. how many houses it has
print(len(property_details))
current_player = 1
player_data = []
play = True
begin = True
# Explaining how to answer questions
print("For yes or no questions, you must type exactly yes or no.")
sleep(2)
print("For questions that require a numeric value, you must type only a numeric value.")
sleep(2)
# testing player to see if they understand
while begin:
    start = str(input("Are you ready to continue: "))
    if start.upper() != "YES":
        print("Oooops! Try again.")
        sleep(2)
    else:
        begin = False
player_amount = int(input("How many players do you have: "))
for i in range(player_amount):
    # 1. Amount of money 2. Space landed on 3. In jail
    player_data.append([1500, 0, False])
while play:
    property_monopoly = False
    property_monopoly_details = []
    print("It is now player " + str(current_player) + "'s turn.")
    sleep(2)
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    roll = player_data[current_player - 1][1] + die1 + die2
    print("You rolled a " + str(die1) + " and a " + str(die2))
    if roll >= 40:
        roll = roll - 40
    sleep(1)
    print("Congratulations! You have landed on " + property_details[roll * 13] + ". Its color is " + property_details[(roll * 13) + 2])
    sleep(2)
    player_data[current_player - 1][1] = roll
    # Other random properties
    if roll == 0 or roll == 2 or roll == 4 or roll == 5 or roll == 7 or roll == 10 or roll == 12 or roll == 15 or roll == 17 or roll == 20 or roll == 22 or roll == 25 or roll == 28 or roll == 30 or roll == 33 or roll == 35 or roll == 36 or roll == 38:
        print("hello")
    # regular buyable properties
    else:
        balance = player_data[current_player - 1][0]
        print("The price of " + property_details[roll * 13] + " will be $" + str(property_details[roll * 13 + 1]))
        sleep(2)
        print("You have $" + str(player_data[current_player - 1][0]))
        sleep(2)
        purchase = str(input("Would you like to buy it: "))
        sleep(1)
        #If they want to buy it
        if purchase.upper() == "YES":
            balance = balance - property_details[(roll * 13) + 1]
            player_data[current_player - 1].append(property_details[roll * 13])
            player_data[current_player - 1].append(property_details[(roll * 13) + 2])
            sleep(1)
            print("You have just bought " + (property_details[roll * 13]))
            sleep(1)
            print("Your balance is now " + str(balance))
    #checking if you can buy houses
    for i in range(40):
        color_occurences = player_data[current_player - 1].count(property_details[(i * 13) + 2])
        if color_occurences == 3 or (color_occurences == 2 and (property_details[(i * 13) + 2] == "brown" or property_details[(i * 13) + 2] == "darkblue")):
            property_monopoly = True
            property_monopoly_details.append(property_details[(i * 13) + 2])
            property_monopoly_details.append(property_details[i * 13])
    #Asking if you would like to by houses.
    if property_monopoly:
        houses = input("Would you like to buy some houses")
        if houses.upper() == "YES":
            print("Would you like to buy houses on...")
            #asking which property
            for i in range(len(property_monopoly_details) / 2):
                print(str(i + 1) + ". " + property_monopoly_details[i * 2] + ". House number: " + str(property_details[property_details.index(property_monopoly_details[i * 2]) + 12]))
            print("Make sure to enter a numerical value")
            house_property = input("Which house would you like to buy houses on: ")
            house_number = property_details[property_details.index(property_monopoly_details[((house_property - 1) * 2) + 1]) + 12]
            select_property = property_details.index(house_number) - 12
            #informing how many houses you can buy.
            buyable_houses = 4 - house_number
            if buyable_houses >= 1:
                if buyable_houses == 1:
                    print("You can buy " + str(buyable_houses) + " house")
                else:
                    print("You can buy " + str(buyable_houses) + " houses")
                print("Your balance is $" + str(balance))
                move = True
                while move:
                    house_purchase = int(input("How many houses would you like to purchase"))
                    if house_purchase > buyable_houses or house_purchase <= 0:
                        print("Ooops! Invalid house number. Try again")
                    else:
                        move = False
                balance = balance - (house_purchase * property_details[select_property + 10])
                print("Your balance is now $" + balance)
                property_details[select_property + 12] = property_details[select_property + 12] + house_purchase
            if house_number == 4:
                print("You can buy a hotel")
            elif house_number < 4:
                print("If you buy all the houses you can also buy a hotel. ")
    player_data[current_player - 1][0] = balance

print("You have landed on " + property_details[player_data[current_player - 1][1] * 11])
print(player_data)
