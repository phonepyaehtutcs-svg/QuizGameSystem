"""Entry point for the Quiz Game System."""

from quiz_game.models import Question


def main():
    """Start the program."""
    options = {"A": "3", "B": "4", "C": "5", "D": "6"}
    question = Question("What is 2 + 2?", options, "b")
    print(question)
    print(question.is_correct("B"))
    print(question.is_correct("A"))


if __name__ == "__main__":
    main()