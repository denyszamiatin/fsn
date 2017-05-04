import datetime
import unittest
# import unittest.mock

from expimp import ExpImp, ExpImpFile
from posts import Post, DATETIME_FORMAT


def print_name(f):
    """Декоратор для вывода названия теста по названию метода __name__"""
    def wrapper(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return wrapper


class TestExpImp(unittest.TestCase):
    def setUp(self):
        self._today = datetime.datetime.today()
        self.p = Post(self._today, "https://", "Bla-bla-bla")
        print("\n<--- TestExpImp: %s" % self._today.strftime(DATETIME_FORMAT))

    @print_name
    def testReloadPost(self):
        """ Экспорт-Импорт должен сохранить объект"""
        io = ExpImp('JSON')
        json_str = io.export_(self.p)
        io.import_(self.p, json_str)
        self.assertTrue((self.p.date, self.p.url, self.p.body) == (self._today, "https://", "Bla-bla-bla"))

    @print_name
    def testReloadPost(self):
        """ Экспорт-Импорт должен сохранить объект"""
        io = ExpImp('JSON')
        json_str = io.export_(self.p)
        io.import_(self.p, json_str)
        self.assertTrue((self.p.date, self.p.url, self.p.body) == (self._today, "https://", "Bla-bla-bla"))

    def tearDown(self):
        print('TestExpImp --->')


class TestExpImpFile(unittest.TestCase):
    def setUp(self):
        self._today = datetime.datetime.today()
        self.p = Post(self._today, "https://", "Bla-bla-bla")
        print("\n<--- TestExpImpFile: %s" % self._today.strftime(DATETIME_FORMAT))

    @print_name
    def testReloadPost(self):
        """ Экспорт-Импорт должен сохранить объект"""
        io = ExpImpFile('JSON','test_main.json')
        io.export_(self.p)
        io.import_(self.p)
        self.assertTrue((self.p.date, self.p.url, self.p.body) == (self._today, "https://", "Bla-bla-bla"))

    def tearDown(self):
        print('TestExpImpFile --->')


if __name__ == '__main__':
    pass