print("Program Started!")

print("Please enter a standard character:")
character = input()

if (len(character) == 1):
    print("The ASCII code for {} is {}".format(character, ord(character))
else:
    print("A single character was expected.")

print("Program Ended!")
print("Program Started!")

print("Please enter an ASCII code:")
code = int(input())

if (code >= 32 and code <= 126):
    print("The character represented by the ASCII value {} is: {}".format(code, chr(code))
else:
    print("The character cannot be displayed.")

print("Program Ended!")

# The function
def listen():

    # Ask user for the sound 
    print("What sound did I hear?")
    sound = input() 

    # Display message
    print("\nThat was a loud", sound)


# Call to function
listen()
# The function
def identify():
    # Ask user for what lies ahead
    print("What lies before us?")
    response = input() 

    # Display message
    if (response == "a large boulder"):
        print("It's time to run!")
    else:
        print("We will be fine.")


# Call to function
identify()
# The function with a single parameter named 'plan'
def escape_by(plan):
    # Determine which message to display
    if (plan == "jumping over"):
        print("We cannot escape that way! The boulder is too big!")
    elif (plan == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif (plan == "going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("Not sure about that plan!")

# Calls to the function
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
def crossed_bridge(steps):
    # Display each step 
    for step in range(steps):
        print("Crossed step.") 

    # Display message
    if (steps > 5):
        print("The bridge is collapsing!")
    else: 
        print("We must keep going!")

  ef climb_ladder(steps_remaining, steps_crossed):
    # Compare and display a suitable message
    if (steps_remaining > steps_crossed):
        print("Still some way to go!")
    else:
        print("We are almost there!") 


climb_ladder(5, 2)
climb_ladder(2, 5)
ef display_ladder(steps):
    # Display each step 
    for step in range(steps):
        print("| |")
        print("***") 

    # Display bottom of ladder
    print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight) / 2
    return avg_weight

def run():
    # retrieve required user data
    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What is the weight of Beep?")
    beep_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    # determine and carry out action
    if (action == "sum"):
        answer = sum_weights(beep_weight, bop_weight)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
    elif (action == "average"):
        answer = calc_avg_weight(beep_weight, bop_weight)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
    else:
        print("I am not sure what you would like to do.")
      def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)

def display_lower_case(word):
    print(word.lower())

def display_upper_case(word):
    print(word.upper())

def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print("{} | {}".format(word, mirrored))

def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        # even repetition
        if (repetition % 2 == 0):
            print(display_lower_case(word))
        # odd repetition
        else:
            print(display_upper_case(word))

def run():
    print("Please enter a word:")
    word = input()

    # remember the user has not yet selected an option
    response = 0

    while (response != 6):
        # get the user's selection
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input()) 
 
        # determine and execute action
        if (response == 1):
            display_box(word)
        elif (response == 2):
            display_lower_case(word)
        elif (response == 3):
            display_upper_case(word)
        elif (response == 4):
            display_mirrored(word)
        elif (response == 5):
            display_repeated(word)
        elif (response == 6):
            break
        else:
            print("Unknown option.") 

run()
import random

print("Please enter the minimum value:")
min_value = int(input())

print("Please enter the maximum value:")
max_value = int(input())

random_number = random.randrange(min_value, max_value)

print("I am thinking of a number between {} and {}.".format(min_value, max_value))
print("Can you guess what it is?")

guess = 0

while(guess != random_number):
  print("Please enter a number:")
  guess = int(input())

  if (guess == random_number):
    print("Congratulations!")
    break
  elif (guess < random_number):
    print("Guess higher")
  else:
    print("Guess lower")
  
print("Game over!")
