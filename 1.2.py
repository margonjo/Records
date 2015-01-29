#Marc Gonzalez
#29/01/15
#1.1

class StudentMarks:
    def __init__(self):

        self.Name = ""
        self.Mark = int()


test_scores = []


for student in range(3):
    
    new_student = StudentMarks()
    new_student.Name = input("please enter student name: ")
    new_student.Mark = int(input("please eneter the test score for this student: "))
    test_scores.append(new_student)

for person in test_scores:
    print("The student {0} has achieved a score of  {1} well done".format(person.Name, person.Mark))

    






