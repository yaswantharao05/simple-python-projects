from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title('Quiz (True/False)')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {self.score}', font=('Arial', 12, 'bold'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150, 125, width=300,  # a width less than canvas width is given to
                                                # adjust words in canvas
                                                text='Questions come here',
                                                font=('Courier', 20, 'italic'),
                                                fill='black')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file=r'\images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button_func)
        self.true_button.grid(row=3, column=0)

        false_img = PhotoImage(file=r'\images\false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button_func)
        self.false_button.grid(row=3, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            new_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question, text=new_question, fill='black')
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of Quiz!", fill='black')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def check_answer(self, answer: str):
        self.canvas.itemconfig(self.question, fill='white')
        if self.quiz_brain.check_answer(answer):
            self.canvas.config(bg='green')
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.canvas.config(bg='red')

    def true_button_func(self):
        self.check_answer('true')
        self.window.after(1000, self.next_question)

    def false_button_func(self):
        self.check_answer('false')
        self.window.after(1000, self.next_question)
