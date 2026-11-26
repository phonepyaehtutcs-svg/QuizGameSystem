"""Entry point for the Quiz Game System."""

from quiz_game.game import Leaderboard, Quiz
from quiz_game.models import Question


def main():
    """Start the program."""
    options = {"A": "3", "B": "4", "C": "5", "D": "6"}
    quiz = Quiz([Question("What is 2 + 2?", options, "B")])
    for number, question in quiz.question_generator():
        print(f"Question {number}: {question}")
        print(quiz.check_answer(question, "b"))
    print("Score:", quiz.score)

    board = Leaderboard()
    board.add_result("Ann", 1)
    board.add_result("Ben", 3)
    print(board.ranked())


if __name__ == "__main__":
    main()
    