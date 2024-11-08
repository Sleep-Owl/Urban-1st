import module_12_2
import unittest


class TournamentTest(unittest.TestCase):
    """
        Класс для тестирования турниров.
    """

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        """
        Создание объектов бегунов.
        """
        self.usain = module_12_2.Runner("Усэйн", 10)
        self.andrey = module_12_2.Runner("Андрей", 9)
        self.nick = module_12_2.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.items():
            r = {}
            for key, value in i[1].items():
                r[key] = value.name
            print(r)

    def test_tournament_usain_nick(self):
        """
        Сравнение Усейна и Ника
        """
        tournament = module_12_2.Tournament(90, self.usain, self.nick)
        finishers = tournament.start()
        last_runner = list(finishers.values())[-1]
        self.assertTrue(last_runner == self.nick, "Последний бегун должен быть Ник")
        self.all_results[1] = finishers

    def test_tournament_andrey_nick(self):
        """
        Сравнение Андрея и Ника
        """
        tournament = module_12_2.Tournament(90, self.andrey, self.nick)
        finishers = tournament.start()
        last_runner = list(finishers.values())[-1]
        self.assertTrue(last_runner == self.nick, "Последний бегун должен быть Ник")
        self.all_results[2] = finishers

    def test_tournament_usain_andrey_nick(self):
        """
        Сравнение Усейна, Андрея и Ника
        """
        tournament = module_12_2.Tournament(90, self.usain, self.andrey, self.nick)
        finishers = tournament.start()
        last_runner = list(finishers.values())[-1]
        self.assertTrue(last_runner == self.nick, "Последний бегун должен быть Ник")
        self.all_results[3] = finishers

    is_frozen = True
