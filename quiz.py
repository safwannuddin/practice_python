print(" Welcome to my Quiz Game!  😊")
score = 0
playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time! Goodbye! 👋")
    quit()

print("Great! Let's get started playing! 🎉")

answer = input(" What does the CPU stands for ?")

if answer.lower() == "central processing unit" :
    print("Correct!  U are Right 🎉")
    score += 1
else:
    print("Incorrect! The correct answer is 'Central Processing Unit' . 😔")

answer = input("What does the GPU stands for ? ")

if answer.lower() == "graphics processing unit":
    print("Correct! U are Right 🎉")
    score += 1
else:
    print("Incorrect! The correct answer is 'Graphics Processing Unit'. 😔")

answer = input("What does the RAM stands for ? ")

if answer.lower() == "random access memory":
    print("Correct! U are Right 🎉")
    score += 1
else:
    print("Incorrect! The correct answer is 'Random Access Memory'. 😔")

answer = input("What does the PSU stands for ? ")

if answer.lower() == "power supply unit":
    print("Correct! U are Right 🎉")
    score += 1
else:
    print("Incorrect! The correct answer is 'Power Supply Unit'. 😔")

answer = input("What does the ROM stands for ? ")

if answer.lower() == "read only memory":
    print("Correct! U are Right 🎉")
    score += 1
else:
    print("Incorrect! The correct answer is 'Read Only Memory'. 😔")
print("Your Score is " + str(score) + " out of 5. 🏆")