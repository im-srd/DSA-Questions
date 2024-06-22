# class Student:
#     name = 'shyam ranjan dubey'
#     def __init__(self,name):
#         self.name = name

# s1 = Student('Shyam')
# print(s1.name)
# del s1
# # print(s1.name)
# print(Student.name)

class Student:
    def __init__(self, p, c, m):
        self.physics = p
        self.chemistry = c
        self.math = m
        # self.percentage = (self.physics + self.chemistry + self.math) / 3
    
    @property # its like pehle percentage change nahi horha tha jab hm chemisry ka marks change kar rhe the, so we use property decorator, to keep chaanging the attributes if some changes were made 
    def percentage(self):
        return (self.physics + self.chemistry + self.math) / 3

s1 = Student(96,97,98)
print(s1.percentage)
s1.chemistry = 62
print(s1.percentage)