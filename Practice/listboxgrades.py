from tkinter import *

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # Use a dictionary to store grades for different subjects

    def get_grades(self):
        return self.grades

    def set_grade(self, subject, grade):
        self.grades[subject] = grade

def show_grades(event):
    selected_index = name_listbox.curselection()
    if selected_index:
        selected_student = csc_2[selected_index[0]]
        grades = selected_student.get_grades()
        grade_label.config(text=f"Grades for {selected_student.name}:\n{grades}")

csc_2 = []

# Creating students and setting individual grades for each subject
student1 = Student("Bilal")
student1.set_grade("Science", "Merit")

student2 = Student("Rehaan")
student2.set_grade("Math", "Not Achived")
student2.set_grade("French", "Excellence")

student3 = Student("Abdi")
student3.set_grade("Math", "Excellence")
student3.set_grade("English ", "Excellence")

csc_2.extend([student1, student2, student3])

window = Tk()
window.geometry("500x500")

name_listbox = Listbox(window)
for student in csc_2:
    name_listbox.insert(END, student.name)

name_listbox.pack()

grade_label = Label(window, justify=LEFT)
grade_label.pack()

name_listbox.bind("<Double-Button-1>", show_grades)

window.mainloop()
