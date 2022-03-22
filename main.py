from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_for_a_lectur(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades:
            lecturer.grades[course] += [grade]
          else: lecturer.grades[course] = [grade]
        else: 'Ошибка'

    def __str__(self):
        list_avg = 0
        for grad in self.grades:
            list_avg = mean( self.grades.get(grad) )
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {list_avg}\nКурсы в процессе изучения: {','.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}"
        return text

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        for grad in self.grades:
            list_avg = mean( self.grades.get(grad) )
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{list_avg}"
        return text


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}"
        return text


best_student = Student('Ruoy', 'Eman', 'boy')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)

print(best_student.grades)

second_student = Student('Bob', 'Grenn', 'girl')
second_student.courses_in_progress += ['Geology']

cool_lecturer = Lecturer('Sam', 'Smith')
cool_lecturer.courses_attached += ['Geology']
second_student.grade_for_a_lectur(cool_lecturer, 'Geology', 9)
second_student.grade_for_a_lectur(cool_lecturer, 'Geology', 8)

print(cool_lecturer.grades)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)

s1 = Student('Ruoy1', 'Eman1', 'boy1')
s2 = Student('Ruoy2', 'Eman2', 'boy2')

m1 = Mentor('Bil1', 'Tom2')
m2 = Mentor('Bil2', 'Tom2')

l1 = Lecturer('Sam1', 'Smith1')
l2 = Lecturer('Sam2', 'Smith2')

r1 = Reviewer('Some1', 'Buddy1')
r2 = Reviewer('Some2', 'Buddy2')

s1.grade_for_a_lectur(l1, 'Geology', 7)
s2.grade_for_a_lectur(l2, 'Geology', 6)

r1.rate_hw(s1, 'Python', 9)
r2.rate_hw(s2, 'Python', 9)

m1.rate_hw(s1, 'Geology', 7)
m2.rate_hw(s2, 'Geology', 6)

l1.rate_hw(s1, 'Geology', 7)
l2.rate_hw(s2, 'Geology', 6)