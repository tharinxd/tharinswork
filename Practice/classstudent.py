from tkinter import*

class Student:

    def __init__(self, name):
        self.name = name
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade

def show_grade ():
    grade_label.config(text=csc_2[0].get_grade())

csc_2 =[]

csc_2.append(Student("Bilal"))
csc_2[0].set_grade("Not Achived")

window = Tk()
window.geometry("400x400")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()