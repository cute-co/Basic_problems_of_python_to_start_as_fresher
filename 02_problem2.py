#In this we are going to replace name and date with actually name name and date 
letter = '''Dear <|name|>,
            you are selected!
            <|date|>'''
print(letter.replace(" <|name|>"," Harshita ").replace("<|date|>","07 Jan 2002"))            