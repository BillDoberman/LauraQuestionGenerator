import random


def get_question_count(score):
    count = 3
    if score < 4:
        count = 5
    if score < 2:
        count = 7
    if score < 1:
        count = 9
    return count

def generate_question_list(question_library, student_scores):
    questions = {}
    for student in student_scores:
        name = student['name']
        questions[name] = list()
        for category in question_library:
            if category in student:
                student_score = student[category]
                question_count = get_question_count(student_score)
                question_list = question_library[category]
                random.shuffle(question_list)
                for i in range(0, min(len(question_list), question_count)):
                    questions[name].append(question_list[i])
    return questions
