def bill():
    total=0.
    emotion= raw_input('Welcome to cafe Dunlea, how are you?')
    people= float(raw_input("Glad to hear that! How many people are in your party?"))
    print ("Ok, take a seat. Here is our menu.")

    template = ("***CAFE DUNLEA MENU***.\n"
                "1. Minion's choice Banana------------------------- $500.\n"
                "2. 'Get back in your seat' ----------------------- $10.\n"
                "3. 'STOP EATING IN MY CLASS'  -------------------- $600.\n"
                "4.'Yellow cups up if you're done'----------------- $5000.\n"
                "5. Mission Impossible on forever loop ------------ priceless.")
    print(template)
    serve= raw_input("Please call me over by typing 'server' when you're ready to order")
    if serve == 'server':
        choices = raw_input('Please type the number of the items you would like')
    if '1' in choices:
        total=total+500.
    if '2' in choices:
        total=total+10.
    if '3' in choices:
        total=total+600.
    if '4' in choices:
        total=total+5000.
    if '5' in choices:
        total=total+9999999999999999999999999999999999999999999999999999999999999999999999.
    print('Excellent choices! The dunleaisms will be right out.')
    print("The food was horrible")
    tip = float(raw_input('What percent are you tipping? Enter .15, .2 or another amount '))
    tax= 1.0775
    cost= (total*tax*(1+tip))/people
    print ('Your total cost is', cost, '! Thank you for stopping by CAFE DUNLEA.')
