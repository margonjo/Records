#Marc Gonzalez
#29/01/15
#1.1

class StudentMarks:
    def __init__(self):

        self.studentName = ""
        self.testMark = int()


new_student = StudentMarks()


new_student.studentName = input("please enetr student name: ")

new_student.testMark = int(input("please eneter the test score for this student: "))


print("The student {0} has achieved a score of  {1} well done".format(new_student.studentName, new_student.testMark))
