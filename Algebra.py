import random
import time
from fractions import Fraction
#@Author Arthur Strizheus
# Global Vars
# ********************************
# Vars for Linear Algebra
global rightNum
global leftNum
global rightX
global leftX
# ********************************


def mainMenu():
    print('\n\n\n\n\n**************************************************')
    print("What would you like to practice(Enter the Number):")
    print("1: Linear Algebra\n2: Powers\n3: Roots\n4: Equations")
    usr = int(input(": "))

    if usr == 1:
        print("\n\n\n\n")
        linearAlgebra()
    elif usr == 2:
        print("\n\n\n\n")
        powers()
    elif usr == 3:
        print("\n\n\n\n")
        roots()
    elif usr == 4:
        print("\n\n\n\n")
        equations()


def printProblem(x, qCount):
    '''
        Prints the problem if x = 1 prints the available commands.
    :param x:           [Int] Type of output
    :return: Null
    '''
    global leftX
    global rightX
    global leftNum
    global rightNum
    if x == 1:
        print('********************************')
        print('Problem (' + str(qCount) + '): ', end='')
        if leftNum >= 0 and rightNum >= 0:
                print('\n\t' + str(leftX) + 'x +', leftNum, '=', str(rightX) + 'x +', rightNum)
        elif leftNum < 0 and rightNum < 0:
            print('\n\t' + str(leftX) + 'x -', abs(leftNum), '=', str(rightX) + 'x -', abs(rightNum))
        elif leftNum < 0 and rightNum > 0:
            print('\n\t' + str(leftX) + 'x -', abs(leftNum), '=', str(rightX) + 'x +', rightNum)
        elif leftNum > 0 and rightNum < 0:
            print('\n\t\t' + str(leftX) + 'x +', leftNum, '=', str(rightX) + 'x -', abs(rightNum))
        print('********************************')
    elif x == 2:
        print('********************************')
        print('Problem (' + str(qCount) + '): ', end='')
        if leftNum >= 0 and rightNum >= 0:
            print('\n\t' + str(leftX) + 'x +', leftNum, '=', str(rightX) + 'x +', rightNum)
        elif leftNum < 0 and rightNum < 0:
            print('\n\t' + str(leftX) + 'x -', abs(leftNum), '=', str(rightX) + 'x -', abs(rightNum))
        elif leftNum < 0 and rightNum > 0:
            print('\n\t' + str(leftX) + 'x -', abs(leftNum), '=', str(rightX) + 'x +', rightNum)
        elif leftNum > 0 and rightNum < 0:
            print('\n\t\t' + str(leftX) + 'x +', leftNum, '=', str(rightX) + 'x -', abs(rightNum))
        print('********************************')
    elif x == 3:
        print('\n\n\n')
        print('********************************')
        print('Type \'Next\' if you don\'t know')
        print('Type \'Hint\' for hints')


def getProblem(fractions):
    global leftX
    global rightX
    global leftNum
    global rightNum
    answer = 0
    leftX = random.randint(-150, 200)
    rightX = random.randint(-150, 200)
    leftNum = random.randint(-150, 150)
    rightNum = random.randint(-150, 150)
    if rightX >= 0:
        xAdd = leftX - rightX
    else:
        xAdd = leftX + abs(rightX)
    if leftNum >= 0:
        numAdd = rightNum - leftNum
    else:
        numAdd = rightNum + abs(leftNum)
    while xAdd == 0:
        leftX = random.randint(-150, 200)
        rightX = random.randint(-150, 200)
        if rightX >= 0:
            xAdd = leftX - rightX
        else:
            xAdd = leftX + rightX
    answer = Fraction(numAdd/xAdd).limit_denominator(100)
    answerToFloat = float(answer)
    while not answerToFloat.is_integer() and fractions is False:
        leftX = random.randint(-150, 200)
        rightX = random.randint(-150, 200)
        leftNum = random.randint(-150, 150)
        rightNum = random.randint(-150, 150)
        if rightX >= 0:
            xAdd = leftX - rightX
        else:
            xAdd = leftX + abs(rightX)
        if leftNum >= 0:
            numAdd = rightNum - leftNum
        else:
            numAdd = rightNum + abs(leftNum)
        while xAdd == 0:
            leftX = random.randint(-150, 200)
            rightX = random.randint(-150, 200)
            if rightX >= 0:
                xAdd = leftX - rightX
            else:
                xAdd = leftX + abs(rightX)
        answer = Fraction(numAdd/xAdd).limit_denominator(100)
        answerToFloat = float(answer)
        answer = int(answerToFloat)
    return answer


def linearAlgebra():
    '''
        Handles calculations and correct and incorrect answers.
    :var xAdd:                [Int] Combines x's to one side(left)
    :var numAdd:              [Int] Combines numbers to one side(right)
    :var leftX:               [Int, Random] Random number assigned to X value on left side of equation
    :var rightX:              [Int, Random] Random number assigned to X value on right side of equation
    :var leftNum:             [Int, Random] Random number assigned to Number value on right side of equation
    :var rightNum:            [Int, Random] Random number assigned to Number value on right side of equation
    :var prbAmt:              [Int] Number of problems the user wants to do.
    :var fracStr:             [String] Y(yes) if user wants to see fractions N(no) if not
    :var fractions:           [Bool] T if user answered Y to see fractions F if answered N
    :var correct:             [Bool] T of users answer is correct F if not
    :return Null:
    '''
    print("**********************************")
    print("**********LINEAR ALGEBRA**********")
    print("**********************************")
    prbAmt = int(input('How many problems would you like to practice?: '))
    fracStr = input('Would you like to see Fractions in answers?(Y or N): ').lower()
    fractions = False
    qCount = 0
    if fracStr == 'y':
        fractions = True
    for x in range(1, prbAmt + 1):
        qCount = x
        correct = False
        answer = getProblem(fractions)
        printProblem(3, qCount)  # Printing problem type 1
        while not correct:
            if fractions:
                printProblem(2, qCount)  # Printing problem type 2
                usrAnswer = input("Answer(As A Fraction) x = ")
            else:
                printProblem(2, qCount)  # Printing problem type 2
                usrAnswer = input("Answer x = ")
            if usrAnswer.lower() == 'next':
                print('The Answer Was x =', answer)
                time.sleep(2)
                correct = True
            elif usrAnswer.lower() == 'hint':
                print('\n\n\n')
                print('********************************')
                print('Take all X  to one side')
                print('Take all numbers to one side')
                print('Separate numbers from x, opposite of multiplication')
                print('EVERYTHING you do to one side you must do to the other!')
                print('********************************')
                print('Press Enter to continue')
                input()
            else:
                if usrAnswer != str(answer):
                    print('\nINCORRECT!\n')
                    time.sleep(2)
                elif usrAnswer == str(answer):
                    print('\n!CORRECT!\n')
                    correct = True
                    time.sleep(2)
    print('Congratulations! you have finished all the problems!')
    print('\nHeading back to Main Menu...')
    time.sleep(2)
    mainMenu()








def powers():
    print("**********************************")
    print("**************POWERS**************")
    print("**********************************")
    print("\nSorry this portion of the program has not been finished.")
    print('\nHeading back to Main Menu...')
    time.sleep(2)
    mainMenu()


def roots():
    print("**********************************")
    print("**************ROOTS***************")
    print("**********************************")
    print("\nSorry this portion of the program has not been finished.")
    print('\nHeading back to Main Menu...')
    time.sleep(2)
    mainMenu()


def equations():
    print("**********************************")
    print("************EQUATIONS*************")
    print("**********************************")
    print("\nSorry this portion of the program has not been finished.")
    print('\nHeading back to Main Menu...')
    time.sleep(2)
    mainMenu()


print("**!!Welcome to Math Practice!!**")
print("What would you like to practice(Enter the Number):")
print("1: Linear Algebra\n2: Powers\n3: Roots\n4: Equations")
usr = int(input(": "))


if usr == 1:
    print("\n\n\n\n")
    linearAlgebra()
elif usr == 2:
    print("\n\n\n\n")
    powers()
elif usr == 3:
    print("\n\n\n\n")
    roots()
elif usr == 4:
    print("\n\n\n\n")
    equations()
