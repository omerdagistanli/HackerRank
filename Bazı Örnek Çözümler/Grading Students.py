def gradingStudents(arr, n):
    liste =  []
    for i in range(n):
        if arr[i] < 38:
            liste += [arr[i]]
        elif 5 - (arr[i] % 5) <= 2:
            liste += [arr[i] + (5 - (arr[i] % 5))]
        else:
            liste += [arr[i]]
    for j in liste:
        print(j)

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
   grades_item = int(input().strip())
   grades.append(grades_item)

gradingStudents(grades, grades_count)