class Student:
    def __init__(self, name, age, grade, height):
        self.name = name  
        self.age = age   
        self.grade = grade  
        self.height = height  

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Height: {self.height}cm"

    def update_grade(self, new_grade):
        self.grade = new_grade  


student1 = Student("John", 20, "A", 171)


print(student1.name)  
print(student1.age)   
print(student1.grade) 


print(student1)  

# Updating the grade
student1.update_grade("A+")
student1.grade = "B"
print(student1)  