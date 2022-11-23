print(repeat_lyrics())

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#this will be revealed by python to be an error because the function is called
#before it is defined
