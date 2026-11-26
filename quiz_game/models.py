"""Data models for the Quiz Game System."""

from dataclasses import dataclass

LETTERS = ("A", "B", "C", "D")


@dataclass
class Question:
    """One multiple-choice question."""

    text: str
    options: dict[str, str]
    answer: str

    def __post_init__(self):
        """Check that the question is valid."""
        if not isinstance(self.text, str) or not self.text.strip():
            raise ValueError("Question text cannot be empty.")
        if not isinstance(self.options, dict) or set(self.options) != set(LETTERS):
            raise ValueError("Options must be A, B, C and D.")
        for option in self.options.values():
            if not isinstance(option, str) or not option.strip():
                raise ValueError("An answer choice cannot be empty.")
        answer = str(self.answer).strip().upper()
        if answer not in LETTERS:
            raise ValueError("Correct answer must be A, B, C or D.")
        self.answer = answer

    def is_correct(self, choice):
        """Return True if the choice is the correct answer."""
        return choice.strip().upper() == self.answer

    def __str__(self):
        """Return the question and its choices as text."""
        lines = [self.text]
        for letter in LETTERS:
            lines.append(f"{letter}. {self.options[letter]}")
        return "\n".join(lines)
