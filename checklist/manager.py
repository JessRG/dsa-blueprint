import json
import os
from typing import List, Tuple
from models import Week, Problem


class ChecklistManager:
    """Handles deserialization, internal mapping, and serialization of the checklist JSON data."""

    def __init__(self, file_path: str = "data.json"):
        self.file_path: str = file_path
        self.weeks: List[Week] = []
        self.flat_problems: List[Problem] = []  # Flat index mapping for easy UI selection
        self.load_data()

    def load_data(self) -> None:
        """Loads and deserializes the JSON file into an object hierarchy."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Missing mandatory data storage schema: '{self.file_path}'")

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.weeks = [
            Week(w["week"], w["topic"], w["categories"]) for w in data.get("weeks", [])
        ]

        # Regenerate flat array references for sequential mapping access
        self.flat_problems = []
        for week in self.weeks:
            for category in week.categories:
                for problem in category.problems:
                    self.flat_problems.append(problem)

    def save_data(self) -> None:
        """Serializes the object model graph back to the clean JSON format file layout."""
        output_data = {
            "weeks": [w.to_dict() for w in self.weeks]
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2)

    def toggle_problem_by_index(self, index: int) -> bool:
        """Toggles a problem's state using a 1-based console list index."""
        if 1 <= index <= len(self.flat_problems):
            problem = self.flat_problems[index - 1]
            problem.toggle()
            self.save_data()
            return True
        return False

    def get_progress_metrics(self) -> Tuple[int, int, float]:
        """Calculates global analytics metrics: completed tasks, total tasks, and percentage."""
        total = len(self.flat_problems)
        completed = sum(1 for p in self.flat_problems if p.completed)
        percentage = (completed / total * 100) if total > 0 else 0.0
        return completed, total, percentage