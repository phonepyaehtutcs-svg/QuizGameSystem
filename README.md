# Quiz Game System

A command-line quiz game written in Python (CS105BKK final project).

## Features

- Take a multiple-choice quiz and get a score
- Add and view questions
- View a leaderboard
- Questions and scores are saved as JSON

Requires Python 3.12 or newer. The game works offline.

## Run on Windows

```
git clone https://github.com/phonepyaehtutcs-svg/QuizGameSystem.git
cd QuizGameSystem
python main.py
```

## Run on macOS

```
git clone https://github.com/phonepyaehtutcs-svg/QuizGameSystem.git
cd QuizGameSystem
python3 -m venv .venv
source .venv/bin/activate
python main.py
```

## Tests and code quality

Installing these tools needs internet.

```
python -m pip install -r requirements.txt
python -m pytest
python -m ruff check .
```

## Project structure

- `main.py`: menu and user input
- `quiz_game/models.py`: `Question` class
- `quiz_game/game.py`: `Quiz` and `Leaderboard` classes
- `quiz_game/storage.py`: loading and saving JSON
- `data/`: saved questions and scores
- `tests/`: pytest tests