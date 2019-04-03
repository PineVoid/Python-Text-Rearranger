# A code word scrambler, made by Jacob Gray. My first real Python project, so don't expect it to be too good! Finished on 8/31/18. In total, I worked on it over the course of about 5 days. Took about 6 to 8 hours total.

while 1 > 0:
    baseText=input(str("Insert mix-matched text here."))
    numberSkip= int(input("Insert the amount of characters skipped here."))
    baseTextLength= int(len(baseText))
    characterNumber= 0
    offset = 0

    translatedText= list(None for x in range(int(baseTextLength)))

    while characterNumber/baseTextLength != 1:	#as long as you're not at the last character
        if characterNumber % (baseTextLength / numberSkip) == 0:    # calculate whether the offset has to be bumped up
            offset = characterNumber / (baseTextLength/ numberSkip) # calculate the offset
        translatedText[int(characterNumber)] = baseText[int(((characterNumber + 1) * numberSkip - 1 + offset) % baseTextLength)]	#figures and matches up the old spot to the new one
        characterNumber = characterNumber + 1
    print("Your new text is " + "".join(translatedText))    # joins the list of characters that have been reassigned
    print("")
    input("Hit enter to input another number.")	
    print("")