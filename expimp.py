import json


class ExpImp:
    """ Универсальный класс для Экспорта-Импорта аттрибутов другого класса cls через словарь
        Использует его методы cls.import_dict и cls.export_dict
    """
    def __init__(self, fmt: str):
        if fmt not in ('JSON'): # ,'XML'
            raise ValueError("Unknown import format '%s'" % fmt)
        self.format_ = fmt

    def import_(self, cls, data):
        if self.format_ == 'JSON': # ,'XML'
            cls.import_dict(json.loads(data))

    def export_(self, cls):
        if self.format_ == 'JSON':
            return json.dumps(cls.export_dict())

class ExpImpFile:
    def __init__(self, fmt: str, fname):
        self._worker = ExpImp(fmt)
        self._fname = fname

    def import_(self, cls):
        with open(self._fname,'rt') as fdesc:
            self._worker.import_(cls, fdesc.read())

    def export_(self, cls):
        with open(self._fname,'wt') as fdesc:
            fdesc.write(self._worker.export_(cls))

if __name__ == '__main__':
    pass