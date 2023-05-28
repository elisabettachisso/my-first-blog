print('Hello Django girls!')
name = 'Elisabetta'
if name == 'Chiara':
    print('Hey Chiara!')
elif name == 'Elisabetta':
    print('Hey Elisabetta!')
else :
    print('Hey anonymus!')
volume = 58
if volume < 20 :
    print("It's kinda quiet")
elif 20 <= volume < 40 :
    print("Background Music")
elif 40 <= volume < 60 :
    print("Perfect")
elif 60 <= volume < 80 :
    print("Nice for parties")
elif 80 <= volume < 100 :
    print("A bit loud")
else : 
    print("My ears are hutring")
# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
def hi() :
    print("Hey there!")
    print("How are you?")

hi()
def hi(name) :
    print('Hi ' + name + '!')

hi("Gianna")
