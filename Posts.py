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

class Post:
    def __init__(self, date, url, body,):
        self.date = date
        self.url = url
        self.body = body
        self.timemark = datetime.datetime()

    def update(self, body):
        """Update self.body and set new timestamp"""
        self.body = body
        self.timemark = datetime.datetime()

    def exp_dict(self):
        """Формирует словарь аттрибутов для дальнейшего хранения"""
        return {'date':self.date,
                'url':self.url,
                'body':self.body,
                'timemark':self.timemark}

    def exp(self, fmt: str):
        """ Возвращает строку в заданном формате
        для начала в JSON"""
        if fmt == 'JSON': return json.dumps(self.exp_dict())
        raise ValueError("Unknown export format '%s'" % fmt)

    def imp_dict(self, data):
        self.date = data['date']
        self.url = data['url']
        self.body = data['body']
        self.timemark = datetime.datetime()

    def imp(self, fmt: str, data: str):
        """ Втяшиваем строку в заданном формате
        для начала в JSON"""
        if fmt == 'JSON': self.imp_dict(json.loads(data))
        raise ValueError("Unknown export format '%s'" % fmt)
