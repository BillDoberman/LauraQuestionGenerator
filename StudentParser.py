import csv

def parse_student_scores(csv_file_path):
    students = []

    with open(csv_file_path, newline='') as f:
        reader = csv.reader(f)

        # Read header row
        header = next(reader)
        subjects = header[1:]  # skip first blank cell

        # Process each student row
        for row in reader:
            name = row[0]
            scores = row[1:]

            student_dict = {"name": name}

            # Map each subject to its score
            for subject, score in zip(subjects, scores):
                # Convert to number when possible
                try:
                    score = int(score)
                except ValueError:
                    pass
                student_dict[subject.lower()] = score

            students.append(student_dict)

    return students