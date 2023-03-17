#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

    with open("Input/Names/invited_names.txt") as name_file:
        names = name_file.readlines()
        for name in names:
            letter_now = letter_content.replace("[name]", name.strip())
            with open(f"Output/ReadyToSend/letter_to_{name.strip()}", mode='w') as letter_name:
                letter_name.write(letter_now)


