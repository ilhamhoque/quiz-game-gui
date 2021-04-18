import json
from tkinter import *
from tkinter import messagebox

with open('rules.json', 'r') as file:
    data = json.load(file)


def destroyReplace_Menu():
    app.destroy()
    end_menu()


def result():
    global result_display
    result_display = Tk()
    result_display.title("Results")

    result_display_canvas = Canvas(result_display, width=720, height=440, bg="#000077")
    result_display_canvas.pack()

    result_display_frame = Frame(result_display_canvas, bg="#a9c5e4")
    result_display_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(result_display_frame, text="Please enter the name of the student", fg="white",
                    bg="#7694e3", font=("", 25, "bold"))
    heading.place(relx=0.2, rely=0.3)

    label_ = Label(result_display_frame, text="Name:", fg='white', bg='black')
    label_.place(relx=0.21, rely=0.5)

    var = StringVar

    user_value = Entry(result_display_frame, bg='white', fg='black', textvariable=var)
    user_value.config(width=42)
    user_value.place(relx=0.31, rely=0.5)

    def check_name_present():
        if len(user_value.get()) == 0:
            error = Label(text="Name can't be empty", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)
        else:
            name = str(user_value.get())
            global app
            app = Tk()
            app.title("Result")

            text_display_canvas = Canvas(app, width=720, height=440, bg="#000077")
            text_display_canvas.pack()

            check_button_ = Button(app, text="Menu", bg="black", fg="black", font="calibri 12",
                                   command=destroyReplace_Menu)
            check_button_.place(relx=0.45, rely=0.93)

            text = Text(text_display_canvas)
            text_display_canvas.create_window((80, 60), window=text, anchor='nw')

            with open("student.json") as config_file:
                data_file = json.load(config_file)

                for item in data_file["student"]:
                    if item["name"] == name:
                        for k in item:
                            text.insert("end", '{} = {}\n'.format(k, item[k]))

            result_display.destroy()
            app.mainloop()

    check_button = Button(result_display_frame, text="Search", bg="black", fg="black", font="calibri 12",
                          command=check_name_present)
    check_button.place(relx=0.45, rely=0.93)
    result_display.mainloop()


def destroyTable_Menu():
    table_display.destroy()
    end_menu()


def table():
    global table_display
    global store
    table_display = Tk()
    table_display.title(store + " rules")

    table_display_canvas = Canvas(table_display, width=720, height=440, bg="#000077")
    table_display_canvas.pack()

    table_display_frame = Frame(table_display_canvas, bg="#a9c5e4")
    table_display_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    value1 = Label(table_display_frame, text="Range of values to use (inclusive): " + str(data[store][0]["range"]),
                   bg="#7694e3", font=("oxygen", 25))
    value1.place()
    value1.pack(pady=15)

    value2 = Label(table_display_frame, text="Number of addition questions: " + str(data[store][0]["ques_add"]),
                   bg="#7694e3", font=("oxygen", 25))
    value2.place()
    value2.pack(pady=15)

    value3 = Label(table_display_frame, text="Number of subtraction questions: " + str(data[store][0]["ques_sub"]),
                   bg="#7694e3", font=("oxygen", 25))
    value3.place()
    value3.pack(pady=15)

    value4 = Label(table_display_frame, text="Number of multiplication questions: " + str(data[store][0]["ques_mul"]),
                   bg="#7694e3", font=("oxygen", 25))
    value4.place()
    value4.pack(pady=15)

    value5 = Label(table_display_frame, text="Number of attempts per questions: " + str(data[store][0]["attempt"]),
                   bg="#7694e3", font=("oxygen", 25))
    value5.place()
    value5.pack(pady=15)

    return_to = Button(table_display_frame, text="Menu", bg="black", fg="black", font="calibri 12", command=destroyTable_Menu)
    return_to.place(relx=0.45, rely=0.93)
    table_display.mainloop()


def find():
    global find_rule
    find_rule = Tk()
    find_rule.title("View the rules")

    find_rule_canvas = Canvas(find_rule, width=720, height=440, bg="#000077")
    find_rule_canvas.pack()

    find_rule_frame = Frame(find_rule_canvas, bg="#a9c5e4")
    find_rule_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    level = Label(find_rule_frame, text='Select your Difficulty Level !!', bg="#7694e3", font="calibri 18")
    level.place(relx=0.25, rely=0.3)

    var = IntVar()
    easyR = Radiobutton(find_rule_frame, text='Easy', bg="#a9c5e4", font="calibri 16", value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)

    mediumR = Radiobutton(find_rule_frame, text='Standard', bg="#a9c5e4", font="calibri 16", value=2, variable=var)
    mediumR.place(relx=0.25, rely=0.5)

    hardR = Radiobutton(find_rule_frame, text='Hard', bg="#a9c5e4", font="calibri 16", value=3, variable=var)
    hardR.place(relx=0.25, rely=0.6)

    def navigate():
        global store

        x = var.get()
        print(x)
        if x == 1:
            find_rule.destroy()

            store = "easy"

            table()

        elif x == 2:
            find_rule.destroy()

            store = "standard"
            table()

        elif x == 3:
            find_rule.destroy()
            store = "hard"
            table()
        else:
            pass

    go = Button(find_rule_frame, text="Go", bg="black", fg="black", font="calibri 12", command=navigate)
    go.place(relx=0.25, rely=0.8)
    find_rule.mainloop()


#   def add_rules():
#       key = input("The Rule: ").lower()
#        new_string = input("Value: ").lower()
#
#      data[key] = new_string
#
#       with open('rules.json', 'w') as f:
#            json.dump(data, f, indent=2)
#           end_menu()

def des_to_change():
    check_display.destroy()
    change()


def check():
    a = int(data[rep][0]["ques_add"])
    s = int(data[rep][0]["ques_sub"])
    m = int(data[rep][0]["ques_mul"])

    sum_rules = a + s + m
    if sum_rules != 10:
        global check_display
        check_display = Tk()
        check_display.title("Error " + rep)

        check_display_canvas = Canvas(check_display, width=720, height=440, bg="#000077")
        check_display_canvas.pack()

        check_display_frame = Frame(check_display_canvas, bg="#a9c5e4")
        check_display_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        value1 = Label(check_display_frame, text="The total question doesn't add up to 10 question", bg="#7694e3",
                       font=("oxygen", 25))
        value1.place()
        value1.pack(pady=15)

        value2 = Label(check_display_frame, text="Number of addition questions: " + str(data[rep][0]["ques_add"]),
                       bg="#7694e3", font=("oxygen", 25))
        value2.place()
        value2.pack(pady=15)

        value3 = Label(check_display_frame, text="Number of subtraction questions: " + str(data[rep][0]["ques_sub"]),
                       bg="#7694e3", font=("oxygen", 25))
        value3.place()
        value3.pack(pady=15)

        value4 = Label(check_display_frame, text="multiplication: " + str(data[rep][0]["ques_mul"]), bg="#7694e3",
                       font=("oxygen", 25))
        value4.place()
        value4.pack(pady=15)

        value5 = Label(check_display_frame, text="The total number of question : " + str(sum_rules), bg="#7694e3",
                       font=("oxygen", 25))
        value5.place()
        value5.pack(pady=15)

        change_to_ = Button(check_display_frame, text="Change", bg="black", fg="black", font="calibri 12",
                            command=des_to_change)
        change_to_.place(relx=0.25, rely=0.93)
        check_display.mainloop()

    else:
        print("the question add up to 10 question")
        messagebox.showinfo("Correct", "the questions add up to 10 question")  ##### it creates an empty file.. why??? ####
        end_menu()


def modify():
    global modify_display
    modify_display = Tk()
    modify_display.title("Modify " + rep)

    var = StringVar

    modify_display_canvas = Canvas(modify_display, width=720, height=440, bg="#000077")
    modify_display_canvas.pack()

    modify_display_frame = Frame(modify_display_canvas, bg="#a9c5e4")
    modify_display_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(modify_display_frame, text="Please enter the value for " + dis_name, fg="white", bg="#7694e3",
                    font=("", 25, "bold"))
    heading.place(relx=0.25, rely=0.2)

    current = Label(modify_display_frame, text="current value: " + str(data[rep][0][change_to]), fg="white",
                    bg="#7694e3",
                    font=("", 25, "bold"))
    current.place(relx=0.3, rely=0.35)

    label_ = Label(modify_display_frame, text="Value:", fg='white', bg='black')
    label_.place(relx=0.21, rely=0.5)

    user_value = Entry(modify_display_frame, bg='white', fg='black', textvariable=var)
    user_value.config(width=42)
    user_value.place(relx=0.31, rely=0.5)

    def check_value_present():
        try:
            if int(user_value.get()) == 0:
                error = Label(modify_display_frame, text="please enter the value", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)
                modify_display.update()
            else:
                print("current value: ", data[rep][0][change_to])

                modify_into = change_to
                value = int(user_value.get())
                data[rep][0][modify_into] = value

                with open('rules.json', 'w') as fi:
                    json.dump(data, fi, indent=2)
                modify_display.destroy()
                change()

        except ValueError:
            print("please use integer only")
            error = Label(text="Please enter Integer only", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)


    change_value = Button(modify_display_frame, text='Change', padx=5, pady=5, width=5, command=check_value_present,
                          fg="white", bg="black")
    change_value.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    change_value.place(relx=0.4, rely=0.6)
    modify_display.mainloop()


def change():
    global change_display
    change_display = Tk()
    change_display.title("change the rules for " + rep)

    change_display_canvas = Canvas(change_display, width=720, height=440, bg="#000077")
    change_display_canvas.pack()

    change_display_frame = Frame(change_display_canvas, bg="#a9c5e4")
    change_display_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    select = Label(change_display_frame, text='Change the rules for: ' + rep, bg="#7694e3", font="calibri 18")
    select.place(relx=0.25, rely=0.1)

    var = IntVar()
    change_range = Radiobutton(change_display_frame, text='Range of Values - Current: '+str(data[rep][0]["range"]), bg="#a9c5e4", font="calibri 16", value=1,
                               variable=var)
    change_range.place(relx=0.25, rely=0.2)

    change_add = Radiobutton(change_display_frame, text='Number of addition question - Current: '+str(data[rep][0]["ques_add"]), bg="#a9c5e4", font="calibri 16",
                             value=2, variable=var)
    change_add.place(relx=0.25, rely=0.3)

    change_sub = Radiobutton(change_display_frame, text='Number of subtraction question - Current: '+str(data[rep][0]["ques_sub"]), bg="#a9c5e4",
                             font="calibri 16", value=3, variable=var)
    change_sub.place(relx=0.25, rely=0.4)

    change_mul = Radiobutton(change_display_frame, text='Number of multiplication question - Current: '+str(data[rep][0]["ques_mul"]), bg="#a9c5e4",
                             font="calibri 16", value=4, variable=var)
    change_mul.place(relx=0.25, rely=0.5)

    change_attempt = Radiobutton(change_display_frame, text='Number of attempts per question - Current: '+str(data[rep][0]["attempt"]), bg="#a9c5e4",
                                 font="calibri 16", value=5, variable=var)
    change_attempt.place(relx=0.25, rely=0.6)

    to_quit = Radiobutton(change_display_frame, text='Quit', bg="#a9c5e4", font="calibri 16", value=6, variable=var)
    to_quit.place(relx=0.25, rely=0.7)

    def navigate():
        global change_to
        global dis_name
        x = var.get()
        print(x)
        if x == 1:
            change_display.destroy()
            change_to = "range"
            dis_name = "Range"
            modify()
        elif x == 2:
            change_display.destroy()
            change_to = "ques_add"
            dis_name = "Addition"
            modify()
        elif x == 3:
            change_display.destroy()
            change_to = "ques_sub"
            dis_name = "Subtraction"
            modify()
        elif x == 4:
            change_display.destroy()
            change_to = "ques_mul"
            dis_name = "Multiplication"
            modify()
        elif x == 5:
            change_display.destroy()
            change_to = "attempt"
            dis_name = "Attempt"
            modify()
        elif x == 6:
            change_display.destroy()
            with open('rules.json', 'w') as ff:
                json.dump(data, ff, indent=2)
            check()
        else:
            pass

    goto = Button(change_display_frame, text="Click", bg="black", fg="black", font="calibri 12", command=navigate)
    goto.place(relx=0.25, rely=0.8)
    change_display.mainloop()


def replace():
    global replace_display
    replace_display = Tk()
    replace_display.title("change the rules")

    replace_display_canvas = Canvas(replace_display, width=720, height=440, bg="#000077")
    replace_display_canvas.pack()

    replace_display_frame = Frame(replace_display_canvas, bg="#a9c5e4")
    replace_display_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    select = Label(replace_display_frame, text='What difficulties rules you want to change?', bg="#7694e3",
                   font="calibri 18")
    select.place(relx=0.25, rely=0.3)

    var = IntVar()

    easy_rules = Radiobutton(replace_display_frame, text='Easy', bg="#a9c5e4", font="calibri 16", value=1, variable=var)
    easy_rules.place(relx=0.25, rely=0.4)

    standard_rules = Radiobutton(replace_display_frame, text='Standard', bg="#a9c5e4", font="calibri 16", value=2,
                                 variable=var)
    standard_rules.place(relx=0.25, rely=0.5)

    hard_rules = Radiobutton(replace_display_frame, text='Hard', bg="#a9c5e4", font="calibri 16", value=3, variable=var)
    hard_rules.place(relx=0.25, rely=0.6)

    to_quit = Radiobutton(replace_display_frame, text='Quit', bg="#a9c5e4", font="calibri 16", value=4, variable=var)
    to_quit.place(relx=0.25, rely=0.7)

    def navigate():
        global rep
        x = var.get()
        print(x)
        if x == 1:
            replace_display.destroy()
            rep = "easy"
            change()
        elif x == 2:
            replace_display.destroy()
            rep = "standard"
            change()
        elif x == 3:
            replace_display.destroy()
            rep = "hard"
            change()
        elif x == 4:
            replace_display.destroy()
            end_menu()
        else:
            pass

    goto = Button(replace_display_frame, text="Click", bg="black", fg="black", font="calibri 12", command=navigate)
    goto.place(relx=0.25, rely=0.8)
    replace_display.mainloop()


def menu():
    global ask_display
    ask_display = Tk()
    ask_display.title("Menu")

    ask_canvas = Canvas(ask_display, width=720, height=440, bg="#000077")
    ask_canvas.pack()

    ask_frame = Frame(ask_canvas, bg="#a9c5e4")
    ask_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(ask_canvas, text=" P R O G R A M  F O R  T E A C H E R' S  O N L Y  ", fg="white", bg="#000077")
    wel.config(font=('oxygen', 25, "bold"))
    wel.place(relx=0.12, rely=0.01)

    select = Label(ask_frame, text='please Select the below option', bg="#7694e3", font="calibri 18")
    select.place(relx=0.25, rely=0.3)

    var = IntVar()
    find_rules = Radiobutton(ask_frame, text='View the rules', bg="#a9c5e4", font="calibri 16", value=1, variable=var)
    find_rules.place(relx=0.25, rely=0.4)

    change_rules = Radiobutton(ask_frame, text='Change the rules', bg="#a9c5e4", font="calibri 16", value=2,
                               variable=var)
    change_rules.place(relx=0.25, rely=0.5)

    quit_rules = Radiobutton(ask_frame, text='View result of a student', bg="#a9c5e4", font="calibri 16", value=3,
                             variable=var)
    quit_rules.place(relx=0.25, rely=0.6)

    quit_rules = Radiobutton(ask_frame, text='Quit', bg="#a9c5e4", font="calibri 16", value=4, variable=var)
    quit_rules.place(relx=0.25, rely=0.7)

    def navigate():

        x = var.get()
        print(x)
        if x == 1:
            ask_display.destroy()
            find()
        elif x == 2:
            ask_display.destroy()
            replace()

        elif x == 3:
            ask_display.destroy()
            result()
        elif x == 3:
            ask_display.destroy()
            quit()
        else:
            pass

    goto = Button(ask_frame, text="Click", bg="black", fg="black", font="calibri 12", command=navigate)
    goto.place(relx=0.25, rely=0.8)
    ask_display.mainloop()


def end_menu():
    global ask_again_display
    ask_again_display = Tk()
    ask_again_display.title("Menu")

    ask_again_canvas = Canvas(ask_again_display, width=720, height=440, bg="#000077")
    ask_again_canvas.pack()

    ask_again_frame = Frame(ask_again_canvas, bg="#a9c5e4")
    ask_again_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(ask_again_canvas, text=" P R O G R A M F O R T E A C H E R' S O N L Y  ", fg="white", bg="#000077")
    wel.config(font=('oxygen', 25, "bold"))
    wel.place(relx=0.1, rely=0.02)

    select = Label(ask_again_frame, text='Do you want to use the program again ?', bg="#7694e3", font="calibri 18")
    select.place(relx=0.25, rely=0.3)

    var = IntVar()
    find_rules = Radiobutton(ask_again_frame, text='YES', bg="#a9c5e4", font="calibri 16", value=1, variable=var)
    find_rules.place(relx=0.25, rely=0.4)

    change_rules = Radiobutton(ask_again_frame, text='NO', bg="#a9c5e4", font="calibri 16", value=0, variable=var)
    change_rules.place(relx=0.25, rely=0.5)

    def navigate():
        x = var.get()
        print(x)
        if x == 1:
            ask_again_display.destroy()
            menu()
        elif x == 0:
            ask_again_display.destroy()
        else:
            pass

    goto = Button(ask_again_frame, text="Click", bg="black", fg="black", font="calibri 12", command=navigate)
    goto.place(relx=0.25, rely=0.8)
    ask_again_display.mainloop()


menu()
