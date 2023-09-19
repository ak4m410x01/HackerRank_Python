#!/bin/python3


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for student_name, student_scores in student_marks.items():
        if student_name == query_name:
            student_scores_avg = sum(student_scores) / len(student_scores)
            print(f"{student_scores_avg:.2f}")
