class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecture, course, grade):
        if (isinstance(lecture, Lecturer)
                and course in self.courses_in_progress
                and course in lecture.courses_attached):
            lecture.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка: неверные данные при оценке лектора'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка: неверные данные при оценке студента'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades, '\n')

best_lecture = Lecturer('Some_Lec', 'Some_per')
best_lecture.courses_attached.append('Python')

cool_mentor = Reviewer('Some_Rev', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)

cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades, '\n')

print(best_lecture.grades)
best_student.rate_lecture(best_lecture, 'Python', 9)
print(best_lecture.grades)

