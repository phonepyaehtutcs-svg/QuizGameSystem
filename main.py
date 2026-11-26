"""Entry point and menu for the Quiz Game System."""

from quiz_game.game import Leaderboard, Quiz
from quiz_game.models import LETTERS, Question
from quiz_game.storage import load_questions, load_scores, save_questions, save_scores

MENU = """
========================================
           QUIZ GAME SYSTEM
========================================

1. Start Quiz
2. Add New Question
3. View All Questions
4. View Leaderboard
5. Exit

========================================"""


def ask_text(prompt):
    """Ask until the user types something that is not empty."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This cannot be empty.")


def ask_letter(prompt):
    """Ask until the user types A, B, C or D."""
    while True:
        letter = input(prompt).strip().upper()
        if letter in LETTERS:
            return letter
        print("Please enter A, B, C or D.")


def start_quiz(questions, board):
    """Play all questions and record the score."""
    if not questions:
        print("No questions yet. Add one first.")
        return
    name = ask_text("Your name: ")
    quiz = Quiz(questions)
    for number, question in quiz.question_generator():
        print(f"\nQuestion {number}: {question}")
        if quiz.check_answer(question, ask_letter("Your answer: ")):
            print("Correct!")
        else:
            print(f"Wrong. The answer is {question.answer}.")
    print(f"\n{name}, your score is {quiz.score}/{len(questions)}.")
    board.add_result(name, quiz.score)


def add_question(questions):
    """Ask for a new question and add it to the list."""
    text = ask_text("Question: ")
    options = {}
    for letter in LETTERS:
        options[letter] = ask_text(f"Answer {letter}: ")
    answer = ask_letter("Correct answer (A-D): ")
    questions.append(Question(text, options, answer))
    print("Question added.")


def view_questions(questions):
    """Show every question with its correct answer."""
    if not questions:
        print("No questions yet.")
    for number, question in enumerate(questions, start=1):
        print(f"\n{number}. {question}")
        print(f"Correct answer: {question.answer}")


def view_leaderboard(board):
    """Show players from highest to lowest score."""
    if not board.results:
        print("No scores yet.")
    for place, result in enumerate(board.ranked(), start=1):
        print(f"{place}. {result['name']} - {result['score']}")


def main():
    """Show the menu until the user exits."""
    questions = load_questions()
    board = Leaderboard(load_scores())
    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            start_quiz(questions, board)
            save_scores(board.results)
        elif choice == "2":
            add_question(questions)
            save_questions(questions)
        elif choice == "3":
            view_questions(questions)
        elif choice == "4":
            view_leaderboard(board)
        elif choice == "5":
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid choice. Enter 1 to 5.")
        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")