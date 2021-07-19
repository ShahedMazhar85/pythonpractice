Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
print("Enter the details of the new employee....");
Employee["Name"] = input("Name: ");
Employee["Age"] = int(input("Age: "));
Employee["salary"] = int(input("Salary: "));
Employee["Company"] = input("Company:");
print("printing the new data");
print(Employee)

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
print("Deleting some of the employee data")
del Employee["Name"]
del Employee["Company"]
print("printing the modified information ")
print(Employee)
print("Deleting the dictionary: Employee")
del Employee
print("Lets try to print it again ")
print(Employee)

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
for x in Employee:
    print(x)

    Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
    for x in Employee:
        print('Key:{} Value:{}'.format(x, Employee[x]))

        Integer = 10;
        Float = 1.290
        String = "Devansh"
        print("Hi I am Integer ... My value is %d\n"
              "Hi I am float ... My value is %f\nHi "
              "I am string ... My value is %s" % (Integer, Float, String))
Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print("Name : %s" % Employee["Name"])
print("Age : %d" % Employee["Age"])
print("Salary : %d" % Employee["salary"])
print("Company : %s" % Employee["Company"])
