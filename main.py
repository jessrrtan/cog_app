import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Radiobutton
import sqlite3
import datetime

# connection = sqlite3.connect("users.db")
# cursor = connection.cursor()
#
# create_phq_table_query = """
# CREATE TABLE IF NOT EXISTS phq (
#     id INTEGER PRIMARY KEY,
#     date TEXT,
#     score INTEGER
# )
# """
#
# cursor.execute(create_phq_table_query)
#
# create_gad_table_query = """
# CREATE TABLE IF NOT EXISTS gad (
#     id STRING,
#     date TEXT,
#     score INTEGER
# )
# """
# cursor.execute(create_gad_table_query)
#
# create_mood_table_query = """
# CREATE TABLE IF NOT EXISTS mood (
#     id STRING,
#     date TEXT,
#     score INTEGER
# )
# """
# cursor.execute(create_mood_table_query)

root = tk.Tk()
root.geometry("550x300")
root.title("Welcome Page")

# writes user id to users.txt
# def onClick_submit():
#     id = userID_entry.get()
#     with open('users.txt', 'w') as file:
#         file.write(f"User id: {id}")
#     print("user recorded")

# verifies if user wants to exit an assessment without submitting results
def onClick_home(window):
    answer = tk.messagebox.askquestion("Do you wish to proceed?","Going home without submitting will result in your answers being lost.\nDo you wish to proceed?")
    if answer == 'yes':
        window.destroy()


# provides description of assessments
def onClick_info(assessment):
    if assessment=="phq":
        tk.messagebox.showinfo("title","What is the PHQ-9?\n\nThe PHQ-9 is an assessment that helps clinicians diagnose depression")
    elif assessment=="gad":
        tk.messagebox.showinfo("title","What is the GAD-7?\n\nThe GAD-7 is an assessment that helps clinicians diagnose anxiety")
    elif assessment=="mood":
        tk.messagebox.showinfo("title","Use the slider bar to indicate your mood.\nOr you can enter a number in the netry box.\nRefer to the legend for the emotion value of the numbers")



# creates new window for phq assessments
def create_phq_assessment_window():
    extra_window = tk.Toplevel()
    extra_window.title('PHQ Assessment')
    extra_window.geometry('1000x1000')
    var = tk.IntVar(value=0)

    phq_questions = ["Little interest or pleasure in doing things",
                    "Feeling down, depressed, or hopeless",
                    "Trouble falling or staying asleep, or sleeping too much",
                    "Feeling tired or having little energy",
                    "Poor appetite or overeating",
                    "Feeling bad about yourself - or that you are a failure or have let yourself or your family down",
                    "Trouble concentrating on things, such as reading the newspaper or watching television",
                    "Moving or speaking so slowly that other people could have noticed.\n Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual",
                    "Thoughts that you would be better off dead, or of hurting yourself in some way"]

    title_frame = tk.Frame(extra_window)
    title_frame.pack(fill=tk.X)

    exit_button = tk.Button(title_frame,text="Home",command=lambda:onClick_home(extra_window))
    exit_button.pack(side=tk.LEFT)

    left_spacer = tk.Frame(title_frame)
    left_spacer.pack(side=tk.LEFT, expand=True, fill=tk.X)

    assessment_text = tk.Label(title_frame, text="Over the last 2 weeks, how often have you been bothered by any of the following problems?",font='Helvetica 14 bold')
    assessment_text.pack(side=tk.LEFT)

    right_spacer = tk.Frame(title_frame)
    right_spacer.pack(side=tk.LEFT, expand=True, fill=tk.X)

    info_button = tk.Button(title_frame,text="?",command=lambda:onClick_info("phq"))
    info_button.pack(side=tk.RIGHT)



    phq_values = []
    for idx,question in enumerate(phq_questions):
        var = tk.IntVar(value=0)
        phq_values.append(var)

        question_frame = tk.Frame(extra_window,pady=10)
        question_frame.pack()

        label = tk.Label(question_frame,text=question)
        label.pack()

        for option_value,option_text in zip([0,1,2,3],["Not at all", "Several days", "More than half the days", "Nearly every day"]):
            rb = tk.Radiobutton(question_frame,text=option_text, variable=var, value=option_value)
            rb.pack(side=tk.LEFT)

# verifies if user wants to submit results
    def assessment_submit():
        proceed = tk.messagebox.askquestion("title","Individual answers will have to be re-entered if you want to edit them. Do you wish to proceed?")
        if proceed == 'yes':
            phq_sum = 0
            answers = [var.get() for var in phq_values]
            for val in phq_values:
                phq_sum += val.get()

            # insert_statement = ("INSERT INTO phq (id, date, score)"
            #                     "VALUES (?,?,?)")
            # data = (id_entry, datetime.datetime.now(),phq_sum)
            # cursor.execute(insert_statement,data)

            tk.messagebox.showinfo("Total score", f"Your total score is {phq_sum}")
        elif proceed == 'no':
            pass

    # id_entry_label = tk.Label(extra_window,text="Please enter your user ID")
    # id_entry_label.pack()
    # id_entry = tk.Entry(extra_window)
    # id_entry.pack()
    assessment_submit_button = ttk.Button(extra_window, text="Submit",command=assessment_submit)
    assessment_submit_button.pack()


# creates new window for gad assessments
def create_gad_assessment_window():
    extra_window = tk.Toplevel()
    extra_window.title('GAD Assessment')
    extra_window.geometry('1000x1000')
    var = tk.IntVar(value=0)

    gad_questions = ["Feeling nervous, anxious, or on edge",
                     "Not being able to stop or control worrying",
                     "Worrying too much about different things",
                     "Trouble relaxing",
                     "Being so restless that it's hard to sit still",
                     "Becoming easily annoyed or irritable",
                     "Feeling afraid as if something awful might happen"]

    title_frame = tk.Frame(extra_window)
    title_frame.pack(fill=tk.X, padx=10, pady=10)

    exit_button = tk.Button(title_frame,text="Home",command=lambda:onClick_home(extra_window))
    exit_button.pack(side=tk.LEFT)

    left_spacer = tk.Frame(title_frame)
    left_spacer.pack(side=tk.LEFT, expand=True, fill=tk.X)

    assessment_text = tk.Label(title_frame, text="Over the last 2 weeks, how often have you been bothered by any of the following problems?",font='Helvetica 14 bold')
    assessment_text.pack(side=tk.LEFT)

    right_spacer = tk.Frame(title_frame)
    right_spacer.pack(side=tk.LEFT, expand=True, fill=tk.X)

    info_button = tk.Button(title_frame,text="?",command=lambda:onClick_info("gad"))
    info_button.pack(side=tk.RIGHT)

    gad_values = []
    for idx,question in enumerate(gad_questions):
        var = tk.IntVar(value=0)
        gad_values.append(var)

        question_frame = tk.Frame(extra_window,pady=10)
        question_frame.pack()

        label = tk.Label(question_frame,text=question)
        label.pack()



        for option_value,option_text in zip([0,1,2,3],["Not at all", "Several days", "More than half the days", "Nearly every day"]):
            rb = tk.Radiobutton(question_frame,text=option_text, variable=var, value=option_value)
            rb.pack(side=tk.LEFT)

# verifies if user wants to submit results
    def assessment_submit():
        proceed = tk.messagebox.askquestion("title","Individual answers will have to be re-entered if you want to edit them. Do you wish to proceed?")
        if proceed == 'yes':
            gad_sum = 0
            answers = [var.get() for var in gad_values]
            for val in gad_values:
                gad_sum += val.get()
            tk.messagebox.showinfo("Total Score", f"Your total score is {gad_sum}")
        elif proceed == 'no':
            pass

    # id_entry_label = tk.Label(extra_window,text="Please enter your user ID")
    # id_entry_label.pack()
    # id_entry = tk.Entry(extra_window)
    # id_entry.pack()

    assessment_submit_button = ttk.Button(extra_window,text="Submit",command=assessment_submit)
    assessment_submit_button.pack()


# creates new window for mood tracker
def create_mood_window():
    extra_window = tk.Toplevel()
    extra_window.title('Mood Tracker')
    extra_window.geometry("400x400")

    title_frame = tk.Frame(extra_window)
    title_frame.pack(fill=tk.X)

    exit_button = tk.Button(title_frame,text="Home",command=lambda:onClick_home(extra_window))
    exit_button.pack(side=tk.LEFT)

    # left_spacer = tk.Frame(title_frame)
    # left_spacer.pack(side=tk.LEFT, expand=True, fill=tk.X)
    #
    # assessment_text = tk.Label(title_frame, text="Over the last 2 weeks, how often have you been bothered by any of the following problems?",font='Helvetica 14 bold')
    # assessment_text.pack(side=tk.LEFT)
    #
    # right_spacer = tk.Frame(title_frame)
    # right_spacer.pack(side=tk.LEFT, expand=True, fill=tk.X)

    info_button = tk.Button(title_frame,text="?",command=lambda:onClick_info("mood"))
    info_button.pack(side=tk.RIGHT)

    legend = tk.Label(extra_window,text="0=angry, frustrated, anxious\n1=sad, lonely, insecure\n2=sick, tired, unmotivated\n3=average, normal, good\n4=productive, energetic, active\n5=happy, content, joyful")
    legend.pack()

    slider = tk.Scale(extra_window,from_=0, to=5, orient='horizontal',length=300)
    slider.pack()

    # mood_button_1 = tk.Button(extra_window, text='Submit',command=lambda: submit(slider.get()))
    # mood_button_1.pack()

    enter_mood_text = tk.Label(extra_window,text="Alternatively, you can enter a number from 0 to 5")
    enter_mood_text.pack()
    enter_mood = tk.Entry(extra_window)
    enter_mood.pack()

    def submit(value):
        tk.messagebox.showinfo("title",f"You submitted a score of {value}")


    # id_entry_label = tk.Label(extra_window,text="Please enter your user ID")
    # id_entry_label.pack()
    # id_entry = tk.Entry(extra_window)
    # id_entry.pack()

    if enter_mood.get():
        val = enter_mood.get()
    else:
        val= slider.get()

    mood_button_2 = tk.Button(extra_window, text='Submit',command=lambda: submit(enter_mood.get() if enter_mood.get() else slider.get()))
    mood_button_2.pack()




welcome_text = tk.Label(root, text="Welcome to the Mind Hub App\nHere, you can take mental health assessments and track your mood\nPlease take the PHQ-9 assessment and the GAD-7 assessment then track your mood")
welcome_text.grid(row=0,column=0,columnspan=3)

# userID_entry_label = tk.Label(root, text = "If you don't have an existing user ID, please enter a user ID: ")
# userID_entry = tk.Entry(root, width=20)
# submit_button = tk.Button(root, text="Submit", command=onClick_submit)

nav_to_phq_assessment = ttk.Button(root, text="Take PHQ-9 Assessment", command=create_phq_assessment_window)
nav_to_gad_assessment = ttk.Button(root, text="Take GAD-7 Assessment", command=create_gad_assessment_window)
nav_to_moodtracker = ttk.Button(root, text="Track Your Mood", command=create_mood_window)


welcome_text.grid(row=0,column=0)
# userID_entry_label.grid(row=2,column=0)
# userID_entry.grid(row=2,column=1)
# submit_button.grid(row=2,column=2)
nav_to_phq_assessment.grid(row=3,column=0,columnspan=3)
nav_to_gad_assessment.grid(row=4,column=0,columnspan=3)
nav_to_moodtracker.grid(row=5,column=0,columnspan=3)



root.mainloop()


cursor.execute("PRAGMA table_info(phq);")
columns = cursor.fetchall()
for column in columns:
    print(column)  # This will print out the column details

connection.close()