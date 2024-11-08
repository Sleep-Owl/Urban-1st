import unittest
import tests_12_2
import tests_12_1

module12ST = unittest.TestSuite()
module12ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
module12ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(module12ST)
