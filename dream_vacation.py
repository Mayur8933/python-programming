dream_vacation = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name?")
    response = input("\nIf you could visit one place in the world,where would you go?")
    dream_vacation[name] = response

    repeat = input("\nWould you like to let another person respond?")
    if repeat == "no":
        poll_active = False
print("\n----POLL RESULTS----\n")           
for name,response in dream_vacation.items():
    print("-",name,response)

   
