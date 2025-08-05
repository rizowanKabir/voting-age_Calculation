class employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show(self):
        print("Role=",self.role,"Department=",self.department,"Salary=",self.salary)

class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Accounties","finance","2000000")



obj = engineer("Rizowan","25")
obj.show()