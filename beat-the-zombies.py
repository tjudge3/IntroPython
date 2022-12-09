#This assignment was to create a basic text based game. 
#Originally when I did this, the game did in fact have global thermal nuclear war but I felt that was a bit glib given the current state of the world, so I just re-did everything and made it simpler
def play_again(): #it's easiest just to have a function to play again
  play_again=input("\n Would you like to play again? Y/N ").upper()#here we ask if they'd like to play again and change it to an upper
  if play_again=='Y':#if they select the "yes" option then we start again
        main()
  else:#if they do not choose the "yes" option then we thank them for playing and quit the program
       print("Thanks for Playing!")
       quit()     
def main():
  print('{:^84s}'.format("Cemetery Madness\n\n"))#Name of the game formatted to align center(ish)
  print("You wake up in a cemetry, it is pitch black and the wind is whipping between the tomb stones.\n\n Off in the distance you begin to hear a rustling and scraping on the ground. \n\n A low and gutteral echo is slowly getting closer and closer to you. \n\n As you stand up tall, you see a horde of zombies approaching your position.\n\n")#Here we have the intro with the line breaks
  print("\n What action do you take?\n")#We ask what actions they wish to take
  print('1: Climb into a nearby grave')#Option A
  print('2: Look around on the ground')#Option B 
  print('3: Climb a near by tree')#Option C
  print('4: Scream in terror')#Option D
  while True :#Here we use Try/Except for input validation the first time
    try:
        opening=int(input("\nEnter 1, 2, 3 or 4 that corresponds to the action you wish to take: "))#We ask user to select option, if it validates as an int then we pass opening down to the if statement 
    except ValueError:
        print("That's not an integer")#If they type a non integer it tells them and they have to try again
        print()  
    else:
      break
  if opening==1:#If the input validates above we get to here and have options for next step, if the number one is the option they move on, otherwise they die
    print("\n Climbing into the nearby grave was the right move!\n")#Message
    print("\n The Zombies pass right overhead")#Message
    print("\n What action do you take now?\n")#Here we ask what action for the middle part they wish to take
    print('1: Lay very still')#Option A
    print('2: Get out of the grave and run to a tree')#Option B 
    print('3: Cover yourself in dirt')#Option C
    while True :#Here we use Try/Except for input validation the second time
      try:
        middle=int(input("\nEnter 1, 2 or 3 that corresponds to the action you wish to take: "))#We ask user to select option, if it validates as an int then we pass middle down to the if statement 
      except ValueError:
        print("That's not an integer")#If they type a non integer it tells them and they have to try again
        print()  
      else:
        break
    if middle==3: #This is the correct option and we tell our user as such. They survived.
      print("\n Covering yourself in dirt was the right move!\n")#Message
      print("\n When it comes to zombie, you have learned that the only winning move is not to play\n")#Message
      play_again()#The play again function
    else:
      print("\n **Sad Trombone**.")#Message
      print("\n You ended up being eaten by zombie.")#Message
      print("\n **You ended up being eaten by zombie**.")#Message
      play_again()#The play again function
  else: #any other choices they made in the opening is the wrong move and we kill them off, letting them know as such
      print("\n **Sad Trombone**.")#Message
      print("\n You ended up being eaten by zombie.")#Message
      print("\n **You ended up being eaten by zombie**.")#Message
      play_again()#The play again function
main()
