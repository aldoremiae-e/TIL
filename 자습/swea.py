# ------------------------------- *예제* ---------------------------------
# members = [
#     {"name" : "홍길동", "age" : 20},
#     {"name" : "이순신", "age" : 45},
#     {"name" : "강감찬", "age" : 35},
# ]

# for member in members :
#     print("{0}\t{1}".format(member["name"],member["age"]))

# def create(name, age):
#     return {"name" : name, "age" : age}

# def to_str(person) : 
#     return "{0}\t{1}".format(person["name"],person["age"])

# members = [
#     create("홍길동", 20),
#     create("이순신", 45),
#     create("강감찬", 35) 
# ]

# for member in members : 
#     print(to_str(member))

#------------------------------ *연습문제 1 * -----------------------------

# class Student :
#     def __init__(self, kor, eng, math) :
#         self.__kor = kor
#         self.__eng = eng
#         self.__math = math

#     @property
#     def kor(self):
#         return self.__kor

#     @property
#     def eng(self):
#         return self.__eng

#     @property
#     def math(self):
#         return self.__math

#     def sum(self):
#         return "국어, 영어, 수학의 총점: {0}".format(self.__kor + self.__eng + self.__math)

# score = list(map(int,input().split(', ')))
# student_score = Student(score[0],score[1],score[2])
# print(student_score.sum())

#------------------------------ *연습문제 2 * -----------------------------

# class Korean :
#     @staticmethod
#     def printNationality():
#         return "대한민국"

# for i in range(0,2) :
#     print(Korean.printNationality())

#------------------------------ *연습문제 3 * -----------------------------
# 
class Parent:
    def __init__(self,name):
        self.__name = name

    @property
    def f_name(self):
        return self.__name

    def __repr__(self):
        return "이름: {0}".format(self.__name)

class Child(Parent):
    def __init__(self, name, major):
        Parent.__init__(self, name)
        self.__major = major
    
    @property
    def major(self):
        return self.__major
    
    def __repr__(self):
        return Parent.__repr__(self) + ', 전공: {0}'.format(self.__major)

a = Parent('홍길동')
b = Child('이순신', '컴퓨터')
print(a)
print(b)

