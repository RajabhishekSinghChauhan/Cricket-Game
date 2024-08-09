
import random

def get_valid_number():
    while True:
        try:
            n = int(input("Enter The Number \U0001f914 : "))
            if 1 <= n <= 6:
                return n
            else:
                print("Please Enter a Digit Between 1 to 6 To Proceed \U0001f615")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

def check_milestones(score, player):
    if score == 50:
        print(f"{player} Scored a Fifty! \U0001f44f")
    elif score == 100:
        print(f"{player} Scored a Century! \U0001f44f\U0001f44f")

def cricket_game():
    print("\U0001f3cf Welcome To The Cricket Game \U0001f3cf")

    while True:
        sum_user = 0
        sum_computer = 0

        ready1 = int(input('''Are You Ready \U0001f609 : 
        1) Yes
        2) No
        '''))

        if ready1 == 2:
            print("We Appreciate Your Answer \U0001f607, Thank you :)")
            break
        elif ready1 == 1:
            print("Here We Go \U0001f60e")
            ready2 = int(input('''Are You Ready For Toss \U0001f609 : 
            1) Yes
            2) No
            '''))

            if ready2 == 2:
                print("We Appreciate Your Answer \U0001f607, Thank you :)")
                break
            else:
                toss = int(input('''What's Your Call
                1) Head
                2) Tail
                '''))

                toss_result = random.randint(1, 2)
                print("Toss Result Is ", toss_result)

                if toss_result == toss:
                    print("You Won The Toss")
                    bat_bowl = int(input('''What Do You Choose
                    1) Bat
                    2) Bowl
                    '''))

                    if bat_bowl == 1:
                        print("You Have To Bat First")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Your Score Is \U0001f440 \U0001f4c8:", sum_user)
                                print("You Have Given Target Of ", sum_user + 1, " To Computer ")
                                break
                            else:
                                sum_user += n
                                print("Your Score Is \U0001f4c8: ", sum_user)
                                check_milestones(sum_user, "You")

                        target = sum_user + 1
                        print("Now It's Your Turn To Bowl")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Computer's Score Is \U0001f440 \U0001f4c8:", sum_computer)
                                if sum_user > sum_computer:
                                    print('''WINNER=You
                                    LOSER=Computer    you won by ''',sum_user - sum_computer,''' runs''')
                                elif sum_user == sum_computer:
                                    print("It's a DRAW")
                                else:
                                    print('''WINNER=Computer
                                    LOSER=You    computer won by ''',sum_computer - sum_user,''' runs''')
                                break
                            else:
                                sum_computer += m
                                print("Computer's Score Is \U0001f4c8: ", sum_computer)
                                check_milestones(sum_computer, "Computer")
                                target -= m
                                print("Target Left: ", target)
                                if sum_computer >= sum_user + 1:
                                    print('''WINNER=Computer
                                    LOSER=You     computer won by ''', sum_computer - sum_user ,''' runs''')
                                    break

                    elif bat_bowl == 2:
                        print("You Have To Bowl First")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Computer's Score Is \U0001f440 \U0001f4c8:", sum_computer)
                                print("Computer Gives Target Of ", sum_computer + 1, " To You")
                                break
                            else:
                                sum_computer += m
                                print("Computer's Score Is \U0001f4c8: ", sum_computer)
                                check_milestones(sum_computer, "Computer")

                        target = sum_computer + 1
                        print("Now It's Your Turn To Bat")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Your Score Is \U0001f440 \U0001f4c8:", sum_user)
                                if sum_user > sum_computer:
                                    print('''WINNER=You
                                    LOSER=Computer''')
                                elif sum_user == sum_computer:
                                    print("It's a DRAW")
                                else:
                                    print('''WINNER=Computer
                                    LOSER=You''')
                                break
                            else:
                                sum_user += n
                                print("Your Score Is \U0001f4c8: ", sum_user)
                                check_milestones(sum_user, "You")
                                target -= n
                                print("Target Left: ", target)
                                if sum_user >= sum_computer + 1:
                                    print('''WINNER=You
                                    LOSER=Computer''')
                                    break

                    else:
                        print("Invalid Choice")
                else:
                    computer_call = random.randint(1, 2)
                    if computer_call == 1:
                        print("You Lost The Toss, Computer Chooses To Bowl First")
                        print("You Have To Bat First")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Your Score Is \U0001f440 \U0001f4c8:", sum_user)
                                print("You Have Given Target Of ", sum_user + 1, " To Computer ")
                                break
                            else:
                                sum_user += n
                                print("Your Score Is \U0001f4c8: ", sum_user)
                                check_milestones(sum_user, "You")

                        target = sum_user + 1
                        print("Now It's Your Turn To Bowl")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Computer's Score Is \U0001f440 \U0001f4c8:", sum_computer)
                                if sum_user > sum_computer:
                                    print('''WINNER=You
                                    LOSER=Computer''')
                                elif sum_user == sum_computer:
                                    print("It's a DRAW")
                                else:
                                    print('''WINNER=Computer
                                    LOSER=You''')
                                break
                            else:
                                sum_computer += m
                                print("Computer's Score Is \U0001f4c8: ", sum_computer)
                                check_milestones(sum_computer, "Computer")
                                target -= m
                                print("Target Left: ", target)
                                if sum_computer >= sum_user + 1:
                                    print('''WINNER=Computer
                                    LOSER=You''')
                                    break

                    else:
                        print("You Lost The Toss, Computer Chooses To Bat First")
                        print("You Have To Bowl First")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Computer's Score Is \U0001f440 \U0001f4c8:", sum_computer)
                                print("Computer Gives Target Of ", sum_computer + 1, " To You")
                                break
                            else:
                                sum_computer += m
                                print("Computer's Score Is \U0001f4c8: ", sum_computer)
                                check_milestones(sum_computer, "Computer")

                        target = sum_computer + 1
                        print("Now It's Your Turn To Bat")
                        while True:
                            n = get_valid_number()
                            print("You Played", n, " Now Let's See What Computer Plays \U0001f609 ")
                            m = random.randint(1, 6)
                            print("Computer played \U0001f60b", m)

                            if n == m:
                                print("'OUT' \U0001f62D \U0001f44e, Well Played \U0001f91f. Your Score Is \U0001f440 \U0001f4c8:", sum_user)
                                if sum_user > sum_computer:
                                    print('''WINNER=You
                                    LOSER=Computer you won by ''',sum_user - sum_computer,''' runs''')
                                elif sum_user == sum_computer:
                                    print("It's a DRAW")
                                else:
                                    print('''WINNER=Computer
                                    LOSER=You   computer won by ''',sum_computer - sum_user,''' runs''')
                                break
                            else:
                                sum_user += n
                                print("Your Score Is \U0001f4c8: ", sum_user)
                                check_milestones(sum_user, "You")
                                target -= n
                                print("Target Left: ", target)
                                if sum_user >= sum_computer + 1:
                                    print('''WINNER=You
                                    LOSER=Computer    you won by ''',sum_user - sum_computer,''' runs'''  )
                                    break

        else:
            print("Invalid Choice")

cricket_game()
