class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {'ccs': [9, 10]}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecture, course, grade):
        if (isinstance(lecture, Lecturer)
                and course in self.courses_in_progress
                and course in lecture.courses_attached):
            lecture.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка: неверные данные при оценке лектора'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                'Средняя оценка за домашние задания: '
                f'{self._get_average_grade():g}\n'
                'Курсы в процессе изучения: '
                f'{','.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {''.join(self.finished_courses)}')

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() == other._get_average_grade()
        else:
            return 'Ошибка: объект сравнения не относится к классу Student'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() < other._get_average_grade()
        else:
            return 'Ошибка: объект сравнения не относится к классу Student'

    def __le__(self, other):
        if isinstance(other, Student):
            return self._get_average_grade() <= other._get_average_grade()
        else:
            return 'Ошибка: объект сравнения не относится к классу Student'

    def _get_average_grade(self):
        all_grades = sum(self.grades.values(), [])
        return sum(all_grades) / len(all_grades)


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {'html': [], 'ccs': [9, 10], 'java': [], 'sql': [7, 8]}

    def __str__(self):
        return (super().__str__()
                + '\nСредняя оценка за лекции: '
                  f'{self._get_average_grade():g}')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() == other._get_average_grade()
        else:
            return 'Ошибка: объект сравнения не относится к классу Student'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() < other._get_average_grade()
        else:
            return 'Ошибка: объект сравнения не относится к классу Student'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self._get_average_grade() <= other._get_average_grade()
        else:
            return 'Ошибка: объект сравнения не относится к классу Student'

    def _get_average_grade(self):
        all_grades = sum(self.grades.values(), [])
        return sum(all_grades) / len(all_grades)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка: неверные данные при оценке студента'


a_st = Student('A_Student', 'First', 'male')
a_st.finished_courses += ['Git']
a_st.courses_in_progress += ['Python']
a_st.grades['Git'] = [10, 10, 10, 10, 10]
a_st.grades['Python'] = [10, 10]

b_st = Student('B_Student', 'Second', 'male')
b_st.finished_courses += ['Git']
b_st.courses_in_progress += ['Python']
b_st.grades['Git'] = [10, 10, 10, 10, 10]
b_st.grades['Python'] = [10, 10]

a_lec = Lecturer('A_Lecturer', 'A_per')
a_lec.courses_attached.append('Python')

b_lec = Lecturer('B_Lecturer', 'B_per')
b_lec.courses_attached.append('Python')

a_rev = Reviewer('A_Reviewer', 'R_first')
a_rev.courses_attached += ['Python']

b_rev = Reviewer('B_Reviewer', 'R_second')
b_rev.courses_attached += ['Python']

a_rev.rate_hw(a_st, 'Python', 9.9)
print(a_st.grades)
# a_rev.rate_hw(a_st, 'Python', 10)
print(a_st.grades)
# a_rev.rate_hw(a_st, 'Python', 10)
print(a_st.grades, '\n')

print(a_lec.grades)
print(a_lec)
a_st.rate_lecture(a_lec, 'Python', 9)
print(a_lec.grades, '\n')

print(a_lec, '\n')

print(a_rev, '\n')
print(a_st, '\n')
print(b_st, '\n')

print('a_st == b_st:', a_st == b_st)
print('a_st != b_st:', a_st != b_st)
print('a_st > b_st:', a_st > b_st)
print('a_st < b_st:', a_st < b_st)
print('a_st <= b_st:', a_st <= b_st)
print('a_st >= b_st:', a_st >= b_st, '\n')

print('a_lec == b_lec:', a_lec == b_lec)
print('a_lec != b_lec:', a_lec != b_lec)
print('a_lec > b_lec:', a_lec > b_lec)
print('a_lec < b_lec:', a_lec < b_lec)
print('a_lec <= b_lec:', a_lec <= b_lec)
print('a_lec >= b_lec:', a_lec >= b_lec, '\n')

print(a_lec, b_lec, sep='\n')

