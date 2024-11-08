import module_12_1
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тест пройден')
    def test_walk(self):
        """
        Проверка функции walk
        """
        runner = module_12_1.Runner("Alex")
        for i in range(10):
            runner.walk()
        walk_distance = runner.distance
        self.assertEqual(walk_distance, 50, 'Ошибка !!!')

    @unittest.skipIf(is_frozen == True, 'Тест пройден')
    def test_run(self):
        """
        Проверка функции Run
        """
        runner = module_12_1.Runner("Alex")
        for i in range(10):
            runner.run()
        run_distance = runner.distance
        self.assertEqual(run_distance, 100, 'Ошибка !!!')

    @unittest.skipIf(is_frozen == True, 'Тест пройден')
    def test_challenge(self):
        """
        Проверка неравенства двух объектов класса Runner
        """
        runner_1 = module_12_1.Runner('Alex')
        runner_2 = module_12_1.Runner('Max')
        for i in range(10):
            runner_1.run()
        run_distance = runner_1.distance
        for j in range(10):
            runner_2.walk()
        walk_distance = runner_2.distance
        self.assertNotEqual(run_distance, walk_distance, 'Ошибка !!!')
