import os

def export_questions_to_html(questions, output_folder, is_answer_key, name, suffix):
    """
    Exports a list of questions to an HTML file.

    Parameters:
    - questions: List[Dict], each dict has 'question', 'correct', 'incorrect' keys
    - output_file: str, filename to save the HTML to
    """

    create_folder(output_folder)
    output_file = output_folder + '/' + name + suffix

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>"""

    html_content += f"<title>Quiz Questions for {name}</title>"
    html_content += """<style>
            body { font-family: Arial, sans-serif; }
            .question { margin-bottom: 20px; }
            .answers { margin-left: 20px; }
        </style>
    </head>
    <body>
        <h1>Quiz Questions"""
    html_content += f" for {name}</h1>"



    for i, q in enumerate(questions, start=1):
        html_content += f'<div class="question">'
        html_content += f'<p><strong>Q{i}:</strong> {q["question"]}</p>'

        if is_answer_key:
            html_content += f'<p>({q["category"]})</p>'

        html_content += '<ul class="answers">'

        # Combine correct and incorrect answers
        if not is_answer_key:
            all_answers = [q["correct"]] + q["incorrect"]
        else:
            all_answers = [q["correct"]]

        # Optionally shuffle answers
        import random
        random.shuffle(all_answers)

        for ans in all_answers:
            html_content += f'<li>{ans}</li>'
        html_content += '</ul></div>'

    html_content += """
    </body>
    </html>
    """

    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Questions exported to {output_file}")


def create_folder(folder_path):
    """
    Creates a folder if it doesn't exist.

    Parameters:
    - folder_path: str, path of the folder to create
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")