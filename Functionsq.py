import random
import time
import Gfunctions as g


def Category_Selector(c):
    global flag
    category = ""
    flag = True

    if c == '1':
        category = "Questions/GK_Q.txt"
    if c == '2':
        category = "Questions/PopCulture_Q.txt"
    if c == '4':
        category = "Questions/Computer_Q.txt"
    if c == '3':
        category = "Questions/Math_Q.txt"
    if c == '5':
        category = "Questions/Science_Q.txt"

    with open(f"{category}", "r") as f:
        global qlist
        a = f.read()
        qlist = a.split('#')
        # print(qlist)


def Quiz_Master():
    random.shuffle(qlist)
    global t_score

    t_score = 0

    lives = 3
    count = 0
    liflcount = 0

    g._3lives()
    for i in qlist:
        # print(i)
        Q = i.split(':')
        qcount = str(count + 1)
        print('Q' + qcount)
        print(Q[0])
        print('\n')

        a = input("Enter the correct answer: ")
        print('='.center(69, '='))
        count += 1

        if a.lower() not in ['a', 'b', 'c', 'd', 'lifeline']:
            a = input("Invalid choice, please refer to the instructions and select a valid choice: ")

        if a.lower() == 'lifeline':
            if liflcount < 3:
                print("""You have 3 lifelines to assist you when you're stuck:

1)50:50: This lifeline will remove two incorrect answer options, increasing your chances of selecting the correct answer.

2)Audience Poll: Get the audience's opinion on the correct answer. This will help you make an informed choice.

3)Skip Question: you have the option to skip the current question without answering it

YOU CAN ONLY USE ONE LIFELINE PER QUESTION !!! """)
                liflcount += 1
                print('='.center(69, '='))
                lifechoice = int(input('Enter 1,2 or 3 corresponding to your choice: '))

                if lifechoice == 1:
                    optionlist = ['a', 'b', 'c', 'd']
                    optionlist.remove(Q[1])
                    random.shuffle(optionlist)
                    print(Q[0])
                    print('the incorrect options are', optionlist[1], optionlist[0])
                    a = input("Enter the correct answer: ")

                if lifechoice == 2:
                    optionlist = ['a', 'b', 'c', 'd']
                    optionlist.remove(Q[1])
                    aulist = []
                    aupoll = random.randint(0, 60)
                    aupoll2 = 60 - aupoll
                    aupoll3 = random.randint(0, aupoll2)
                    aupoll4 = aupoll2 - aupoll3
                    aupoll5 = random.randint(0, aupoll4)
                    m = 40 + aupoll4 - aupoll5
                    random.shuffle(optionlist)
                    aulist = ["Option:" + optionlist[0] + ' ' + str(aupoll),
                              "Option:" + optionlist[1] + ' ' + str(aupoll3),
                              "Option:" + optionlist[2] + ' ' + str(aupoll5), "Option:" + Q[1] + ' ' + str(m)]
                    random.shuffle(aulist)
                    print(Q[0])
                    print('\n')
                    print(aulist)
                    a = input("Enter the correct answer: ")
                    if a.lower() == 'lifeline':
                        print("Sorry you can't use two lifelines on one question. Your answer is considered incorrect")

                if lifechoice == 3:
                    print("Okay,Guess we're skipping this one")
                    print("We'll be back after a short ad break")
                    print("Dhe Poyi")
                    time.sleep(3)
                    print('Dha vannu')
                    continue

            else:
                print("""Nice try, you're out of lifelines""")
                print(Q[0])
                a = input("Enter the correct answer: ")

        if a.lower() == Q[1]:
            t_score += 1000
            print("Correct Answer!!!")
            print('='.center(69, '='))

        if a.lower() != Q[1]:
            lives = lives - 1
            t_score -= 500
            print(f"Oops! That was the wrong answer, You only have {lives} live(s) left")
            print('='.center(69, '='))

            if lives == 2:
                g._2lives()
            elif lives == 1:
                g._1lives()
            if lives == 0:
                g._0lives()
                time.sleep(1.5)
                break

        if count == 5:
            leave1 = input("Do you want to continue playing ? (yes/no) ")
            if leave1.lower() == 'no':
                break
            else:
                pass

        if count == 10:
            leave2 = input("Do you want to continue playing ? (yes/no) ")
            if leave2.lower() == 'no':
                break
            else:
                pass

        if count == 15:
            t_score += 5000
            break

    print("You've reached the end of the quiz, Congratulations")
    print(f"Your total points are {t_score}")
    print("Thank You for playing")
    print('='.center(69, '='))
    return t_score


def vq():
    ca = input(
        "Select the Category you want to view questions from: \n1.General Knowledge\n2.Pop "
        "Culture\n3.Mathematics\n4.Computer and Technology\n5.Science : ")
    print('='.center(69, '='))
    Category_Selector(ca)
    for i in qlist:
        print(i)


def aq():
    ca = input(
        "Select the Category you want to add questions to: \n1.General Knowledge\n2.Pop "
        "Culture\n3.Mathematics\n4.Computer and Technology\n5.Science : ")
    category = ""
    if ca == '1':
        category = "Questions/GK_Q.txt"
    if ca == '2':
        category = "Questions/PopCulture_Q.txt"
    if ca == '3':
        category = "Questions/Computer_Q.txt"
    if ca == '4':
        category = "Questions/Math_Q.txt"
    if ca == '5':
        category = "Questions/Science_Q.txt"

    with open(f"{category}", "a") as f:

        aq = input("Enter the question you want to add: ")
        aa = input("Enter the correct option: ")
        print("Question Added Succesfully")

        f.write('\n' + '#' + aq + ':' + aa)
