n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key, value in student_marks.items():
        if query_name==key:
            avg=sum(value)/len(value)
            print("{:.2f}".format(avg))
