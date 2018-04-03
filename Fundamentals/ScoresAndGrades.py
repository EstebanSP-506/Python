import random
def scoresAndGrades():
    print "Scores and Grades"
    grade = str
    for index in range(0,10):
        random_num = random.randint(60,100)
        if random_num >= 60 and random_num<70:
            grade = "D"
        elif random_num >= 70 and random_num<80:
            grade = "C"
        elif random_num >= 80 and random_num<90:
            grade = "B"
        elif random_num >= 90 and random_num<=100:
            grade = "A"
        print "Score: "+str(random_num)+"; Your grade is "+grade
    print "End of the program, Bye!"

scoresAndGrades()



