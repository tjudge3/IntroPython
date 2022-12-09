#This assignment was to create a class schedule.
course = input('Enter a class name:').upper() #Asks for class name input, also converts all inputs to uppercase
courses_num_class = {'CS101': 'CS101', 'CS102' : 'CS102', 'CS103' : 'CS103', 'NT110' : 'NT110', 'CM241' : 'CM241'} #creates the first relationships between keyval-pairs - class name
courses_num_rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411} #creates the second relationships between keyval-pairs - room numbers
courses_num_instructs = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'} #creates the third relationship between keyval-pairs - instructors
courses_num_times = {'CS101':'8:00am','CS102':'9:00am','CS103':'10:00am','NT110':'11:00am','CM241':'1:00pm'}#creates the fourth relationship between keyval-pairs - times
#output from class number entered
if course in courses_num_rooms:
    print('Class:', courses_num_class[course])
    #outputs class based on course - keyval->value
    print('Room:', courses_num_rooms[course]) #outputs room based on course - keyval->value
    print('Instructor:', courses_num_instructs[course]) #outputs instructor based on course - keyval->value
    print('Time:', courses_num_times[course]) #outputs time based on course - keyval->value
else:
    print('Invalid class number.')
