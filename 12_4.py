import unittest
from testi import Runner  
import logging


logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="UTF-8",
    format="%(levelname)s:%(message)s"
)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            walkk = Runner("a", -1)  
            logging.info('"test_walk" успешно выполнен')
            for i in range(10):
                walkk.walk()
            
            self.assertEqual(walkk.distance, -10)  
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            runn = Runner("runner", 20)  
            logging.info('"test_run" успешно выполнен')
            for i in range(10):
                runn.run()
            
            self.assertNotEqual(runn.distance, 200)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')

    def test_challenge(self):
        runnn = Runner('bbb', 10)
        walkkk = Runner('bb', 5)

        for i in range(10):
            runnn.run()

        for i in range(10):
            walkkk.walk()  

        self.assertNotEqual(runnn.distance, walkkk.distance)  

if __name__ == "__main__":
    unittest.main()
