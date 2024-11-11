import module_12_4
import unittest
import logging

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Проверка функции walk
        """
        try:
            runner = module_12_4.Runner("Alex", -5)
            for i in range(10):
                runner.walk()
            walk_distance = runner.distance
            self.assertEqual(walk_distance, 50, 'Ошибка !!!')
            logging.info('test_walk выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        """
        Проверка функции Run
        """
        try:
            runner = module_12_4.Runner(1, 5)
            for i in range(10):
                runner.run()
            run_distance = runner.distance
            self.assertEqual(run_distance, 100, 'Ошибка !!!')
            logging.info('test_run выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        """
        Проверка неравенства двух объектов класса Runner
        """
        runner_1 = module_12_4.Runner('Alex')
        runner_2 = module_12_4.Runner('Max')
        for i in range(10):
            runner_1.run()
        run_distance = runner_1.distance
        for j in range(10):
            runner_2.walk()
        walk_distance = runner_2.distance
        self.assertNotEqual(run_distance, walk_distance, 'Ошибка !!!')


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s, %(levelname)s, %(message)s')
