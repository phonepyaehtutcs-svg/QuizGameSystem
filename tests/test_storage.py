"""Tests for saving and loading JSON files."""

from quiz_game.models import Question
from quiz_game.storage import (
    load_questions,
    load_scores,
    save_questions,
    save_scores,
)


def test_questions_save_and_load(tmp_path):
    path = tmp_path / "questions.json"
    options = {"A": "1", "B": "2", "C": "3", "D": "4"}
    questions = [Question("What is 1 + 1?", options, "B")]
    save_questions(questions, path)
    assert load_questions(path) == questions


def test_scores_save_and_load(tmp_path):
    path = tmp_path / "scores.json"
    scores = [{"name": "Ann", "score": 0}]
    save_scores(scores, path)
    assert load_scores(path) == scores


def test_missing_file_gives_empty_list(tmp_path):
    assert load_scores(tmp_path / "missing.json") == []


def test_corrupted_file_is_backed_up(tmp_path):
    path = tmp_path / "scores.json"
    path.write_text("abc", encoding="utf-8")
    assert load_scores(path) == []
    assert (tmp_path / "scores.bak").read_text(encoding="utf-8") == "abc"


def test_invalid_score_is_skipped(tmp_path):
    path = tmp_path / "scores.json"
    save_scores([{"name": "Ann", "score": -1}, {"name": "Ben", "score": 2}], path)
    assert load_scores(path) == [{"name": "Ben", "score": 2}]
