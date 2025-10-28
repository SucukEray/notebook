notes = []
keepGoing = True
organizedNotes = ''

#Keep going until user says otherwise
while keepGoing == True:
    #Different first message
    if len(notes) == 0:
        getNote = str(input("\nEnter first note: "))
    
    #Main part
    else:
        #Ask for note and append note into list
        getNote = str(input("\nEnter note: "))
        notes.append(getNote)

        #Ask if user wants to keep adding notes
        keepGoing = input("Would you like to keep adding new notes?: ")
        
        #The rest is self explanatory
        if keepGoing == "yes":
            keepGoing = True 

        elif keepGoing == "no":
            keepGoing = False

        else:
            print("Please enter a proper reply (yes, no)")
            exit()

#Organize the notes into a string and print it out for the user
organizedNotes = ",\n      ".join(str(x) for x in notes)
print(f"""\nHere are your notes:

      {organizedNotes}""") 
# TODO: Make it so the user has the
# option to add more notes even after saying no
