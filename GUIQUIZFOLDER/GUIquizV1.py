from tkinter import *
import random

names = []
asked = []
score = 0

# Dictionary containing questions and their respective answers
questions_answers = {
    1: ["What is the purpose of a budget?",
        'To track your spending',
        'To limit your spending',
        'To plan for future expenses',
        1],
    2: ["How does compound interest work?",
        'Interest on the initial amount only',
        'Interest on the initial amount plus previously earned interest',
        'Interest on the latest deposit only',
        2],
    3: ["What is the difference between a debit card and a credit card?",
        'Debit card deducts money directly from your account',
        'Credit card allows borrowing with interest',
        'Debit card is for online purchases, and credit card is for in-person purchases',
        1],
    4: ["Why is it important to have an emergency fund?",
        'To cover regular monthly expenses',
        'To be prepared for unexpected expenses',
        'To earn more interest',
        2],
    5: ["What is the concept of 'pay yourself first'?",
        'Save a portion of your income before spending',
        'Pay off debts first before saving',
        'Spend all your income and save whatever is left',
        1],
    6: ["What is the role of a credit score?",
        'Determines how much you can borrow',
        'Measures your ability to save money',
        'Reflects the number of purchases youve made',
        1],
    7: ["How does inflation affect purchasing power?",
        'Increases it',
        'Decreases it',
        'Has no effect on it',
        2],
    8: ["What is the difference between a stock and a bond?",
        'Stock represents ownership in a company, while a bond is a loan to a company or government',
        'Stock and bond are terms used interchangeably',
        'Stock and bond both represent ownership in a company',
        1],
    9: ["Why is diversification important in investing?",
        'Reduces risk by spreading investments across different assets',
        'Concentrates investments in a single asset for higher returns',
        'Diversification is not important in investing',
        1],
    10: ["What is the difference between simple and compound interest?",
          'Simple interest is earned on the initial amount only',
          'Compound interest is earned on both the initial amount and previously earned interest',
          'Simple interest is earned at a higher rate than compound interest',
          1],
}

def randomiser():
    """Selects a random question number."""
    global qnum
    qnum = random.randint(1, 10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

class QuizStarter:
    def __init__(self, parent):
        background_color = "OldLace"

        # Frame setup
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        # Heading label
        self.heading_label = Label(self.quiz_frame, text="Financial Education Quiz", font=("Times New Roman", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0, padx=20)

        self.var1 = IntVar()

        # Username label
        self.user_label = Label(self.quiz_frame, text="Please enter your username below:", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)

        # Entry box for username
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        # Continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)

    def name_collection(self):
        """Collects username and starts the quiz."""
        name = self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        Quiz(root)

class Quiz:
    def __init__(self, parent):
        background_color = "OldLace"

        # Frame setup
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        randomiser()

        # Question label
        self.question_label = Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Times New Roman", "18", "bold"), bg=background_color)
        self.question_label.grid(row=0, padx=20)

        self.var1 = IntVar()

        # Radio buttons (four consistent options)
        self.rb1 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], variable=self.var1, value=1, indicator=0, background="light blue")
        self.rb1.grid(row=1, sticky=W)

        self.rb2 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], variable=self.var1, value=2, indicator=0, background="light blue")
        self.rb2.grid(row=2, sticky=W)

        self.rb3 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], variable=self.var1, value=3, indicator=0, background="light blue")
        self.rb3.grid(row=3, sticky=W)

       # Confirm button
        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="red", command=self.test_progress)
        self.confirm_button.grid(row=5)

        # Score label
        self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color)
        self.score_label.grid(row=7, pady=1)

    def questions_setup(self):
        """Sets up the next question."""
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        

    def test_progress(self):
        """Checks user's answer and progresses through the quiz."""
        global score
        scr_label = self.score_label
        choice = self.var1.get()
        
        if len(asked) > 9:
            if choice == questions_answers[qnum][4]:
                score += 1
                scr_label.configure(text=score)
                self.confirm_button.config(text="Confirm")
            else:
                # Display correct answer
                scr_label.configure(text="The correct answer was: " + questions_answers[qnum][questions_answers[qnum][4]])
                self.confirm_button.config(text="Confirm")
        else:
            if choice == questions_answers[qnum][4]:
                score += 1
                scr_label.configure(text=score)
                self.confirm_button.config(text="Confirm")
                self.questions_setup()
            else:
                scr_label.configure(text="The correct answer was: " + questions_answers[qnum][questions_answers[qnum][4]])
                self.confirm_button.config(text="Confirm")
                self.questions_setup()

randomiser()

if __name__ == "__main__":
    root = Tk()
    root.title("Financial Education Quiz")
    quiz_instance = QuizStarter(root)
    root.mainloop()
