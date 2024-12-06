from os import curdir
from tkinter import SEL


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades.keys():
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Ошибка'

    def st_mean(self):
        mean = 0
        for key in self.grades.keys():
            mean = mean + sum(self.grades[key]) / len(self.grades[key])
        mean = mean / len(self.grades.keys())
        return mean

    def compare(self, st):
        if self.st_mean() < st.st_mean():
            print(self.name, "хуже", st.name)
        elif self.st_mean() == st.st_mean():
            print(st.name, "равны c", self.name)
        else:

            print(st.name, "лучше", self.name)

    def get_instances(self):
        return list(self.__instances.values())

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.st_mean()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.check = []

        self.courses_attached = []
        self.grades = {}

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.lect_mean()}"

    def lect_mean(self):
        mean_self = 0

        for key in self.grades.keys():
            mean_self = mean_self + sum(self.grades[key]) / len(self.grades[key])
            mean_self = mean_self / len(self.grades.keys())
        return mean_self

    def compare(self, lect):
        if self.lect_mean() < lect.lect_mean():
            print(self.name, "хуже", lect.name)
        elif self.lect_mean() == lect.lect_mean():
            print(lect.name, "равны c", self.name)
        else:

            print(lect.name, "лучше", self.name)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.check = []
        self.courses_attached = []
        self.grades = {}

    def get_courses(self):
        return self.courses_attached

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

    def get_name(self):
        return self.name


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 5, 9, 10]
best_student.grades['Python'] = [10, 4]
best_student1 = Student('Rslan', 'Emin', 'your_gender')
best_student1.finished_courses += ['Git']
best_student1.courses_in_progress += ['Python']
best_student1.grades['Git'] = [3, 2, 5, 9, 10]
best_student1.grades['Python'] = [8, 7]

print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.name)
cool_mentor = Lecturer('Somes', 'Buddys')

cool_mentor.courses_attached += ['SQL']
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached, cool_mentor.name)
best_student.rate(cool_mentor, 'Python', 1)
print(cool_mentor.grades)

second_student = Student('Ruslan', 'Emin', 'male')
second_student.finished_courses += ['Git']
second_student.courses_in_progress += ['Python']
second_student.rate(cool_mentor, 'Python', 9)
revisor = Reviewer('Revisor', 'No1')
print("__STR__Reviewer")
print(revisor)
print("__STR__lect")

print(cool_mentor)
print("__STR__Student")

print(best_student)

cool_mentor1 = Lecturer('Ruslan', 'M')

cool_mentor1.courses_attached += ['SQL']
cool_mentor1.courses_attached += ['Python']
print(cool_mentor1.courses_attached, cool_mentor1.name)
best_student.rate(cool_mentor1, 'Python', 1)
print(cool_mentor1.grades)

second_student.courses_in_progress += ['Python']
second_student.rate(cool_mentor1, 'Python', 9)
revisor = Reviewer('Revisor', '1')
# print(cool_mentor.lect_mean())
cool_mentor.compare(cool_mentor1)
best_student.compare(best_student1)


def mean_student_and_course(st_list, course):
    mean = 0
    for st in st_list:
        if course in st.finished_courses or course in st.courses_in_progress:
            mean = mean + sum(st.grades[course]) / len(st.grades[course])
    print(mean / len(st_list))
    return mean / len(st_list)


def mean_lect_and_course(lect_list, course):
    mean = 0
    for lect in lect_list:
        if course in lect.courses_attached:
            mean = mean + sum(lect.grades[course]) / len(lect.grades[course])
    print(mean / len(lect_list))
    return mean / len(lect_list)


mean_student_and_course([best_student, best_student1], "Python")

mean_lect_and_course([cool_mentor, cool_mentor1], "Python")