print('---------------You wanna play this game--------------')
player =input('if you wanna play then enter y if you dont enter x :')

if player.lower() != "y":
    quit()

print("okay lets play :) ")
score=0
question=input('what is the full form of cpu? : ')
if question.lower()=="central processing unit":
     print('correct')
     score=score+1
else:
     print('incorrect')

question=input('what is the full form of LCD? : ')
if question.lower()=="liquid crystal display":
     print('correct')
     score=score+1
else:
     print('incorrect')


question=input('what is the full form of ALU? : ')
if question.lower()=="arithmetic logic unit":
     print('correct')
     score+=1
else:
     print('incorrect')

question=input('what is the full form of ATM? : ')
if question.lower()=="automated teller machine":
     print('correct')
     score+=1
else:
     print('incorrect')

question=input('what is the full form of GUI? : ')
if question.lower()=="graphical user interface":
     print('correct')
     score+=1
else:
     print('incorrect')

question=input('what is the full form of API? : ')
if question.lower()=="application programming interface":
     print('correct')
     score+=1
else:
     print('incorrect')   
print('your score', score)
if score<=2:
     print("good :|")
elif score<=4:
     print("very Good")
elif score<=6:
     print('outstanding')     
print("-----------x-------GAME OVER-------x-------------")