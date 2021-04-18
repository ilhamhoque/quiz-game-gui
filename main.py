import random
import json
from tkinter import *
import time
from tkinter import messagebox

with open('rules.json', 'r') as file:
    data = json.load(file)

addition_var = -1
subtraction_var = -1
multiply_var = -1
attempt_var = 0
score_var = 0


def save():
    def write_json(student_detail, filename='student.json'):
        with open(filename, 'w') as f:
            json.dump(student_detail, f, indent=2)

    with open('student.json') as json_file:
        data_student = json.load(json_file)

        temp = data_student['student']

        user_name = uname.get()

        details = {
            "name": str(user_name),
            "difficulty": diff,
            "score": score_var

        }
        temp.append(details)
        write_json(data_student)
        quit()


def score_result():
    messagebox.showinfo("You have completed your score", str(uname.get()) + " your score is "+str(score_var))
    print(str(uname.get()), " Your score is: ", score_var)
    save()



def check():
    if addition_var == addition_file and multiply_var == multiplication_file and subtraction_var == subtraction_file:
        print("The quiz is done")
        score_result()

    else:
        random_choose()




def random_choose():
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


def addition():  ### Addition #####
    global attempt_var, score_var, addition_var

    if addition_var == addition_file:
        print(addition_var)
        random_choose()
    else:
        random_number = ran_num()
        if random_number is None:
            addition()
        else:
            global a
            a = Tk()
            a.title('Quiz level ' + diff)

            add_canvas = Canvas(a, width=720, height=440, bg="#000077")
            add_canvas.pack()

            add_frame = Frame(add_canvas, bg="#a9c5e4")
            add_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

            add_num, add2_num = random_number
            add_num = int(add_num)
            add2_num = int(add2_num)
            ans = (add_num + add2_num)

            user_ans = StringVar()

            question = Label(add_frame, text="what is " + str(add_num) + " + " + str(add2_num), bg="#7694e3")
            question.place(relx=0.25, rely=0.4)

            user = Entry(add_frame, bg='white', fg='black', textvariable=user_ans)
            user.config(width=42)
            user.place(relx=0.31, rely=0.5)

            def validate():
                global attempt_var, score_var, addition_var

                try:
                    answer = user.get()
                    if int(answer) == int(ans):
                        print("you got it")
                        got_it = Label(add_frame, text="You got it", bg="#7694e3")
                        got_it.place(relx=0.25, rely=0.6)
                        a.update()

                        score_var = score_var + 1
                        time.sleep(1.2)
                        a.destroy()
                        check()

                    else:
                        print("you didn't got it")
                        print("the answer was", ans)

                        attempt_var = attempt_var + 1

                        print("attempt_var", attempt_var)

                        didnt_got_it = Label(add_frame, text="you didn't got it.\nThe answer was " + str(ans),
                                             bg="#7694e3")
                        didnt_got_it.place(relx=0.25, rely=0.6)

                        attempt_it = Label(add_frame, text="attempt " + str(attempt_var), bg="#7694e3")
                        attempt_it.place(relx=0.25, rely=0.75)
                        a.update()
                        time.sleep(1.2)

                        if int(attempt_var) == attempt_file:
                            print("your out of attempt_var")

                            out_attempt = Label(add_frame, text="You are out of attempt", bg="#7694e3")
                            out_attempt.place(relx=0.25, rely=0.4)

                            a.update()
                            time.sleep(1.2)
                            a.destroy()
                            score_result()
                        else:
                            a.update()

                            a.destroy()
                            check()

                except ValueError:
                    messagebox.showerror("Invalid input", "please only enter an integer")
                    print("value error")
                    a.update()
                    a.destroy()
                    addition()

            submit = Button(add_frame, command=validate, text="Submit", bg="black")
            submit.place(relx=0.5, rely=0.82, anchor=CENTER)
            a.mainloop()


def subtraction():  ### Subtraction ####
    global attempt_var, score_var, subtraction_var

    if subtraction_var == subtraction_file:
        random_choose()
    else:

        random_number = ran_num()
        if random_number is None:
            subtraction()
        else:
            global s
            s = Tk()
            s.title("Quiz level " + diff)

            sub_canvas = Canvas(s, width=720, height=440, bg="#000077")
            sub_canvas.pack()

            sub_frame = Frame(sub_canvas, bg="#a9c5e4")
            sub_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

            add_num, add2_num = random_number
            add_num = int(add_num)
            add2_num = int(add2_num)

            ans = (add_num - add2_num)
            user_ans = StringVar()

            question = Label(sub_frame, text="what is " + str(add_num) + " - " + str(add2_num), bg="#7694e3")
            question.place(relx=0.25, rely=0.4)

            user = Entry(sub_frame, bg='white', fg='black', textvariable=user_ans)
            user.config(width=42)
            user.place(relx=0.31, rely=0.5)

            def validate():
                global attempt_var, score_var, subtraction_var
                try:
                    answer = user.get()
                    if int(answer) == ans:
                        print("you got it")

                        got_it = Label(sub_frame, text="You got it", bg="#7694e3")
                        got_it.place(relx=0.25, rely=0.6)
                        s.update()

                        score_var = score_var + 1
                        time.sleep(1.2)
                        s.destroy()
                        check()
                    else:
                        print("you didn't got it")
                        print("the answer was", ans)
                        attempt_var = attempt_var + 1

                        print("attempt_var", attempt_var)

                        didnt_got_it = Label(sub_frame, text="you didn't got it.\nThe answer was " + str(ans),
                                             bg="#7694e3")
                        didnt_got_it.place(relx=0.25, rely=0.6)

                        attempt_it = Label(sub_frame, text="attempt " + str(attempt_var), bg="#7694e3")
                        attempt_it.place(relx=0.25, rely=0.75)
                        s.update()
                        time.sleep(1.2)

                        if int(attempt_var) == attempt_file:
                            print("your out of attempt")

                            out_attempt = Label(sub_frame, text="You are out of attempt", bg="#7694e3")
                            out_attempt.place(relx=0.25, rely=0.4)
                            s.update()
                            time.sleep(1.2)
                            s.destroy()
                            score_result()
                        else:
                            s.update()

                            s.destroy()
                            check()

                except ValueError:
                    messagebox.showerror("Invalid input", "please only enter an integer")
                    print("value error")
                    s.update()
                    s.destroy()
                    subtraction()

            submit = Button(sub_frame, command=validate, text="Submit", bg="black")
            submit.place(relx=0.5, rely=0.82, anchor=CENTER)
            s.mainloop()


def multiplication():  ### Multiplication ######
    global attempt_var, score_var, multiply_var

    if multiply_var == multiplication_file:
        random_choose()
    else:
        random_number = ran_num()
        if random_number is None:
            multiplication()
        else:
            global m
            m = Tk()
            m.title("Quiz level " + diff)

            mul_canvas = Canvas(m, width=720, height=440, bg="#000077")
            mul_canvas.pack()

            mul_frame = Frame(mul_canvas, bg="#a9c5e4")
            mul_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

            add_num, add2_num = random_number
            add_num = int(add_num)
            add2_num = int(add2_num)
            ans = (add_num * add2_num)

            user_ans = StringVar()

            question = Label(mul_frame, text="what is " + str(add_num) + " x " + str(add2_num), bg="#7694e3")
            question.place(relx=0.25, rely=0.4)

            user = Entry(mul_frame, bg='white', fg='black', textvariable=user_ans)
            user.config(width=42)
            user.place(relx=0.31, rely=0.5)

            def validate():
                global attempt_var, score_var, multiply_var
                try:
                    answer = user.get()
                    if int(answer) == ans:
                        print("you got it")

                        got_it = Label(mul_frame, text="You got it", bg="#7694e3")
                        got_it.place(relx=0.25, rely=0.6)
                        m.update()

                        score_var = score_var + 1
                        time.sleep(1.2)
                        m.destroy()

                        check()
                    else:
                        print("you didn't got it")
                        print("the answer was", ans)
                        attempt_var = attempt_var + 1

                        print("attempt_var", attempt_var)

                        didnt_got_it = Label(mul_frame, text="you didn't got it.\nThe answer was " + str(ans),
                                             bg="#7694e3")
                        didnt_got_it.place(relx=0.25, rely=0.6)

                        attempt_it = Label(mul_frame, text="attempt " + str(attempt_var), bg="#7694e3")
                        attempt_it.place(relx=0.25, rely=0.75)
                        m.update()
                        time.sleep(1.2)

                        if int(attempt_var) == attempt_file:
                            print("your out of attempt_var")

                            out_attempt = Label(mul_frame, text="You are out of attempt", bg="#7694e3")
                            out_attempt.place(relx=0.25, rely=0.4)
                            m.update()
                            time.sleep(1.2)
                            m.destroy()
                            score_result()

                        else:
                            m.update()

                            m.destroy()
                            check()

                except ValueError:
                    messagebox.showerror("Invalid input", "please only enter an integer")
                    print("value error")
                    m.update()
                    m.destroy()
                    multiplication()

            submit = Button(mul_frame, command=validate, text="Submit", bg="black")
            submit.place(relx=0.5, rely=0.82, anchor=CENTER)
            m.mainloop()


def ran_num():
    random_number = data[diff][0]["range"].split(',')

    a_a = int(random_number[0])
    b_b = int(random_number[1])

    num1 = random.randint(a_a, b_b)
    num2 = random.randint(a_a, b_b)

    if num1 is None and num2 is None:
        ran_num()
    else:
        if num1 <= num2:
            ran_num()
        else:
            return num1, num2


def easy():
    global diff, addition_file, subtraction_file, multiplication_file, attempt_file
    diff = "easy"
    addition_file = int(data["easy"][0]["ques_add"])
    subtraction_file = int(data["easy"][0]["ques_sub"])
    multiplication_file = int(data["easy"][0]["ques_mul"])
    attempt_file = int(data["easy"][0]["attempt"])
    random_choose()


def standard():
    global diff, addition_file, subtraction_file, multiplication_file, attempt_file
    diff = "standard"
    addition_file = int(data["standard"][0]["ques_add"])
    subtraction_file = int(data["standard"][0]["ques_sub"])
    multiplication_file = int(data["standard"][0]["ques_mul"])
    attempt_file = int(data["standard"][0]["attempt"])
    random_choose()


def hard():
    global diff, addition_file, subtraction_file, multiplication_file, attempt_file
    diff = "hard"

    addition_file = int(data["hard"][0]["ques_add"])
    subtraction_file = int(data["hard"][0]["ques_sub"])
    multiplication_file = int(data["hard"][0]["ques_mul"])
    attempt_file = int(data["hard"][0]["attempt"])
    random_choose()


def menu():
    gui_login.destroy()
    global menu

    menu = Tk()
    menu.title('Quiz App Menu')

    menu_canvas = Canvas(menu, width=720, height=440, bg="#000077")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="#a9c5e4")
    menu_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(menu_canvas, text=' W E L C O M E  T O  M A T H S  Q U I Z ', fg="white", bg="#000077")
    wel.config(font=('Broadway', "22", "bold"))
    wel.place(relx=0.1, rely=0.02)
    name_menu = uname.get()
    display_name = 'Welcome ' + str(name_menu)
    level34 = Label(menu_frame, text=display_name, bg="#7694e3", font="calibri 20", fg="white")
    level34.place(relx=0.17, rely=0.15)

    level = Label(menu_frame, text='Select your Difficulty Level !!', bg="#7694e3", font="calibri 18")
    level.place(relx=0.25, rely=0.3)

    var = IntVar()
    easyR = Radiobutton(menu_frame, text='Easy', bg="#a9c5e4", font="calibri 16", value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)

    mediumR = Radiobutton(menu_frame, text='Standard', bg="#a9c5e4", font="calibri 16", value=2, variable=var)
    mediumR.place(relx=0.25, rely=0.5)

    hardR = Radiobutton(menu_frame, text='Hard', bg="#a9c5e4", font="calibri 16", value=3, variable=var)
    hardR.place(relx=0.25, rely=0.6)

    def navigate():

        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            standard()

        elif x == 3:
            menu.destroy()
            hard()
        else:
            pass

    click = Button(menu_frame, text="Click", bg="black", fg="black", font="calibri 12", command=navigate)
    click.place(relx=0.25, rely=0.8)
    menu.mainloop()


def gui_login():
    global gui_login
    global uname, user_menu
    gui_login = Tk()
    gui_login.title("Welcome to the quiz game")

    uname = StringVar()

    gui_login_canvas = Canvas(gui_login, width=720, height=440, bg="#000077")
    gui_login_canvas.pack()

    gui_login_frame = Frame(gui_login_canvas, bg="#a9c5e4")
    gui_login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(gui_login_frame, text="Login", fg="white", bg="#7694e3")
    heading.config(font=("", 45))
    heading.place(relx=0.4, rely=0.1)

    heading_2nd = Label(gui_login_frame, text="Please enter your name", fg="white", bg="#7694e3", font=("", 25, "bold"))
    heading_2nd.place(relx=0.3, rely=0.3)

    user_label = Label(gui_login_frame, text="name", fg='white', bg='black')
    user_label.place(relx=0.21, rely=0.5)

    user_menu = Entry(gui_login_frame, bg='white', fg='black', textvariable=uname)
    user_menu.config(width=42)
    user_menu.place(relx=0.31, rely=0.5)

    def check_name_present():
        if len(user_menu.get()) == 0:
            error = Label(gui_login_frame, text="please enter username", fg='black', bg='#7694e3')
            error.place(relx=0.37, rely=0.7)
            gui_login.update()
        else:
            menu()

    log = Button(gui_login_frame, text='Login', padx=5, pady=5, width=5, command=check_name_present, fg="black",
                 bg="black")
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.6)

    gui_login.mainloop()



gui_login()
