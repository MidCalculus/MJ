"""
Name = input("What is your name")
print("My name is ", Name)
while True:
    Answer = input("It is?")
    print(Answer)

    if Answer == "Yes":
        print("Ok!")
        break
    else: 
        print("What is it then? :/")
        pass
"""

#f = open("test_file.txt", 'r')
#reading =  f.readline()

a = open("sussy_baka_text_messages.txt", 'a')

message = input()
a.write(message)


g