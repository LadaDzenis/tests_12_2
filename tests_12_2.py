import Runner_2 as runner
import unittest
from pprint import pprint

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = runner.Runner('Усэйн', 10)
        self.second = runner.Runner('Андрей', 9)
        self.third = runner.Runner('Ник', 3)

    def test_first_tournament(self):
        tournament = runner.Tournament(90, self.first, self.third)
        results = tournament.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['1'] = results


    def test_second_tournament(self):
        tournament_2 = runner.Tournament(90, self.second, self.third)
        results = tournament_2.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['2'] = results

    def test_third_tournament(self):
        tournament_3 = runner.Tournament(90, self.first, self.second, self.third)
        results = tournament_3.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['3'] = results

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Test {test_key}:')
            for key, value in test_value.items():
                print(f'\t{key}: {value}')


if __name__ == "__main__":
    unittest.main()







