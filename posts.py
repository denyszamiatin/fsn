import json
import datetime

# class Account:
#     """Контейнер для параметров Account
#     и списка полученного из него постов (Post) """
#     def __init__(self):
#         self.posts = [] # список объектов Post, выкачанных из ленты этого аккаунта
#
#     def exp_dict(self):
#         """Возвращает атрибуты класса в виде словаря для дальнейшего экспорта в сторонние форматы"""
#         return {}
#
#     def imp_dict(self, data):
#         """Втягивает параметры класса из словаря при импорте из сторонних форматов
#         посты импортятся отдельным методом
#         """
#         # открытый вопрос:
#         #   очищать self.posts,
#         #   или оставлять (порождает недостоверность принадлежности постов этому аккаунту)
#         pass
#
#     def add_post(self, post):
#         if isinstance(post,Post):
#             self.posts.append(post)
#         else:
#             raise TypeError('Parameter is not Post')


def set_timestamp(f):
    def wrapper(self, *args, **kwargs):
        result = f(self, *args, **kwargs)
        self.timestamp = datetime.datetime.now()
        return result
    return wrapper


class Post:
    def __init__(self, date, url, body,):
        self.import_dict(
            {
                'date': date,
                'url': url,
                'body': body,
            }
        )

    @set_timestamp
    def update(self, body):
        """Update self.body and set new timestamp"""
        self.body = body

    def export_dict(self):
        """Формирует словарь аттрибутов для дальнейшего хранения"""
        return {
            'date': self.date,
            'url': self.url,
            'body': self.body,
            'timestamp': self.timestamp
        }
        #return self.__dict__.copy()

    def export_(self, fmt: str):
        """ Возвращает строку в заданном формате
        для начала в JSON"""
        if fmt == 'JSON':
            return json.dumps(self.export_dict())
        raise ValueError("Unknown export format '%s'" % fmt)

    @set_timestamp
    def import_dict(self, data):
        self.__dict__ = data

    def import_(self, fmt: str, data: str):
        """ Втяшиваем строку в заданном формате
        для начала в JSON"""
        if fmt == 'JSON':
            self.import_dict(json.loads(data))
        raise ValueError("Unknown import format '%s'" % fmt)
