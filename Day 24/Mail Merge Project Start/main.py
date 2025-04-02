#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
letter = open("Input/Letters/starting_letter.txt").read()
for name in open("Input/Names/invited_names.txt").readlines():

    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
    letter_with_name = letter.replace("[name]", name.strip())
    destination_file = open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w")
    destination_file.write(letter_with_name)


