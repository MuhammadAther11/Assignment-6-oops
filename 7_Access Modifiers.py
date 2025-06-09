class Employee:
    
    def __init__(self, name, salary ,ssn):
        self.name = name # public
        self._salary = salary # protected
        self.__snn = ssn # private

emp = Employee("John", 50000, "123-45-6789")

print(emp.name)
print(emp._salary)
# print(emp.__ssn)  
print(emp._Employee__snn) # Accessing private variable using name mangling