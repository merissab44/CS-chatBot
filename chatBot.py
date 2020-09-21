from random import choice

def get_bot_response(user_response):
    bot_response_coffee = ["Great morning wake up drink!", "Our most popular is the medium roast", "black is the way to go", "did you know it's helpful to always say the size of the drink first"]
    bot_response_frapp = ["perfect for outings with friends!", "those can be expensive but totally worth it" , "did you know that baristas don't know the secret menu drinks, always have the ingredients ready"]
    bot_response_latte = ["I love doing latte art!", "there's a competition every week for baristas", "if you order a drink for here, you automatically get the latte art"]
    bot_response_refresher = ["my personal favorite!", "those have caffeine as well", "great summer drink!"]

    if user_response == "coffee":
        return choice(bot_response_coffee)
    elif user_response == "frappaccino" or user_response == "frapp":
        return choice(bot_response_frapp)
    elif user_response == "latte":
        return choice(bot_response_latte)
    elif user_response == "refresher":
        return choice(bot_response_refresher)
    else:
        return "I don't have any interesting thoughts about that drink, I'll have to try it out!"

print("Welcome to Starbucks bot, I'm David!")
print("please enter your favorite type of drink( coffee, frappaccino, latte, or refresher?) ")

user_response = ""

while True:
     # asks the user if they want to go again, if yes it will ask the first question, if no the program ends
    user_response = input("what's your favorite Starbucks drink? ")
    
    if user_response == "I don't have one":
        break

    bot_response = get_bot_response(user_response)
    print(bot_response)
   
    