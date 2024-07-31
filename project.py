import clear
import art
import re

def bid_war():

    while True:
        clear.clear_console()
        print(F"{art.logo}\nWelcome to the Secret Auction")

        bid_war_dictionary = {}
        highest_bid = 0
        bid_name = ""

        while True:
           
            while True:
                name = input("What is the name?:\n")
                if not re.match("^[a-zA-Z]+$", name):
                    print("Please provide an alphabetical name without numbers, spaces, or symbols")
                elif name in bid_war_dictionary:
                    print("Name already exists, please provide a unique name")
                else:
                    break
            
            while True:
                bid_price = input("What is your bid?:\n$")
                try:
                    bid_price = float(bid_price)
                    break
                except ValueError:
                    print("Please provide a valid number - Either an integer or float")

            bid_war_dictionary[name] = bid_price
            # print(bid_war_dictionary)

            additional_bid = input("Would you like to add another bid? - Type Y for yes or anything else to finalize Auction: ").lower()
            if additional_bid != "y":
                for key in bid_war_dictionary:
                    if bid_war_dictionary[key] > highest_bid:
                        highest_bid = bid_war_dictionary[key]
                        bid_name = key
                print(F"The highest bid is ${highest_bid:.2f} by {bid_name}")
                break
            
            #Clearing console so new user DOES NOT see the previous user's bid
            clear.clear_console()
        
        reset = input("Would you like to start another Auction? - Type Y for yes or anything else to exit Auction: ").lower()
        if reset != "y":
            print("Exiting...")
            return

bid_war()