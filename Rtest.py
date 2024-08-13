import logging
import unittest

from Module12.HW4.runner_and_tournament import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("TestWalker", -5)
            logging.info("успешно")
        except:
            logging.error("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            runner = Runner(123, 10)
            logging.info("успешно")
        except :
            logging.error("Неверный тип данных для объекта Runner", exc_info=True)


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s')
if __name__ == '__main__':
    unittest.main()