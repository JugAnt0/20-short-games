#1 SECRET SANTA (Happy Holidays!)

  
#import random
#import time
#import sys

#print("Welcome to Secret Santa!")

#num_players = int(input("Enter number of players (3-15): "))

#players = [f"Player {i+1}" for i in range(num_players)]

#random.shuffle(players)
#santas = players[1:] + players[:1]
#pairs = dict(zip(players, santas))

#input("Press Enter to reveal Secret Santas...")
#time.sleep(1)

#for player in players:
  #  print(f"\n{player}, you are Secret Santa for: {pairs[player]}")
  #  input("Press Enter when ready...")
  #  print("\n" * 50)

#print("All Secret Santas have been assigned!")
#sys.exit()






#2 TWO TRUTHS AND A LIE

#import time
#import sys

#print("Welcome to Two Truths and a Lie!")

#num_players = int(input("Enter number of players (3-10): "))

#players = [f"Player {i+1}" for i in range(num_players)]

#print("Prepare your statements:")
#print("• 2 TRUE statements")
#print("• 1 LIE")
#input("Press Enter when everyone is ready...")
#time.sleep(1)
#
#for player in players:
  #  print(f"\n{player}, it’s your turn to secretly choose your LIE.")
  #  input("Press Enter when ready (others look away)...")
   # print("\n" * 50)

#print("All players have prepared their statements.")
#print("Let the guessing begin!")
#sys.exit()






#3 MAFIA

#import random
#import time
#import sys

#print("Welcome to Mafia!")

#while True:
 #   num_players = int(input("Enter number of players (4-10): "))
#
#    if not (4 <= num_players <= 10):
#       print("Invalid number of players. Please enter a number between 4 and 10.")
  #      continue

 #   print("Let's begin the game!")
 #   input("Press Enter to assign roles...")
  #  time.sleep(1)


 #   players = [f"Player {i+1}" for i in range(num_players)]

   
  #  roles = ["Mafia", "Detective", "Doctor"] + ["Villager"] * (num_players - 3)
#    random.shuffle(roles)

    
 #   player_roles = dict(zip(players, roles))

    # Secretly reveal roles to each player
   # for player in players:
     #   print(f"\n{player}, your role is: {player_roles[player]}")
     #   input("Press Enter when you're done (make sure nobody else is looking)...")
     #   print("\n" * 50)  # Clear-ish screen

  #  print("All roles have been assigned. Let the game begin!")
  #  time.sleep(2)
  #  sys.exit()




#4 HOUSE DECOR
  

#import random
#import time

#print("Welcome to Antonio's House Decor Service (digital edition)!")
#time.sleep(2)

#rooms = {
#    1: ("Living Room", 
#        ["sofa", "coffee table", "TV stand", "bookshelf", "armchair"],
 #       ["modern", "rustic", "minimalist", "bohemian, industrial"]),
 #   2: ("Bedroom", 
 #       ["bed", "wardrobe", "nightstand", "dresser", "desk"],
#        ["contemporary", "vintage", "scandinavian", "eclectic", "traditional"]),
#    3: ("Kitchen", 
#        ["kitchen island", "bar stools", "pantry", "dining table", "cabinetry"],
#        ["farmhouse", "coastal", "transitional", "art deco", "mid-century modern"]),
#    4: ("Bathroom", 
 #       ["vanity", "shower", "bathtub", "toilet", "storage cabinet"],
 #       ["spa-like", "classic", "modern", "eclectic", "rustic"]),
 #   5: ("Backyard", 
 #       ["patio set", "grill", "garden bench", "fire pit", "hammock", "gazebo"],
 #       ["tropical", "zen", "cottage", "mediterranean", "modern"])
#}

#while True:
 #   print("\n----- ROOM SELECTION -----")
#    time.sleep(1)
#    for num, data in rooms.items():
#        print(f"{num}. {data[0]}")
#    print("6. Choose for me")

#    choice = int(input("Which room would you like to decorate? (1-6): "))

#    if choice == 6:
 #       choice = random.randint(1, 5)

 #   if choice in rooms:
  #      room_name, furniture, styles = rooms[choice]
   #     print(f"\nGreat! You chose the {room_name}.")
  #      time.sleep(1)

    #    style = input(f"Choose an interior style {styles}: ")
    #    time.sleep(1)

   #     main_piece = random.choice(furniture)
    #    secondary_1 = random.choice(furniture)
    #    secondary_2 = random.choice(furniture)

     #   print(f"\nYour {style} {room_name.lower()} will feature a {main_piece} as the centerpiece.")
     #   time.sleep(2)
     #   print(f"It will be complemented by a {secondary_1} and a {secondary_2} to complete the look.")
     #   time.sleep(3)
      #  print("\nReturning to Room Selection...")
      #  time.sleep(2)

   # else:
    #    print("Invalid choice. Please enter a number from 1 to 6.")
    #    time.sleep(2)






#5 Antonio's Fortune Telling Service (digital edition)
  
  
#import random
#import time

#print("Welcome to Antonio's Fortune Telling Service (digital edition)!")

#while True:
 #   p = input("Would you like to know your fortune? (yes/no): ").strip().lower()
 #   if p == 'yes':
  #      print("Ok, come inside..")
   #     time.sleep(1)
   #     print("What do you want to try first?")
  #      print("1.- Fortune Cookie")
  #      print("2.- Tarot cards")
   #     print("3.- Ball crystallus")
   #     print("4.- Talk")


      #  op = int(input("Choose from options 1 - 4: "))

     #   if op == 1:
        #    f = [ "You will face a great tragedy soon.",
         #        "Death awaits you, be careful around snails.",
          #       "You will find great wealth.",
          #       "DAMN, y- y- you- you should go see a therapist.",
          #        ]
         #   print("Your fortune cookie says: ")
         #   time.sleep(2)
          #  print(random.choice(f))

       # elif op == 2:
         #   t = [ "The Fool: New beginnings, optimism, trust in life.",
           #       "The Magician: Action, the power to manifest.",
           #       "The High Priestess: Inaction, going within, the subconscious.",
            #      "The Empress: Abundance, nurturing, fertility, life in bloom!",
           #       "The Emperor: Structure, stability, rules and power.",
            #      "The Hierophant: Institutions, tradition, society and its rules.",
             #     "The Lovers: Sexuality, passion, choice, uniting.",
              #    "The Chariot: Movement, progress, integration.",
               #   "Strength: Courage, subtle power, integration of animal self.",
                #  "The Hermit: Meditation, solitude, consciousness.",
       #           "Wheel of Fortune: Cycles, change, ups and downs.",
        #          "Justice: Fairness, equality, balance.",
         #         "The Hanged Man: Surrender, new perspective, enlightenment.",
          #        "Death: The end of something, change, the impermeability of all things.",
           #       "Temperance: Balance, moderation, being sensible.",
#                  "The Devil: Destructive patterns, addiction, giving away your power.",
 #                 "The Tower: Collapse of stable structures, release, sudden insight.",
  #                "The Star: Hope, calm, a good omen!",
   #               "The Moon: Mystery, the subconscious, dreams.",
    #              "The Sun: Success, happiness, all will be well.",
     #             "Judgement: Rebirth, a new phase, inner calling.",
      #            "The World: Completion, wholeness, attainment, celebration of life." ]
       #     print("You draw a tarot card: ")
        #    time.sleep(1)
         #   print(random.choice(t))

     #   elif op == 3:
     #       b = [ "You will find clarity in unexpected places.",
#                  "A new opportunity will present itself soon.",
#                  "Trust your intuition; it will guide you well.",
 #                 "Challenges are ahead, but so are rewards.",
  #                "You will reconnect with an old friend.",
   #               "Patience will bring you great rewards.",
    #              "A surprise is waiting for you around the corner.",
     #             "You will discover a hidden talent.",
      #            "Your creativity will lead to success.",
       #           "You will find peace in nature." ]
        #    print("The crystal ball reveals: ")
         #   time.sleep(2)
          #  print(random.choice(b))

     #   elif op == 4:

 #           print("Who do you want to talk to?")
#            print("1. Talk to dead people")
  #          print("2. Talk to me")
   #         print("3. Talk to your future self")
    #        print("4. Talk to your past self")
     #       talk_op = int(input("Choose from options 1 - 4: "))

      #      if talk_op == 1:
       #         print("Ok, delving into the spirit world...")
        #        time.sleep(2)
         #       print("I have connected you with a variety of spirits.")
          #      print("1. Your great-grandfather")
           #     print("2. Abraham Lincoln")
            #    print("3. Your first pet")
             #   print("4. Tupac Amaru")
              #  print("5. Michael Jackson")
               # print("6. Random guy")
               # spirit_op = int(input("Choose from options 1 - 6: "))
               # print("Connecting...")
               # time.sleep(2)
                #if spirit_op == 1:
                 #   print("Hello grandchild, how have you been! Remember to always cherish family.")
                #elif spirit_op == 2:
   #                 print("Who are you?")
    #            elif spirit_op == 3:
     #               print("*Random animal noises* (seems excited)")
      #          elif spirit_op == 4:
       #             print("Love tradition, young one.")
        #        elif spirit_op == 5:
         #           print("Hee Hee!")
          #      elif spirit_op == 6:
           #         print("Sup")
            #    else:
             #       print("1 - 6 only, please.")
              #  print("The connection has been lost.")
#            elif talk_op == 2:
 #               print("That's nice of you")
  #              time.sleep(1)
   #             name = input("What's your name? ")
    #            print("Nice to meet you", name)
     #           time.sleep(1)
      #          input("What would you like to talk about?")
       #         print("OH? well I think we should talk about anime, do you like it?")
        #        ans = input("(yes/no) ").strip().lower()
         #       if ans == 'yes':
          #          print("Hel yeah, me too")
           #         time.sleep(1)
            #        print("Whats your favorite one?")
             #       fav = input().strip()
              #      print("Oh, I like", fav, "too, but the ending felt forced.")
    #
     #           else:
      #              print("O dang, you're missing out")
       #         input("How are you feeling today? ")
        #        print("That's great to hear.")
         #       time.sleep(5)
          #      print("It was nice talking to you", name)
#                time.sleep(5)
#                print("Goodbye!")

#            elif talk_op == 3:
#                print("Connecting to your future self...")
#                time.sleep(2)
#                print("INVEST IN BITCOIN NOW!")
#                time.sleep(1)
#                print("Connection lost.")
#
#            elif talk_op == 4:
  #              print("Connecting to your past self...")
     #           time.sleep(2)
 #               print("Did we marry him?")
    #            time.sleep(2)
    #            print("What do you MEAN 'who'?")
  #              time.sleep(2)
     #           print("Hiccup!")
    #            time.sleep(2)
  #              print("I love Hiccup, he's so cuuute and smaaaaart, and handsoooooooooooooome, and braaaaaaaaaaaaaaaaaaave, and funnyyyyyyyyyyyyyyy")
  #              time.sleep(2)
 #               print("Have I told you about Hic-")
 #               print("Connection lost.")

 #           else:
 #               print("1 - 4 only, please.")
 #       else:
 #           print("1 - 4 only, please.")
    
    

 #   lel = input("Do you want another round?")

  #  if lel == "yes":
  #      print("OK!")
  #  else:
    #    print("Thanks for coming!")
   #     break




#6 OUTFIT INSPO

#import random
#import time

#print("Welcome to The Outfit Designer!")

#while True:
   # print("\nChoose a character style:")
   # time.sleep(1)
   # print("1. Masculine")
   # print("2. Feminine")
   # print("3. Androgynous / Mixed Style")
    
   # o = input("Select an option (1-3): ")
    
  #  if o not in ["1", "2", "3"]:
    #    print("Invalid option. Try again.")
     #   continue

   # print("\nNice choice!")
   # top = input("Favorite top: ")
   # bottom = input("Favorite bottom: ")
  #  shoes = input("Favorite shoes: ")
  #  accessory = input("Accessory: ")
   # headwear = input("Headwear: ")
    
  #  print("\nDesigning your outfit...")
  #  time.sleep(2)

  #  print("\n✨ Your Outfit ✨")
   # print(f"{headwear}, {top}, {bottom}, {shoes}, {accessory}")
    
   # print("\nRunway review:")
   # reviews = [
   #     "Serving elegance.",
    #    "Giving main character energy.",
    #    "Honestly iconic.",
    #    "Fit goes hard.",
   #     "Pinterest boards wish they were you."
   # ]
   # print(random.choice(reviews))

   # r = input("\nDo you want to design another outfit? (yes/no): ")
  #  if r.lower() != "yes":
   #     print("\nThanks for playing! See you next runway!")
      #  break




#7 SHEEEEEEEEEEEEEEEEEEEEP


#import random
#import time

#print("Welcome to the sheep game!!!!")
#time.sleep(1)
#print("1.- Start Game")
#time.sleep(0.5)
#print("2.- Exit")

#option = int(input("Select an option: "))

#if option == 2:
 #   print("Exiting...")
    
#elif option == 1:
    
    #print("Starting Game...")
    #time.sleep(3)
    #print("SHEEEEEEEEEEEEEEEEEEEEEEEEEEEEPP")
    #time.sleep(2)
    #print("-------CHAPTER 1-------")
    #time.sleep(1)
    #print("On a random tuesday, while counting his 100 sheep, a farmer noticed that the water was infected with a potion of flotation.")
    #time.sleep(3)
    #print("Suddenly, some of his sheep started to float away into the sky.")
    #time.sleep(3)
    #f = ( random.randint(1,100) )
    #while True:
        #guess = int(input("How many are left?: "))
        #print("If you guess right, you continue, if not, try again")
       # while guess != f:
            #if guess < f:
           #     print("Too low, try again")
           #     guess = int(input("There were 100 sheeps and some flew away, how many are left?: "))
          #  elif guess > f:
        #        print("Too high, try again")
       #         guess = int(input("There were 100 sheep and some flew away, how many are left?: "))
        
     #   print("Congratulations, you guessed right! There are", f, "sheep left!")
      #  break
#time.sleep(2)
#print("Next chapter loading...")
#time.sleep(4)
#print("-------CHAPTER 2-------")
#time.sleep(1)
#print("While pastoring his ", f, "sheep, the farmer saw a wolf approaching his herd.")
#time.sleep(2)
#print("He tries to defend them by throwing stones at it.")
#time.sleep(2)
#s = int(input("How many stones does he throw at the wolf?: "))
#print("The farmer threw", s, "stones at the wolf.")
#time.sleep(2)
#print("Of those stones, only", s - ( random.randint(1,s) ), "hit the wolf, and the wolf ran away scared.")

#e = input("Do you want to continue to the next chapter? yes or no: ")
#if e.lower() == "yes":
 #   print("Loading chapter 3...")
 #   time.sleep(4)
 #   print("-------CHAPTER 3-------")
 #   time.sleep(1)
 #   print("After scaring away the wolf, the farmer continued to pasture his sheep.")
 #   time.sleep(2)
 #   print("While walking toward the forest, he stumbled upon a river.")
 #   time.sleep(2)
 #   print("What does he do?")
  #  time.sleep(1)
  #  print("1.- Cross the river")
  #  print("2.- Follow the river")
  #  print("3.- Go back home")
  #  choice = int(input("Select an option: "))
  #  if choice == 1:
   #     print("He crossed the river safely and continued pasturing your sheep.")
  #      time.sleep(2)
  #  elif choice == 2:
 #       print("He followed the river and fell.")
  #      time.sleep(2)
   #     print("He drowned ")
   #     time.sleep(1)
   #     print("His sheep were freed and felt overjoyed and lived happily ever after.")
   #     time.sleep(2)
  #  elif choice == 3:
   #     print("He went back home with his sheep and died cause a sheep hit him from the sky..")
   #     time.sleep(2)
   # else:
   #     print("Invalid option, the farmer decides to go back home and dies cause a sheep hit him from the sky.")
  #      time.sleep(2)
  #  print("Thank you for playing the sheep game!")
#else:
 #   print("Thank you for playing the sheep game!")




#8 MULT GAME

  
 # import random
#print("Welcome to the mult-game!")
#print("In this game, you will enter a number between 1 - 10.")  
#print("If the number is less than 1 or greater than 10, the program will output the square, cube, fourth power, fifth power, sixth power, seventh power, eighth power, ninth power, and tenth power of that number.")
#while True:

   # print("-------START-------")
  #  n = int(input("Select a number between 1 - 10"))

   # if n > 1 or n < 10:
    #    print( n * n, n*n*n, n*n*n*n, n*n*n*n*n, n*n*n*n*n*n, n*n*n*n*n*n*n, n*n*n*n*n*n*n*n, n*n*n*n*n*n*n*n*n, n*n*n*n*n*n*n*n*n*n)

      #  o = input(" Try again? yes or no: ")
      #  if o.lower() == "yes":
     #       continue
     #   else:
     #       print("Thank you for playing the mult-game!")
     #       break
  #  else:
    #    print("Incorrect output, re-enter the number")
      #  break





#9 BALLON POP

#import random
#import time

#def balloon_pop():
   # print("Welcome to Balloon Pop!")
   # print("The balloon grows bigger each turn...")
  #  print("Pop it before it gets too big and bursts!\n")

  #  balloon_size = 0
  #  max_size = random.randint(8, 15)  # random burst point
   # score = 0

   # while True:
     #   action = input("Press Enter to pump the balloon, or type 'pop' to pop it: ").lower()

     #   if action == "pop":
      #      print(f"You popped the balloon at size {balloon_size}!")
       #     score += balloon_size
      #      print(f"Your score: {score}")
      #      # Start a new balloon
       #     balloon_size = 0
       #     max_size = random.randint(8, 15)
        #    continue

   
    #    balloon_size += random.randint(1, 3)
    #    print(f"Balloon size: {balloon_size}")

    
   #     if balloon_size >= max_size:
    #        print("Oh no! The balloon burst!")
   #         print(f"Final Score: {score}")
    #        break


#balloon_pop()




#10 STORY ADVENTURE

#def story_adventure():
    #print("Welcome to The Mystery of the Forgotten Temple!")
    #print("You are an explorer who has discovered an ancient ruin in the jungle.")
    #print("Your choices will decide your fate...\n")

    #def ending(text):
      #  print("\n" + text)
     #   print("🏁 The End.")
    #    return

   # choice1 = input("You stand before two doors inside the temple. One is red, the other blue.\nWhich door do you choose? (red/blue): ").lower()

  #  if choice1 == "red":
 #       print("\nYou push the heavy red door open. A torch-lit hallway stretches ahead...")
#        choice2 = input("You see a strange statue holding a glowing gem. Do you (take) the gem or (ignore) it? ").lower()

    #    if choice2 == "take":
   #         print("\nThe gem radiates warmth as you lift it from the statue’s hands...")
  #          choice3 = input("Suddenly, the floor shakes! Do you (run) forward or (run back)? ").lower()
 #           if choice3 == "run":
#                ending("You dash ahead and escape into a treasure chamber filled with gold! You live a life of fortune.")
          #  else:
         #       ending("The hallway collapses behind you. You are trapped forever in darkness...")
        #else:
          #  print("\nYou decide not to touch the gem. The statue’s eyes glow, and the hallway leads you deeper.")
         #   choice3 = input("At the end, you find a fork: (left) leads to chanting, (right) smells of fresh air. Which way? ").lower()
        #    if choice3 == "left":
       #         ending("You find a secret cult performing rituals. They welcome you as their chosen one. You never leave...")
      #      else:
     #           ending("You emerge safely outside the temple, richer in wisdom but without treasure.")
    
    #elif choice1 == "blue":
        #print("\nhe blue door creaks open, revealing a cold, misty chamber.")
        #choice2 = input("In the center lies a frozen pedestal with a book. Do you (read) the book or (leave) it? ").lower()

        #if choice2 == "read":
          #  print(f"\nThe book glows as you flip it open, whispering secrets of time.")
         #   choice3 = input("Do you (accept) the power it offers, or (reject) it? ").lower()
        #    if choice3 == "accept":
       #         ending("You gain control of time itself! You become a legend... but vanish from the world forever.")
       #     else:
       #         ending("You close the book respectfully. A hidden door opens, leading you safely out. You live, wiser and humbler.")
       # else:
       #     print("\nYou ignore the book and move forward. Suddenly, you hear growling...")
      #      choice3 = input("A shadowy beast blocks your path! Do you (fight) it or (flee)? ").lower()
      #      if choice3 == "fight":
      #          ending("With bravery, you fight the beast... but it overpowers you. The temple claims another victim.")
      #      else:
      #          ending("You sprint away and find a hidden passage that leads to freedom. You survive, but the mystery remains unsolved.")
    
  #  else:
  #      ending("You hesitate too long. The temple collapses, burying its secrets forever... and you with it.")


#story_adventure()




#11 DICE RACE


#import random
#import time

#def race_game():
  #  print("🏁 Welcome to the Dice Race Game!")
 #   print("You and the computer will race to the finish line.\n")

    #finish_line = 30  # distance to win
   # player_pos = 0
  #  computer_pos = 0

 #   while player_pos < finish_line and computer_pos < finish_line:
#        input("Press Enter to roll the dice...")

    
        #player_roll = random.randint(1, 6)
        #player_pos += player_roll
        #print(f"You rolled {player_roll}! You are now at position {player_pos}.")

 
        #time.sleep(1)
        #computer_roll = random.randint(1, 6)
        #computer_pos += computer_roll
        #print(f"Computer rolled {computer_roll}! Computer is now at position {computer_pos}.")

 
        #track = ["-"] * finish_line
        #if player_pos < finish_line:
         #   track[player_pos-1] = "P"
        #else:
         #   track[-1] = "P"
        #if computer_pos < finish_line:
        #    track[computer_pos-1] = "C"
       # else:
      #      track[-1] = "C"
     #   print("".join(track))

    #    print("-" * 40)
   #     time.sleep(1)

  #  if player_pos >= finish_line and computer_pos >= finish_line:
 #       print("It's a tie!")
    #elif player_pos >= finish_line:
   #     print("You win!")
  #  else:
 #       print("Computer wins!")

#race_game()




#12 TRIVIAAAAA

#def trivia_game():
  #  print("Welcome to TRIVIAAAA")
  #  print("Answer the questions by typing A, B, C, or D.\n")


   # questions = [
       # {
           # "question": "What is the capital of France?",
          #  "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
         #   "answer": "C"
        #},
        #{
           # "question": "Which planet is known as the Red Planet?",
          #  "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
         #   "answer": "B"
        #},
        #{
           # "question": "Who wrote 'Romeo and Juliet'?",
          #  "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) J.K. Rowling"],
         #   "answer": "B"
        #},
        #{
        #    "question": "What is 7 × 8?",
       #     "options": ["A) 54", "B) 56", "C) 64", "D) 72"],
      #      "answer": "B"
     #   }
    #]

    #score = 0


   # for i, q in enumerate(questions, start=1):
  #      print(f"\nQ{i}: {q['question']}")
 #       for option in q["options"]:
#            print(option)

       # answer = input("Your answer: ").upper()
      #  if answer == q["answer"]:
     #       print("Correct!")
    #        score += 1
   #     else:
  #          print(f"Wrong! The correct answer was {q['answer']}.")

 #   print(f"\nGame Over! Your final score: {score}/{len(questions)}")


#trivia_game()





#13 TREASURE HUNT

#import random

#def treasure_hunt():
 #   print("💎 Welcome to Treasure Hunt!")
 #   print("Find the hidden treasure on a 5x5 grid.")
 #   print("Enter guesses as row and column numbers (1–5).")

  
    #treasure_row = random.randint(1, 5)
    #treasure_col = random.randint(1, 5)

    #attempts = 0

    #while True:
    #    try:
   #         row = int(input("Enter row (1–5): "))
  #          col = int(input("Enter column (1–5): "))
 #           attempts += 1
#
   #         if not (1 <= row <= 5 and 1 <= col <= 5):
  #              print("Coordinates must be between 1 and 5.")
 #               continue
#
  #          if row == treasure_row and col == treasure_col:
 #               print(f"You found the treasure in {attempts} attempts!")
#                break

        
    #        distance = abs(row - treasure_row) + abs(col - treasure_col)
    #        if distance == 1:
    #            print("Very close!")
    #        elif distance <= 2:
     #           print("Close!")
   #         else:
   #             print("Far away!")
   #     except ValueError:
  #          print("Please enter valid numbers.")

#treasure_hunt()




#14 SIMON SAYSS

#import random
#import time

#def simon_says():
  #  print("Welcome to Simon Says (Memory Sequence)!")
  #  print("Repeat the sequence of colors. Each round adds one more.\n")
  #  colors = ["Red", "Blue", "Green", "Yellow"]
  #  sequence = []
  #  round_num = 1

   # while True:
      #  print(f"\n--- Round {round_num} ---")
        
       # sequence.append(random.choice(colors))

     
      #  print("Watch carefully!")
      #  for color in sequence:
       #     print(color)
       #     time.sleep(0.8)  # pause so player can memorize
      #  time.sleep(0.5)
      #  print("\n" * 20)  # clear screen (fake)

   
     #   print("Now it’s your turn! Enter the sequence:")
     #   for i, color in enumerate(sequence, start=1):
      #      guess = input(f"Color {i}: ").capitalize()
      #      if guess != color:
       #         print(f"Wrong! The correct sequence was: {sequence}")
       #         print(f"You reached Round {round_num}!")
         #       return
     #   print("Correct!")
   #     round_num += 1


#simon_says()




#15 MEMORY (pairs)

#import random

#def memory_game():
  #  print("Welcome to the Memory Game (Pairs)!")
   # print("Match all the pairs to win.\n")


   # items = ["😀", "🐱", "🍎", "🚗", "⚽", "🎵"]
    #pairs = items * 2  # duplicate for pairs
    #random.shuffle(pairs)

  
   # board = ["❓"] * len(pairs)
   # revealed = [False] * len(pairs)
   # attempts = 0

    #def display_board():
    #    print("\nBoard:")
     #   for i, val in enumerate(board, 1):
       #     print(f"{i:2}:{val}", end="  ")
        #    if i % 4 == 0:
        #        print()
       # print()

 
   # while not all(revealed):
      #  display_board()
     #   try:
         #   choice1 = int(input("Pick the first card (1-12): ")) - 1
          #  choice2 = int(input("Pick the second card (1-12): ")) - 1

          #  if choice1 == choice2 or not (0 <= choice1 < len(pairs)) or not (0 <= choice2 < len(pairs)):
          #      print("Invalid choice. Try again.")
          #      continue
         #   if revealed[choice1] or revealed[choice2]:
           #     print("One of those cards is already matched.")
            #    continue

         #   board[choice1] = pairs[choice1]
          #  board[choice2] = pairs[choice2]
         #   display_board()
         #   attempts += 1

         #   if pairs[choice1] == pairs[choice2]:
         #       print("✅")
          #      revealed[choice1] = revealed[choice2] = True
         #   else:
         #       print("❌")
         #       board[choice1] = board[choice2] = "❓"

      #  except ValueError:
       #     print("Please enter valid numbers.")

   # print(f"You found all pairs in {attempts} attempts!")


#memory_game()




#16 MATH QUIZZ


#import random

#def math_quiz():
  #  print("Welcome to the Math Quiz Game!")
#    score = 0
 #   rounds = 5  # number of questions

 #   for i in range(1, rounds + 1):
       
   #     operation = random.choice(["+", "-", "*"])
     #   num1 = random.randint(1, 10)
    #    num2 = random.randint(1, 10)

       
     #   if operation == "-" and num1 < num2:
       #     num1, num2 = num2, num1

        
     #   if operation == "+":
      #      correct_answer = num1 + num2
      #  elif operation == "-":
      #      correct_answer = num1 - num2
       # else:
       #     correct_answer = num1 * num2

     
     #   print(f"\nQuestion {i}: What is {num1} {operation} {num2}?")
      #  try:
        #    player_answer = int(input("Your answer: "))
        #    if player_answer == correct_answer:
        #        print("CORRECT!")
         #       score += 1
        #    else:
        #        print(f"Wrong! The correct answer was {correct_answer}.")
      #  except ValueError:
       #     print("Invalid input. That counts as a wrong answer.")

   # print(f"\nGame Over! Your final score: {score}/{rounds}")


#math_quiz()




#17 GUESS THE WORD

#import random

#def guess_the_word():
  #  print("Welcome to Guess the Word (Hangman Lite)!")

    
  #  words = ["python", "computer", "game", "hangman", "programming", "challenge"]
  #  word = random.choice(words)  # Pick a random word
    #guessed = set()
    #attempts = 6  # Wrong guesses allowed

  
  #  while attempts > 0:
  #      display = "".join([letter if letter in guessed else "_" for letter in word])
  #      print("\nWord:", " ".join(display))
   #     print(f"Wrong guesses left: {attempts}")
#        print(f"Letters guessed: {' '.join(sorted(guessed)) if guessed else 'None'}")

    #    guess = input("Guess a letter: ").lower()

  #      if not guess.isalpha() or len(guess) != 1:
   #         print("Please enter a single letter.")
    #        continue
    #    if guess in guessed:
     #       print("You already guessed that letter.")
        #    continue

      #  guessed.add(guess)

       # if guess in word:
        #    print("Good guess!")
        #    if all(letter in guessed for letter in word):
        #        print(f"\nYou win! The word was: {word}")
           #     break
   #     else:
         #   print("Wrong guess.")
         #   attempts -= 1
  #  else:
       # print(f"\nGame Over! The word was: {word}")


#guess_the_word()



#18 ROC-PAPER-SCISSORS

#import random

#def rock_paper_scissors():
  #  print("Welcome to Rock, Paper, Scissors!")
 #   choices = ["rock", "paper", "scissors"]

   # while True:
       # player = input("Choose Rock, Paper, or Scissors (or 'quit' to stop): ").lower()
        
       # if player == "quit":
          #  print("Thanks for playing!")
          #  break
       # if player not in choices:
          #  print("Invalid choice. Try again.")
           # continue

       # computer = random.choice(choices)
       # print(f"Computer chose: {computer.capitalize()}")

      #  if player == computer:
           # print("It's a tie!")
      #  elif (player == "rock" and computer == "scissors") or \
            # (player == "scissors" and computer == "paper") or \
          #   (player == "paper" and computer == "rock"):
         #   print("YOU WINNN!")
       # else:
         #   print("YOU LOSEEEEEEEEEE !")


#rock_paper_scissors()




#19 TIC-TAC-TOE

#import random

#def print_board(board):
   # print("\n")
   # for row in board:
   #     print(" | ".join(row))
   #     print("-" * 5)
   # print("\n")

#def check_winner(board, player):
    
#    for i in range(3):
      #  if all([cell == player for cell in board[i]]):  # row
      #      return True
     #   if all([board[j][i] == player for j in range(3)]):  # column
           # return True
  #  if all([board[i][i] == player for i in range(3)]):  # main diagonal
      #  return True
  #  if all([board[i][2-i] == player for i in range(3)]):  # anti-diagonal
    #    return True
   # return False

#def is_full(board):
    #return all(cell != " " for row in board for cell in row)

#def player_move(board, player):
  #  while True:
       # try:
            #move = int(input(f"Player {player}, enter your move (1-9): "))
            #row, col = divmod(move - 1, 3)
           # if board[row][col] == " ":
               #board[row][col] = player
                #break
           # else:
                #print("Spot already taken, choose another.")
       # except (ValueError, IndexError):
            #print("Please enter a number between 1 and 9.")

#def computer_move(board, player):
    #print("Computer is making a move...")
    #empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
   # move = random.choice(empty_cells)
   # board[move[0]][move[1]] = player

#def tic_tac_toe():
    #print("Welcome to Tic Tac Toe!")
   # mode = input("Choose mode: (1) Player vs Player, (2) Player vs Computer: ")

   # board = [[" " for _ in range(3)] for _ in range(3)]
   # current_player = "X"

   # print_board(board)

   # while True:
       # if mode == "1" or (mode == "2" and current_player == "X"):
            #player_move(board, current_player)
       # else:
            #computer_move(board, current_player)

        #print_board(board)

       # if check_winner(board, current_player):
            #print(f"Player {current_player} wins!")
            #break
        #elif is_full(board):
            #print("It's a draw!")
            #break

       # current_player = "O" if current_player == "X" else "X"


#tic_tac_toe()



#20 HIDE AND SEEK WITH NUMBERS

#import random

#def hide_and_seek():
   # print("Welcome to Hide and Seek (Digital Version)!")
   # print("I am hiding a number between 1 and 20... Can you find it?")
    
    
    #hidden_number = random.randint(1, 20)
   # attempts = 0
    
    #while True:
        #try:
           # guess = int(input("Enter your guess (1-20): "))
            #attempts += 1

            #if guess < 1 or guess > 20:
               # print("Please choose a number between 1 and 20.")
           # elif guess < hidden_number:
               #print("Too low! Try again.")
            #elif guess > hidden_number:
               #print("Too high! Try again.")
            #else:
                #print(f"You found it! The number was {hidden_number}.")
                #print(f"It took you {attempts} attempts.")
                #break
        #except ValueError:
            #print("Please enter a valid number.")




#hide_and_seek()
