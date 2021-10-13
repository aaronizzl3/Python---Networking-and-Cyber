
# TODO: Student Class which has a profile, can add/remove test scores

# Class Definition
class Student:
    # Class Attributes
    Name = None
    Gender = None
    Age = None
    Course = None
    TargetGrade = None
    TestScores = []

    # Class Constructor
    def __init__(self, Name, Gender, Age, Course="Computing", TargetGrade="Distinction"):
        self.Name = Name
        self.Gender = Gender
        self.Age = Age
        self.Course = Course
        self.TargetGrade = TargetGrade

    # Class Methods
    def student_profile(self):
        print(f"Name: {self.Name}\nGender: {self.Gender}\nAge: {self.Age}")

    # Add a Test Score - add a score, and then print out average score
    def add_score(self, score):
        self.TestScores.append(score)
        print(f"The average score is {sum(self.TestScores) / len(self.TestScores)}")


MyStudent = Student("Aaron H", "Male", "27")
MyStudent.student_profile()
MyStudent.add_score(65)
MyStudent.add_score(35)