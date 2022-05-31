letter = ''' Dear, <|NAME|>
you are selected!
Date = <|DATE|> '''
name = input("Enter the name\n")
date = input("Enter the date\n")
letter = (letter.replace("<|NAME|>" , name))
letter = (letter.replace("<|DATE|>" , date))
print(letter)

