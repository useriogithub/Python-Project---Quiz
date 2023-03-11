#quiz.py

QUESTIONS = [
    ("When was the first car built and by who?", "1893 by the Duryea brothers", "1912", "Henry Ford", "Maserati"),
    ("When was the first pyramid built?","2780 BCE", "33BC", "200AD"),
    ("What is Taylor Swift's most popular single?", "Shake It Off", "I Knew You Were Trouble", "Blank Space", "Love Story")
]

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")