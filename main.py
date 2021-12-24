print('---------------You wanna play this game--------------')
player =input('if you wanna play then enter y if you dont enter x :')

if player.lower() != "y":
    quit()

print("okay lets play :) ")

question=input('what is the full form of cpu? : ')
if question.lower()=="central processing unit":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of LCD? : ')
if question.lower()==" liquid crystal display":
     print('correct')
else:
     print('incorrect')


question=input('what is the full form of ALU? : ')
if question.lower()=="arithmetic logic unit":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of ATM? : ')
if question.lower()=="automated teller machine":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of GUI? : ')
if question.lower()=="graphical user interface":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of API? : ')
if question.lower()=="application programming interface":
     print('correct')
else:
     print('incorrect')

print("-----------x-------YOU WIN--------x-------------")