# Extended Python Quiz Program

def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
            "answer": "B"
        },
        {
            "question": "Which language is used to write Python?",
            "options": ["A. English", "B. Binary", "C. Python", "D. C"],
            "answer": "C"
        },
        {
            "question": "What is the output of 2 + 3 * 2?",b
            "options": ["A. 10", "B. 12", "C. 8", "D. 7"],
            "answer": "D"
        },
        {
            "question": "Which data type is used to store text?",
            "options": ["A. int", "B. str", "C. float", "D. bool"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a Python keyword?",
            "options": ["A. define", "B. switch", "C. finally", "D. function"],
            "answer": "C"
        },
        {
            "question": "What symbol is used to comment a single line in Python?",
            "options": ["A. //", "B. <!--", "C. #", "D. /*"],
            "answer": "C"
        },
        {
            "question": "What does the len() function do?",
            "options": ["A. Returns the number of lines", "B. Returns the length of a string/list", "C. Adds two numbers", "D. Exits the loop"],
            "answer": "B"
        },
        {
            "question": "Which of these is used to define a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "What is the output of: print(type(5))?",
            "options": ["A. <type 'int'>", "B. int", "C. <class 'int'>", "D. number"],
            "answer": "C"
        },
        {
            "question": "Which one is a loop in Python?",
            "options": ["A. repeat", "B. for", "C. loop", "D. iterate"],
            "answer": "B"
        },
    ]

    score = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}.")

    print(f"\n🎯 Your final score is: {score} out of {len(questions)}")

# Run the quiz
run_quiz()