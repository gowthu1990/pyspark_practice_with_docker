class Student():
    name = ""
    rollno = 0

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def get_name(self):
        return self.name
    
    def get_rollno(self):
        return self.rollno

if __name__ == "__main__":
    print("Execution starts here..")

    student = Student("Hari", 100)
    print(f"Student={student.get_name()} {student.get_rollno()}")


