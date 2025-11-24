from collections import defaultdict
import csv

def parse_question_csv(csv_file_path):
    categories = defaultdict(list)

    with open(csv_file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) # skip first row
        for row in reader:
            if not row or len(row) < 3:
                # Skip empty or invalid rows
                continue

            category = row[0]
            question_text = row[1]
            correct_answer = row[2]
            incorrect_answers = row[3:]  # any remaining columns

            question_entry = {
                "question": question_text,
                "correct": correct_answer,
                "incorrect": incorrect_answers,
                "category": category
            }

            categories[category.lower()].append(question_entry)

    return dict(categories)