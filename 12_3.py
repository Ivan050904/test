import unittest
import test_12_1
import test_12_2


calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)