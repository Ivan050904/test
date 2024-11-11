from unittest import TestCase
import unittest
from testik import Runner

class RunnerTest(TestCase):
    def test_walk(self):
        walkk = Runner("aa")
        for i in range(10):
            walkk.walk()
        self.assertEqual(walkk.distance,50)

    def test_run(self):
        runn = Runner("aaa")
        for i in range(10):
            runn.run()
        self.assertEqual(runn.distance,100)

    def test_challenge(self):
        runnn = Runner('bbb')
        walkkk= Runner('bb')

        for i in range(10):
            runnn.run()

        for i in range(10):
            walkkk.walk

        self.assertNotEqual(runnn.distance,walkkk.distance)

if __name__ == "__main__":
    unittest.main()