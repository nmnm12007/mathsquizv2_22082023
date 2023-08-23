# 2
# Sri Rama Jayam
# #####################
# Game Main
# This class has methods that will pose math questions to the children based on their
# school class level and evaluate their responses computed
# #####################
# For Level I     - it will be one-digit numbers on math operations - addition and subtraction
# For Level II    - it will be one-digit and two-digit numbers on math operations - addition and subtraction
# For Level III   - it will be two-digit and three-digit numbers on math operations - addition, subtraction,
#                   multiplication
# #####################

from random import randint, choice

s1, s2, op1, success_cnt = 0, 0, '', 0


def quiz_question1():
    op = ['+', '-', '*']
    a, b, op = randint(5, 9), randint(1, 4), choice(op)
    return a, b, op


def quiz_ans_chk_for_std_1(a, b, op):
    c_ans = eval(str(a) + op + str(b))
    return str(c_ans)


def quiz_question2():
    op = ['+', '-', '*']
    a, b, op = randint(10, 99), randint(2, 9), choice(op)
    return a, b, op


def quiz_ans_chk_for_std_2(a, b, op):
    c_ans = eval(str(a) + op + str(b))
    return str(c_ans)


def quiz_question3():
    op = ['+', '-', '*']
    a, b, op = randint(100, 999), randint(2, 9), choice(op)
    return a, b, op


def quiz_ans_chk_for_std_3(a, b, op):
    c_ans = eval(str(a) + op + str(b))
    return str(c_ans)


def pose_quiz(std):
    print("Standard in question:  ", std)
    global s1, s2, op1
    match int(std):
        case 1:
            s1, s2, op1 = quiz_question1()
            print("quizQuestion1: ", s1, op1, s2)
            return s1, s2, op1

        case 2:
            s1, s2, op1 = quiz_question2()
            print("quizQuestion2: ", s1, op1, s2)
            return s1, s2, op1

        case 3:
            s1, s2, op1 = quiz_question3()
            print("quizQuestion3: ", s1, op1, s2)
            return s1, s2, op1


def check_answer(std, answer):
    global s1, s2, op1, success_cnt
    match int(std):
        case 1:
            c_answer = quiz_ans_chk_for_std_1(s1, s2, op1)
            if answer == c_answer:
                h_ans = "CORRECTLY"
                success_cnt += 1
            else:
                h_ans = "WRONGLY"
            return c_answer, h_ans, success_cnt

        case 2:
            c_answer = quiz_ans_chk_for_std_2(s1, s2, op1)
            if answer == c_answer:
                h_ans = "CORRECTLY"
                success_cnt += 1
            else:
                h_ans = "WRONGLY"
            return c_answer, h_ans, success_cnt

        case 3:
            c_answer = quiz_ans_chk_for_std_3(s1, s2, op1)
            if answer == c_answer:
                h_ans = "CORRECTLY"
                success_cnt += 1
            else:
                h_ans = "WRONGLY"
            return c_answer, h_ans, success_cnt



#
# class MathQuizForChildren:
#     def __int__(self):
#         self.a, self.b = 0, 0
#
#
# m = MathQuizForChildren()


# def pose_quiz(self) -> None:
#     try:
#         std, chk_ans = int(input("Enter the Level which you are in:  1, 2, 3 :    ")), 0
#         print(std)
#         print("Quiz Starts, press Q or q to quit anytime")
#     except ValueError:
#         print("Quits Quiz Now !!")
#         exit(1)
#     match std:
#         case 1:
#             for i in range(1, 6):
#                 chk_ans += 1 if m.quiz_for_std_1() == "CORRECT Answer" else chk_ans
#         case 2:
#             for i in range(1, 6):
#                 chk_ans += 1 if m.quiz_for_std_2() == "CORRECT Answer" else chk_ans
#         case 3:
#             for i in range(1, 6):
#                 chk_ans += 1 if m.quiz_for_std_3() == "CORRECT Answer" else chk_ans
#         case 'q':
#             print("Quits Quiz now!  ")
#             exit(1)
#         case 'Q':
#             print("Quits Quiz now!  ")
#             exit(1)
#         case default:
#             print("Quits Quiz now!  ")
#
#     print("You have answered " + str(chk_ans) + "  out of 5 questions correctly !!  ")
# def quiz_for_std_1(a, b, op):
#     op = ['+', '-']
#     a, b, op, ans = randint(5, 9), randint(1, 4), choice(op), ''
#     c_ans = eval(str(a) + op + str(b))
#     try:
#         h_ans = int(input(str(a) + "  " + op + "  " + str(b) + "  "))
#         print(str(a) + "  " + op + "  " + str(b) + " = " + str(c_ans))
#         ans = "CORRECT Answer" if h_ans == c_ans else "Wrong Answer"
#         print(ans)
#     except ValueError:
#         print("Quits Quiz Now !!")
#         exit(1)
#     return ans
#
#
# def quiz_for_std_2():
#     op = ['+', '-']
#     a, b, op, ans = randint(10, 99), randint(2, 9), choice(op), ''
#     c_ans = eval(str(a) + op + str(b))
#     try:
#         h_ans = int(input(str(a) + "  " + op + "  " + str(b) + "  "))
#         print(str(a) + "  " + op + "  " + str(b) + " = " + str(c_ans))
#         ans = "CORRECT Answer" if h_ans == c_ans else "Wrong Answer"
#         print(ans)
#     except ValueError:
#         print("Quits Quiz Now !!")
#         exit(1)
#     return ans
#
#
# def quiz_for_std_3():
#     op = ['+', '-', '*']
#     a, b, op, ans = randint(100, 999), randint(2, 9), choice(op), ''
#     c_ans = eval(str(a) + op + str(b))
#     try:
#         h_ans = int(input(str(a) + "  " + op + "  " + str(b) + "  "))
#         print(str(a) + "  " + op + "  " + str(b) + " = " + str(c_ans))
#         ans = "CORRECT Answer" if h_ans == c_ans else "Wrong Answer"
#         print(ans)
#     except ValueError:
#         print("Quits Quiz Now !!")
#         exit(1)
#     return ans

# m.pose_quiz()
