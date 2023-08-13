'''
Complete function so that if finds
the average of three scores passed to it
and returns the letter value associated with
that grade like A B C D E F

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
'''


# Version 1
def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 90:
        return 'B'
    elif 70 <= score <= 80:
        return 'C'
    elif 60 <= score <= 70:
        return 'D'
    else:
        return 'F'


s1 = 10
s2 = 20
s3 = 30

grade = get_grade(s1, s2, s3)
print(f"The grade letter is: {grade}")


# Version 2

def get_grade(*args):
    total_score = sum(args)
    average_score = total_score / len(args)
    if 90 <= average_score <= 100:
        return 'A'
    elif 80 <= average_score <= 90:
        return 'B'
    elif 70 <= average_score <= 80:
        return 'C'
    elif 60 <= average_score <= 70:
        return 'D'
    else:
        return 'F'

s1 = 70
s2 = 90
s3 = 100

grade = get_grade(s1, s2, s3)
print(f"The grade letter is: {grade}")
