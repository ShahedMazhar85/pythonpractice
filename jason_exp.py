import json
'''
student = {}
# Key:value mapping
student['peter'] = {
    "Name": "Peter",
    "Roll_no": "0090014",
    "Grade": "A",
    "Age": 20
}

s = json.dumps(student)
with open("c://data//a.txt", "w") as f:
    f.write(s)
    '''
f=open("c://data//a.txt", "r")
s=f.read()
print(s)
print(type(s))
book=json.loads(s)
print(book)
print(type(book))

