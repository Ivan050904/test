from unittest import TestCase
import unittest
from testi import Runner
from testi import Tournament

class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    
    def setUp(self):
        self.Usain = Runner("Усейн", 10)
        self.Andrey = Runner("Андрей", 9)
        self.Nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            formatted_results = {position: runner.name for position, runner in value.items()}
            print(f"Тест {key}: {formatted_results}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        self.__class__.all_results["test_usain_and_nick"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_andrei_and_nick(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        self.__class__.all_results["test_andrei_and_nick"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_usain_andrei_and_nick(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        self.__class__.all_results["test_usain_andrei_and_nick"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")


if __name__ == "__main__":
    unittest.main()
