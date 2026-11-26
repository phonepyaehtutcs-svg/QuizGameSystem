"""Save and load quiz data as JSON files."""

import json
from dataclasses import asdict
from pathlib import Path

from quiz_game.models import Question

DATA_DIR = Path(__file__).parent.parent / "data"
QUESTIONS_FILE = DATA_DIR / "questions.json"
SCORES_FILE = DATA_DIR / "scores.json"


def backup(path):
    """Copy a damaged file before it can be overwritten."""
    try:
        path.with_suffix(".bak").write_bytes(path.read_bytes())
    except OSError:
        print(f"Warning: could not back up {path.name}.")


def load_list(path):
    """Return the list in a JSON file, or an empty list."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    except ValueError:
        print(f"Warning: {path.name} is corrupted.")
        backup(path)
        return []
    except OSError:
        print(f"Warning: could not read {path.name}.")
        return []
    if not isinstance(data, list):
        print(f"Warning: {path.name} has the wrong format.")
        backup(path)
        return []
    return data


def save_list(path, data):
    """Write a list to a JSON file."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        text = json.dumps(data, indent=2, ensure_ascii=False)
        path.write_text(text, encoding="utf-8")
    except OSError:
        print(f"Warning: could not save {path.name}.")


def load_questions(path=QUESTIONS_FILE):
    """Load valid questions and skip invalid ones."""
    questions = []
    damaged = False
    for item in load_list(path):
        try:
            questions.append(Question(**item))
        except (TypeError, ValueError):
            damaged = True
    if damaged:
        print("Warning: invalid questions were skipped.")
        backup(path)
    return questions


def save_questions(questions, path=QUESTIONS_FILE):
    """Save Question objects as dictionaries."""
    save_list(path, [asdict(question) for question in questions])


def is_valid_score(item):
    """Check that a saved score has a name and a number."""
    return (
        isinstance(item, dict)
        and isinstance(item.get("name"), str)
        and bool(item["name"].strip())
        and type(item.get("score")) is int
        and item["score"] >= 0
    )


def load_scores(path=SCORES_FILE):
    """Load valid scores and skip invalid ones."""
    items = load_list(path)
    scores = [item for item in items if is_valid_score(item)]
    if len(scores) != len(items):
        print("Warning: invalid scores were skipped.")
        backup(path)
    return scores


def save_scores(scores, path=SCORES_FILE):
    """Save the leaderboard results."""
    save_list(path, scores)