import Mysqlf as b
import Functionsq as F
import time

while True:
    print("Welcome to THE GREATEST QUIZ OF ALL TIME".center(69, '='))
    print("Do you want to:")
    print('1.Register \n2.Login\n3.Exit')

    choice = input("Enter your choice:  ")

    vadmin = False

    if choice == '1':
        b.signup()
        print('='.center(69, '='))
        print("Please login with your account now:  ")
        print('='.center(69, '='))

    if choice == '2':
        ask = input("Are you an admin ? (yes/no):  ")

        if ask.lower() == 'yes':
            con = input('Enter Password: ')

            if con == 'admin':
                vadmin = True
                print('='.center(69, '='))

                while True:
                    aask = input("Do you want to \n1.View Users Table\n2.View Questions\n3.Add Questions\n4.Exit:  ")
                    print('='.center(69, '='))

                    if aask == '1':
                        b.vt()
                        print('='.center(69, '='))

                    if aask == '2':
                        F.vq()
                        print('='.center(69, '='))

                    if aask == '3':
                        F.aq()
                        print('='.center(69, '='))

                    if aask == '4':
                        break
            else:
                print("Incorrect Password")
                continue

        else:
            verify = b.login()

            if verify == True:
                print("Logged in Successfully")
                print('='.center(69, '='))

            else:
                print(
                    """Incorrect username or password, please try using a different combination or try registering with us again""")
                time.sleep(2)
                continue

        exprof = True

        while True:

            if vadmin == True:
                print("Please Login as a user")
                exprof = False
                break

            print("1.My Profile\n2.Play Quiz\n3.View Leaderboard\n4.Exit")
            choice1 = input("Enter your choice:  ")
            print('='.center(69, '='))

            if choice1 == '1':

                while True:
                    print("1.View Profile\n2.Change password\n3.Delete Profile \n4.Exit")
                    choice2 = input("Enter your choice:  ")
                    print('='.center(69, '='))

                    if choice2 == "1":
                        b.viewprofile()
                        print('='.center(69, '='))

                    if choice2 == "2":
                        b.update()
                        print('='.center(69, '='))

                    if choice2 == "3":
                        b.delete()
                        print('='.center(69, '='))
                        exprof = False
                        break

                    if choice2 == "4":
                        break

            if exprof == False:
                break

            if choice1 == "2":
                while True:
                    print("""Welcome to the Ultimate Quiz Challenge! Here's how the game works:


1. General Rules
• The quiz consists of 15 questions.
• You start with 3 lives.
• Incorrect answers cost you a life.
• If you lose all 3 lives, the game ends.


2. Taking Breaks
• After the 5th and 10th questions, you have the option to take a break and leave with the points you've earned so far.
• If you choose to continue, you'll be playing for the final prize.


3. Lifelines
•   In case you feel stuck in a question you can choose to opt for a lifeline by typing the word “lifeline” in place of the answer
•   You have a total of three lifelines.
•   You can only use one lifeline per question 
•   If using more than one lifeline per question your answer will be treated as incorrect""")

                    print('='.center(69, '='))
                    print(
                        "Select your Category\n1.General Knowledge\n2.Pop Culture\n3.Mathematics\n4.Computer and Technology\n5.Science")
                    choice3 = input("Enter the number corresponding to your choice: ")
                    print('='.center(69, '='))
                    flag = True

                    try:
                        F.Category_Selector(choice3)
                    except FileNotFoundError:
                        print('Please enter a valid choice')
                        flag = False

                    if flag == True:
                        choice4 = input("Are you sure you want to play ? (Yes/No): ")
                        print('='.center(69, '='))

                        if choice4.lower() == 'yes':
                            print("Then let The Greatest Quiz Of All Time Begin.")
                            time.sleep(2)

                            s = F.Quiz_Master()

                            hscore = b.rethscore()

                            if s < hscore:
                                pass

                            else:
                                hscore = s
                                b.changehscore(hscore)

                            b.changescore(s)
                            break

                        else:
                            break

            if choice1 == "3":
                b.ldb()
                print('='.center(69, '='))

            if choice1 == '4':
                break

    if choice == '3':
        print("Thank you for visiting us!")
        print("Have a great day")
        print('='.center(69, '='))
        time.sleep(1)
        break
