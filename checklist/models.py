from typing import List, Dict

class Problem:
    """Represents an individual LeetCode problem."""

    def __init__(self, id_num: int, name: str, completed: bool):
        self.id: int = id_num
        self.name: str = name
        self.completed: bool = completed

    def toggle(self) -> None:
        """Toggles the completion status of the problem."""
        self.completed = not self.completed

    def to_dict(self) -> Dict:
        """Converts the problem instance back into a serializable dictionary."""
        return {"id": self.id, "name": self.name, "completed": self.completed}


class Category:
    """Represents a difficulty level containing a collection of problems."""
    def __init__(self, difficulty: str, problems_data: List[Dict]):
        self.difficulty: str = difficulty
        self.problems: List[Problem] = [
            Problem(p["id"], p["name"], p["completed"]) for p in problems_data
        ]

    def to_dict(self) -> Dict:
        return {
            "difficulty": self.difficulty,
            "problems": [p.to_dict() for p in self.problems]
        }


class Week:
    """Represents a specific week containing a topic and difficulty categories."""
    def __init__(self, week_num: int, topic: str, categories_data: List[Dict]):
        self.week: int = week_num
        self.topic: str = topic
        self.categories: List[Category] = [
            Category(c["difficulty"], c["problems"]) for c in categories_data
        ]

    def to_dict(self) -> Dict:
        return {
            "week": self.week,
            "topic": self.topic,
            "categories": [c.to_dict() for c in self.categories]
        }