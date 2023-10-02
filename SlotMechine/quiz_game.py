print("Welcome! to My quiz game ")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()
print ("Okey! Lets Play")

score = 0

answer = input("What does CPU stand for? Or Full form of CPU: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else :
    print("Wrong!")

answer = input("What does GPU stand for? Or Full form of GPU: ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else :
    print("Wrong!")

answer = input("What does RAM stand for? Or Full form of RAM: ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else :
    print("Wrong!")

answer = input("What does PSU stand for? Or Full form of PSU: ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else :
    print("Wrong!")

print ("You got " + str(score) + " question correct!")
print ("You got " + str((score)/4 * 100) + "%.")