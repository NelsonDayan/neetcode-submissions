class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        iterations = len(students)
        while True:
            if len(students) == 0:
                return 0

            # we've cycled through all the students already once
            if iterations == 0:
                return len(students)

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                iterations = len(students)
            else:
                student = students.pop(0)
                students.append(student)
                iterations -= 1