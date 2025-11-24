import csv
import random

import QuestionParser
import StudentParser
import QuestionGenerator
import HTMLMaker
import os

TEST_SCORES_FILE = 'TestScores.csv'
QUESTIONS_FILE = 'Questions.csv'
QUESTIONS_OUTPUT_FOLDER = 'question_files'
ANSWERS_OUTPUT_FOLDER = 'answer_files'
SHUFFLE_QUESTION_CATEGORIES = True

student_scores = StudentParser.parse_student_scores(TEST_SCORES_FILE)
question_library = QuestionParser.parse_question_csv(QUESTIONS_FILE)
generated_questions = QuestionGenerator.generate_question_list(question_library, student_scores)

for student in generated_questions:
    if SHUFFLE_QUESTION_CATEGORIES:
        random.shuffle(generated_questions[student])
    HTMLMaker.export_questions_to_html(generated_questions[student], QUESTIONS_OUTPUT_FOLDER, False, student, '_quiz.html')
    HTMLMaker.export_questions_to_html(generated_questions[student], ANSWERS_OUTPUT_FOLDER, True, student, '_key.html')
