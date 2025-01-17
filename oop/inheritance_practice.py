#Base Class

class Employee:
  def __init__(self, name, department, job_title):
    self._name = name
    self._department = department
    self._job_title = job_title
    # Add a method to show the details of an instance of the Employee class
    def employee_details(self):
       return f"Name: {self._name}, Department: {self._department}, Job Title: {self._job_title}"
    
# Create a class called programmer that inherits from the Employee class
class Programmer(Employee):
  def __init__(self, name, department, role):
    # Inherit from the Employee class
    super().__init__(name, department, "Programmer")
    self.role = role

    # Add getters & setters to the Programmer class
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    # Add a method to show details of the Programmer class
    def programmer_details(self):
      return f"Name: {self._name}, Department: {self._department}, Job Title: {self._job_title}, Role: {self.role}"

# Use the G&S methods to update the information of your Programmer

Employee1 = Programmer(name="Alice", department="Engineering", role="Backend Developer")

Employee1.name = "Ada"

# Display the updated information

print(Employee1.name)
Employee1.role = "Frontend Developer"

print(Employee1.role)