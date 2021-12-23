print('---------------You wanna play this game--------------')
player =input('if you wanna play then enter y if you dont enter x :')

if player != "y":
    quit()

print("okay lets play :) ")

question=input('what is the full form of cpu? : ')
if question=="central processing unit":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of LCD? : ')
if question==" liquid crystal display":
     print('correct')
else:
     print('incorrect')


question=input('what is the full form of ALU? : ')
if question=="arithmetic logic unit":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of ATM? : ')
if question=="automated teller machine":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of GUI? : ')
if question=="graphical user interface":
     print('correct')
else:
     print('incorrect')

question=input('what is the full form of API? : ')
if question=="application programming interface":
     print('correct')
else:
     print('incorrect')

print("-----------x-------YOU WIN--------x-------------")