# write a loop that will ask the user for their favorite thing (programming language, professor, snack, color, number, month, your choice).  It should continually ask for their favorite thing until it matches a predefined value. When there is a match, congratulate the user.
#2022-02-19  
while True:
	game=input("What is your favorite game?: ") #asks for user input
	if game=="Global Thermal Nuclear War": #defines the game that will break the loop
		print("That's Right!") #message if they enter a correct 'game'
		break #breaks out of loop if correct
	print("That is incorrect, please try again") #if incorrect tells them they are and begins again


