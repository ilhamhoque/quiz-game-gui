import json
import operator
import random
import time
from tkinter import *
from tkinter import messagebox

with open('rules.json', 'r') as file:  # opens the rules.json file to read the rules.
    data = json.load(file)

addition_var = -1  # everytime a user gets a addition question. + 1 adds to this variable
subtraction_var = -1  # everytime a user gets a subtraction question. + 1 adds to this variable
multiply_var = -1  # everytime a user gets a multiplication question. + 1 adds to this variable
attempt_var = 0  # everytime a users answer is not correct. + 1 adds to this variable
score_var = 0  # everytime a user answer the question correctly. + 1 adds to this variable.


def save():
    def write_json(student_detail, filename='student.json'):
        with open(filename, 'w') as f:
            json.dump(student_detail, f, indent=2)

    with open('student.json') as json_file:
        data_student = json.load(json_file)

        temp = data_student['student']

        user_name = uname.get()

        details = {  # saves the name, total score and difficulty in an external file.
            "name": str(user_name),
            "difficulty": diff,
            "score": score_var

        }
        temp.append(details)
        write_json(data_student)


def score_result():  # display the user the total score
    s_r = Tk()
    s_r.withdraw()
    messagebox.showinfo("You have completed your score", str(uname.get()) + " your score is " + str(score_var))
    print(str(uname.get()), " Your score is: ", score_var)
    s_r.destroy()
    save()


def check():  # checks if the number of questions from rules equal to the variables
    if addition_var == addition_file and multiply_var == multiplication_file and subtraction_var == subtraction_file:
        print("The quiz is done")
        score_result()

    else:
        random_choose()


def random_choose():  # random chooses operator
    global addition_var, subtraction_var, multiply_var

    list_ques = ["add", "subtract", "multiply"]
    random.shuffle(list_ques)
    one_item = list_ques[0]

    if one_item == "add":
        if addition_var == addition_file:
            check()
        else:
            addition_var = addition_var + 1

            addition()

    elif one_item == "subtract":
        if subtraction_var == subtraction_file:
            check()
        else:
            subtraction_var = subtraction_var + 1

            subtraction()

    elif one_item == "multiply":
        if multiply_var == multiplication_file:
            check()
        else:
            multiply_var = multiply_var + 1

            multiplication()

    else:
        random_choose()


def addition():
    global operator_var, ans, num1, num2
    if addition_var == addition_file:  # checks if the addition question already been done
        random_choose()
    else:
        random_number = ran_num()
        if random_number is None:  # checks if the value is present in the function
            addition()
        else:
            operator_var = "+"
            num1, num2 = random_number

            num1 = int(num1)
            num2 = int(num2)

            ans = operator.add(num1, num2)
            working()


def subtraction():
    global operator_var, ans, num1, num2
    if subtraction_var == subtraction_file:  # checks if the addition question already been done
        random_choose()
    else:
        random_number = ran_num()
        if random_number is None:  # checks if the value is present in the function
            subtraction()
        else:
            operator_var = "-"
            num1, num2 = random_number
            num1 = int(num1)
            num2 = int(num2)

            ans = operator.sub(num1, num2)
            working()


def multiplication():
    global operator_var, ans, num1, num2
    if multiply_var == multiplication_file:  # checks if the multiplication question already been done
        random_choose()
    else:
        random_number = ran_num()
        if random_number is None:  # checks if the value is present in the function
            multiplication()
        else:
            operator_var = "*"
            num1, num2 = random_number
            num1 = int(num1)
            num2 = int(num2)

            ans = operator.mul(num1, num2)
            working()


def working():
    global attempt_var, score_var, operator_var, ans, num1, num2

    a = Tk()  # creates a window
    a.title('Quiz level ' + diff)  # shows the difficulty level

    canvas = Canvas(a, width=720, height=440, bg="#000077")
    canvas.pack()

    frame = Frame(canvas, bg="#a9c5e4")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    user_ans = StringVar()

    question = Label(frame, text="what is " + str(num1) + " " + operator_var + " " + str(num2), bg="#7694e3")
    question.place(relx=0.25, rely=0.4)  # This widget displays question

    user = Entry(frame, bg='white', fg='black', textvariable=user_ans)
    user.config(width=42)  # this widget allows the user to input their answer
    user.place(relx=0.31, rely=0.5)

    def validate():  # checks the user input and validate answer
        global attempt_var, score_var
        try:
            answer = user.get()  # gets the answer from Entry widget
            if int(answer) == int(ans):  # checks if the user answer is correct
                print("you got it")
                got_it = Label(frame, text="You got it", bg="#7694e3")
                got_it.place(relx=0.25, rely=0.6)
                a.update()

                score_var = score_var + 1  # + 1 is added to the score variable
                attempt_var = attempt_var * 0
                time.sleep(1.2)  # This delays 1.2 second. otherwise user won't see if the user got the answer correct or not.
                a.destroy()  # it destroy the addition display
                check()  # it calls checks to see if the number of addition question is equal to the rules

            else:  # if the user doesn't get the answer
                print("you didn't got it")

                attempt_var = attempt_var + 1  # adds + 1 to the attempts variable

                print("attempt_var", attempt_var)

                didnt_got_it = Label(frame, text="you didn't got it", bg="#7694e3")  # this widget displays the correct answer
                didnt_got_it.place(relx=0.25, rely=0.65)

                attempt_it = Label(frame, text="attempt " + str(attempt_var), bg="#7694e3")
                attempt_it.place(relx=0.25, rely=0.75)  # this widget displays the number of attempts
                a.update()
                time.sleep(1.2)  # This delays 1.2 second. otherwise user won't see the Label widgets above.

                if int(attempt_var) == attempt_file:  # if the number of attempts is equal to the attempts from rules.json

                    didnt_got_it = Label(frame, text="you didn't got it.\nThe answer was " + str(ans),
                                         bg="#7694e3")  # this widget displays the correct answer
                    didnt_got_it.place(relx=0.25, rely=0.6)

                    out_attempt = Label(frame, text="You are out of attempt", bg="#7694e3")
                    out_attempt.place(relx=0.25,
                                      rely=0.4)  # displays to show the user that the user is out of attempts.

                    attempt_var = attempt_var * 0
                    a.update()
                    time.sleep(1.2)  # This delays 1.2 second. otherwise user won't see the out_attempt widget.
                    a.destroy()
                    check()  # calls the score_result functions to display the score and then calls another functions from score_result
                else:  # if the attempt variable does not meet the attempts from the rules.
                    pass

        except ValueError:  # if the users input is not integer
            messagebox.showerror("Invalid input", "please only enter an integer")
            print("value error")
            a.update()
            a.destroy()  # destroys the window
            working()  # it will call the addition function again

    submit = Button(frame, command=validate, text="Submit", bg="white", fg="black")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)  # it will call the validate function
    a.mainloop()


def ran_num():  # generates random number
    random_number = data[diff][0]["range"].split(',')  # extracts the rule "range" from the rules.json.

    first_num = int(random_number[0])
    second_num = int(random_number[1])

    random_num1 = random.randint(first_num, second_num)
    random_num2 = random.randint(first_num, second_num)

    if random_num1 is None and random_num2 is None:  # checks if value is present
        ran_num()
    else:
        if random_num1 < random_num2:  # checks if num1 is smaller than  num2
            ran_num()
        else:
            return random_num1, random_num2


def easy():  # when this function gets called it loads all the variable in the ram.
    global diff, addition_file, subtraction_file, multiplication_file, attempt_file
    diff = "easy"
    addition_file = int(data["easy"][0]["ques_add"])
    subtraction_file = int(data["easy"][0]["ques_sub"])
    multiplication_file = int(data["easy"][0]["ques_mul"])
    attempt_file = int(data["easy"][0]["attempt"])
    random_choose()


def standard():  # when this function gets called it loads all the variable in the ram.
    global diff, addition_file, subtraction_file, multiplication_file, attempt_file
    diff = "standard"
    addition_file = int(data["standard"][0]["ques_add"])
    subtraction_file = int(data["standard"][0]["ques_sub"])
    multiplication_file = int(data["standard"][0]["ques_mul"])
    attempt_file = int(data["standard"][0]["attempt"])
    random_choose()


def hard():  # when this function gets called it loads all the variable in the ram.
    global diff, addition_file, subtraction_file, multiplication_file, attempt_file
    diff = "hard"

    addition_file = int(data["hard"][0]["ques_add"])
    subtraction_file = int(data["hard"][0]["ques_sub"])
    multiplication_file = int(data["hard"][0]["ques_mul"])
    attempt_file = int(data["hard"][0]["attempt"])
    random_choose()


def menu():  # the menu for selecting difficulties
    menu_dis = Tk()
    menu_dis.title('Quiz App Menu')

    menu_canvas = Canvas(menu_dis, width=720, height=440, bg="#000077")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="#a9c5e4")
    menu_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(menu_canvas, text=' W E L C O M E  T O  M A T H S  Q U I Z ', fg="white", bg="#000077")
    wel.config(font=('Broadway', "22", "bold"))  # 2nd title
    wel.place(relx=0.1, rely=0.02)
    name_menu = uname.get()
    display_name = 'Welcome ' + str(name_menu)
    level34 = Label(menu_frame, text=display_name, bg="#7694e3", font="calibri 20", fg="white")
    level34.place(relx=0.17, rely=0.15)

    level = Label(menu_frame, text='Select your Difficulty Level !!', bg="#7694e3", font="calibri 18")
    level.place(relx=0.25, rely=0.3)  # heading

    var = IntVar()
    easyR = Radiobutton(menu_frame, text='Easy', bg="#a9c5e4", font="calibri 16", value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)

    mediumR = Radiobutton(menu_frame, text='Standard', bg="#a9c5e4", font="calibri 16", value=2, variable=var)
    mediumR.place(relx=0.25, rely=0.5)

    hardR = Radiobutton(menu_frame, text='Hard', bg="#a9c5e4", font="calibri 16", value=3, variable=var)
    hardR.place(relx=0.25, rely=0.6)

    def navigate():
        # it will call the function for either easy, standard or hard function. this will only load the function for one difficulty only.
        x = var.get()
        print(x)
        if x == 1:
            menu_dis.destroy()
            easy()
        elif x == 2:
            menu_dis.destroy()
            standard()

        elif x == 3:
            menu_dis.destroy()
            hard()
        else:
            pass

    click = Button(menu_frame, text="Click", bg="white", fg="black", font="calibri 12", command=navigate)
    click.place(relx=0.25, rely=0.8)
    menu_dis.mainloop()


def gui_login():  # The login display. this display will open first
    global uname, user_menu
    gui_login_dis = Tk()
    gui_login_dis.title("Welcome to the quiz game")

    uname = StringVar()

    gui_login_canvas = Canvas(gui_login_dis, width=720, height=440, bg="#000077")
    gui_login_canvas.pack()

    gui_login_frame = Frame(gui_login_canvas, bg="#a9c5e4")
    gui_login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(gui_login_frame, text="Login", fg="white", bg="#7694e3")
    heading.config(font=("", 45))  # heading
    heading.place(relx=0.4, rely=0.1)

    heading_2nd = Label(gui_login_frame, text="Please enter your name", fg="white", bg="#7694e3", font=("", 25, "bold"))
    heading_2nd.place(relx=0.3, rely=0.3)  # sub-heading

    user_label = Label(gui_login_frame, text="name", fg='white', bg='black')
    user_label.place(relx=0.21, rely=0.5)

    user_menu = Entry(gui_login_frame, bg='white', fg='black', textvariable=uname)
    user_menu.config(width=42)  # this widget allows the user to input an text
    user_menu.place(relx=0.31, rely=0.5)

    def check_name_present():  # checks if the value is present
        if len(user_menu.get()) == 0:
            error = Label(gui_login_frame, text="please enter username", fg='black', bg='#7694e3')
            error.place(relx=0.37, rely=0.7)
            gui_login_dis.update()
        else:
            gui_login_dis.destroy()  # if the value is present
            menu()

    log = Button(gui_login_frame, text='Login', padx=5, pady=5, width=5, command=check_name_present, fg="black")
    log.configure(width=15, height=1, activebackground="#33B5E5",
                  relief=FLAT)  # this button calls the check_name_present function
    log.place(relx=0.4, rely=0.6)

    gui_login_dis.mainloop()


gui_login()
