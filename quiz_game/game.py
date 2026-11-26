"""Quiz and leaderboard logic."""


class Quiz:
    """Manage the questions and the player's score."""

    def __init__(self, questions):
        """Store the questions and start with a score of zero."""
        self.questions = questions
        self.score = 0

    def question_generator(self):
        """Yield each question with its number, one at a time."""
        for number, question in enumerate(self.questions, start=1):
            yield number, question

    def check_answer(self, question, choice):
        """Add a point if the choice is correct."""
        if question.is_correct(choice):
            self.score += 1
            return True
        return False


class Leaderboard:
    """Manage player results and rankings."""

    def __init__(self, results=None):
        """Start with saved results or an empty list."""
        if results is None:
            results = []
        self.results = results

    def add_result(self, name, score):
        """Add one player's result."""
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        self.results.append({"name": name, "score": score})

    def ranked(self):
        """Return results from highest to lowest score."""
        return sorted(self.results, key=lambda item: item["score"], reverse=True)
    