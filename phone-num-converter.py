#There's a bunch of different ways to implement this program and make it working and functional, I was just curious what was the minimal number of lines I could do it in. 
phone_number = input("Enter a phone number to be translated:")#asks for input from the user
phone_num_in = "abcdefghijklmnopqrstuvwxyz" #character mapping for maketrans
phone_num_out = "22233344455566677778889999" #letters to numbers in the character mapping
phone_trans = str.maketrans(phone_num_in, phone_num_out) #takes the inputed information and translates it using maketrans
print (phone_number.lower().translate(phone_trans)) #outputs the translation
#Without the comments, it's five lines
#I'm hoping to have some fun with the beat the zombies game, that's why I did this one first, so I could spend more time on that one. 