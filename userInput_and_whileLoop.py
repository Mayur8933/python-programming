name = input("enter your name: ")
your_name_message = f"your name is {name}" #using variables inside a string,format,%
print(your_name_message )

#integers

age = input("enter your age?")#by default it is string
age = int(age)
if age > 21:
    print("you are older than 21")
print(f"age is {age}")

#input()

number = input("enter some number: ")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is Even")#f=format
else:
    print(f"The number {number} is odd")

num = 1
while num<=10:
    print(num)
    num+=1

#input:quit

prompt = input("\n\nTell me something,add I will repeat it back to you: ")
prompt += input("\nEnter 'quit' to end the program.\n")
message = ""
while message != "quit":
    message = input(prompt)
    print(f"\n{message}")
    if message == "stop":
        print("breaking the loop")
        break

#continue
#print all the odd numbers between 1 to 10

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print("_______________________")    

#infinite loop

x = 1
while x<=5:
    print(x)
    x+=1 #infinite loop , if we dont increment the value

#you want to create infinite loop on purpose

while True:
    user_input = input("Tell me something about you (quit to end the program):")
    print(user_input)
    if user_input == "quit":
        break
print("________________________-")    

#using while loop with some data structures : ist,dict to process some data

unconfirmed_users = ["alice","brian","scott"]
confirmed_users = []


while unconfirmed_users :
    current_user = unconfirmed_users.pop()
    print(f"verifying user {current_user}...")
    confirmed_users.append(current_user)
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("________________________________________")    

responses = {}

#set some flag to indicate if polling is active or not

polling_active = True
while polling_active:
    name = input("\nwhat is your name? ")
    response = input("what is your favourite mountain?")#store this in dictionary
    responses[name] = response

    repeat = input("would you like to let another person respond.(yes/no)")

    if repeat == "no":
        polling_active = False

#polling is complete ,print the result

print("\n-----------poll results-----------")

for name,response in responses.items():#reading a dictionary
    print(name,response)

    
     
    
    
    
