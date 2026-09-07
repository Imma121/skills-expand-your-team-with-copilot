import unittest
from unittest.mock import patch

from src.backend.routers import activities


class FakeActivitiesCollection:
    def __init__(self):
        self.last_query = None

    def find(self, query):
        self.last_query = query
        return []


class ActivitiesDifficultyFilterTests(unittest.TestCase):
    def test_filters_by_specific_difficulty(self):
        fake_collection = FakeActivitiesCollection()

        with patch.object(activities, "activities_collection", fake_collection):
            activities.get_activities(difficulty="Beginner")

        self.assertEqual(fake_collection.last_query, {"difficulty": "Beginner"})

    def test_all_difficulty_returns_unspecified_only(self):
        fake_collection = FakeActivitiesCollection()

        with patch.object(activities, "activities_collection", fake_collection):
            activities.get_activities(difficulty="all")

        self.assertEqual(
            fake_collection.last_query,
            {"$or": [{"difficulty": {"$exists": False}}, {"difficulty": None}]},
        )


if __name__ == "__main__":
    unittest.main()
