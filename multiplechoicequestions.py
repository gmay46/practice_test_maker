import random
import tkinter as tk
from question_bank import question_list 

class MultipleChoiceQuestion(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.current_question = 0
        self.question = questions[self.current_question][0]
        self.choices = questions[self.current_question][1]
        self.correct_answer = self.choices[questions[self.current_question][2]]
        self.selected_answer = tk.StringVar()
        self.correct_count = 0
        self.incorrect_count = 0
        self.create_widgets()

    def create_widgets(self):
        self.title("Study questions")
        
        self.label_question = tk.Label(self, text=str(self.current_question + 1) +": " + self.question, wraplength=512, justify="center")
        self.label_question.pack()


        self.radio_button1 = tk.Radiobutton(self, text=self.choices[0], variable=self.selected_answer, value=self.choices[0])
        self.radio_button2 = tk.Radiobutton(self, text=self.choices[1], variable=self.selected_answer, value=self.choices[1])
        self.radio_button3 = tk.Radiobutton(self, text=self.choices[2], variable=self.selected_answer, value=self.choices[2])
        self.radio_button4 = tk.Radiobutton(self, text=self.choices[3], variable=self.selected_answer, value=self.choices[3])

        self.radio_button1.pack(anchor=tk.W)
        self.radio_button2.pack(anchor=tk.W)
        self.radio_button3.pack(anchor=tk.W)
        self.radio_button4.pack(anchor=tk.W)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.result_text = tk.Text(self, height=30, width=256)
        self.result_text.pack()

        
    

    def display_question(self):
            
            self.question = questions[self.current_question][0]
            self.label_question.config(text = str(self.current_question + 1) +": " +self.question)

            new_choices = questions[self.current_question][1]
            self.radio_button1.config(text = new_choices[0], value = new_choices[0])
            self.radio_button2.config(text = new_choices[1], value = new_choices[1])
            self.radio_button3.config(text = new_choices[2], value = new_choices[2])
            self.radio_button4.config(text = new_choices[3], value = new_choices[3])


            self.correct_answer = new_choices[questions[self.current_question][2]]


    def end_times(self):
            self.result_text.insert(tk.END, "\nNo More Questions!")
            self.result_text.insert(tk.END, "\nCorrect Answers: " + str(self.correct_count))
            self.result_text.insert(tk.END, "\nIncorrect Answers: " + str(self.incorrect_count))
            self.result_text.insert(tk.END, "\npercent/grade: " + str((int(self.correct_count)/len(trimmed_questions))*100))
            self.submit_button.config(state=tk.DISABLED)
            return        

    def check_answer(self):
        selected_answer = self.selected_answer.get()
        
        if selected_answer == self.correct_answer:
            self.correct_count += 1
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Correct Answer!\n\n")
            self.result_text.insert(tk.END, f"Previous Question:\n{self.question}\n\n")
            self.result_text.insert(tk.END, f"Previous Correct Answer:\n{self.correct_answer}\n")

            if self.current_question < (len(trimmed_questions) -1):
                self.current_question += 1
                self.display_question()
                
            else:
                self.end_times()
        else:
            self.incorrect_count += 1
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Wrong Answer! Correct answer was: \"{self.correct_answer}\"\n\n")
            self.result_text.insert(tk.END, f"Previous Question:\n{self.question}\n\n")
            self.result_text.insert(tk.END, f"Previous Correct Answer:\n{self.correct_answer}\n")

            if self.current_question < (len(trimmed_questions) -1):
                self.current_question += 1

                self.display_question()
            else:
                self.end_times()



if __name__ == "__main__":
    

    questions = []
    questions.extend(question_list)
    random.shuffle(questions)
    trimmed_questions = []

    if len(questions) < 90:
        questions_count = len(questions)
    else:
        questions_count = 90

    for x in range(questions_count):     #change the number in range(x) to be the number of questions you want
        trimmed_questions.append(questions[x])

    app = MultipleChoiceQuestion(trimmed_questions)
    window_width = 1920 // 2
    window_height = 1080 // 2
    app.geometry(f"{window_width}x{window_height}")
    app.mainloop()
