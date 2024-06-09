# QUIZ GAME , like MCQS and give the score accordingly to it.

print("welcome to my computer quiz!!")

playing = input("do you want to play?? ")

if playing.lowerll != "yes":
    quit()
    
print("let's start playing shivesh")
score = 0

answer = input("who's gonna be prime minister of india?? ")
if answer == "Narendra Modi":
    print('correct!!')
    score +=1
else:
    (print('incorrect'))
    
answer = input("who's gonna be prime minister of india?? ")
if answer == "Narendra Modi":
    print('correct!!')
    score +=1
else:
    (print('incorrect'))
    
answer = input("who's gonna be prime minister of india?? ")
if answer == "Narendra Modi":
    print('correct!!')
    score +=1
else:
    (print('incorrect'))

print("you have got" + str(score) + "questions correct!!")
