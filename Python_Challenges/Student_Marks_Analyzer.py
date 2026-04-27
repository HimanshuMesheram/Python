class StudentMarksAnalyzer:

    def __init__(self):
        self.students = {}

    def add_student(self):

        while True:
            name = input("Enter name of students or done: ").strip()

            if name.lower() == 'done':
                break

            if name in self.students:
                print("Name already exist")
                continue

            try:
                marks = int(input("Enter marks: "))
                self.students[name] = marks
            except ValueError:
                print("Enter valid integer")
        
        self.display_student()

    def display_student(self):

            if not self.students:
                print("No student data available.")
                return
            
            total_student = len(self.students)
            total_marks = sum(self.students.values())
            average = total_marks / total_student

            highest_marks = max(self.students.values())
            lowest_marks = min(self.students.values())

            highest_student = [name for name, marks in self.students.items() if marks == highest_marks]
            lowest_student = [name for name, marks in self.students.items() if marks == lowest_marks] 

            print("\n" + "="*40)
            print("       STUDENT MARKS REPORT")
            print("="*40)

            print(f"Total Students     : {total_student}")
            print(f"Average Marks      : {average:.2f}")

            print(f"\nHighest Marks      : {highest_marks}")
            print(f"Topper(s)          : {', '.join(highest_student)}")

            print(f"\nLowest Marks       : {lowest_marks}")
            print(f"Lowest Scorer(s)   : {', '.join(lowest_student)}")

            print("="*40)


stud = StudentMarksAnalyzer()
stud.add_student()
        
