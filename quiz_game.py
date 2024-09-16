import random

def ask_question(question, correct_answer):
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct answer is {correct_answer}.")
        return 0

def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    
    # Shuffle the questions
    random.shuffle(questions)
    
    for question, answer in questions:
        score += ask_question(question, answer)
    
    print(f"\nYou got {score} out of {total_questions} questions correct!")
    percentage = (score / total_questions) * 100
    print(f"Your score: {percentage:.2f}%")

def main():
    print("Welcome to the Quiz Game!")
    
    if input("Do you want to play? ").lower() != "yes":
        print("Maybe next time. Goodbye!")
        return

    print("Okay! Let's play :)")
    
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
        ("What is the boiling point of water in Celsius?", "100"),
        ("What is the capital of Japan?", "Tokyo"),
        ("What is the chemical symbol for gold?", "Au"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
        ("What is the smallest prime number?", "2"),
        ("What is the capital of Canada?", "Ottawa"),
        ("What is the largest ocean on Earth?", "Pacific"),
        ("Who developed the theory of relativity?", "Einstein"),
        ("What is the hardest natural substance on Earth?", "Diamond"),
        ("What is the capital of Australia?", "Canberra"),
        ("What is the square root of 64?", "8"),
        ("Who wrote '1984'?", "George Orwell"),
        ("What is the capital of Italy?", "Rome"),
        ("What is the chemical symbol for water?", "H2O"),
        ("Who was the first president of the United States?", "George Washington"),
        ("What is the capital of Germany?", "Berlin"),
    ]
    
    run_quiz(questions)

if __name__ == "__main__":
    main()