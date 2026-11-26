"""Tests for questions, the quiz and the leaderboard."""

import pytest

from quiz_game.game import Leaderboard, Quiz
from quiz_game.models import Question


def make_question(text="What is 2 + 2?", answer="B"):
    """Create a sample question for the tests."""
    options = {"A": "3", "B": "4", "C": "5", "D": "6"}
    return Question(text, options, answer)


def test_correct_answer_adds_point():
    question = make_question()
    quiz = Quiz([question])
    assert quiz.check_answer(question, "b") is True
    assert quiz.score == 1


def test_wrong_answer_adds_no_point():
    question = make_question()
    quiz = Quiz([question])
    assert quiz.check_answer(question, "A") is False
    assert quiz.score == 0


def test_generator_numbers_questions_from_one():
    quiz = Quiz([make_question(), make_question()])
    numbers = [number for number, _ in quiz.question_generator()]
    assert numbers == [1, 2]


def test_generator_with_no_questions_is_empty():
    assert list(Quiz([]).question_generator()) == []


def test_empty_question_is_rejected():
    with pytest.raises(ValueError):
        make_question(text="   ")


def test_invalid_answer_letter_is_rejected():
    with pytest.raises(ValueError):
        make_question(answer="E")


def test_leaderboard_sorts_highest_first():
    board = Leaderboard()
    board.add_result("Ann", 1)
    board.add_result("Ben", 3)
    assert [item["name"] for item in board.ranked()] == ["Ben", "Ann"]


def test_empty_name_is_rejected():
    with pytest.raises(ValueError):
        Leaderboard().add_result("   ", 1)
