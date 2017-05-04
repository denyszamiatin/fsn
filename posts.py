import datetime
# import re
from bs4 import BeautifulSoup


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

# единый стандарт для преобразования datetime для совместимости с serialise (например JSON)
DATETIME_FORMAT = "%Y%m%d:%H:%M:%S%f"


def set_timestamp(f):
    """ Декоратор для автоматического обновления аттрибута timestamp
    Ограничения:
    - можно декорировать только методы классов, у которых есть аатрибут timestamp
    - нежелательно применять, метод изменяет аттрибут timestamp"""
    def wrapper(self, *args, **kwargs):
        result = f(self, *args, **kwargs)
        self._timestamp = datetime.datetime.utcnow()
        return result
    return wrapper


class Post:
    """ Контейнер, хранящий данные о публикации.
    Одно из применений - лента новостей, которая может быть организована как список объектов класса Post
    или производных от него классов.
    Post создаётся из источника каким-нибудь загрузчиком и этот момент фиксирует в атрибуте timestamp.
    Post обновляется из источника каким-нибудь загрузчиком и этот момент фиксирует в атрибуте timestamp.
    import_ рассчитывает на то, что атрибут timestamp уже зафиксировал когда были получены данные
        при сохранении методом export_ и поэтому не обновляет метку timestamp.
    """
    @set_timestamp
    def __init__(self, date: datetime.datetime, url, body,):
        self.date = date
        self.url = url
        self.body = body
        if __debug__:  # продублировано только для удобства работы в pycharm
            self._timestamp = datetime.datetime.utcnow()

    def __repr__(self):
        return "%s\n%s\n%s\n%s\n" % (self.date, self.url, self.body, self._timestamp)

    @set_timestamp
    def update(self, body):
        """Update self.body and set new timestamp"""
        self.body = body

    def export_dict(self):
        """Возвращает словарь выборочных! аттрибутов для дальнейшего хранения"""
        data = {
            'date': self.date.strftime(DATETIME_FORMAT),
            'url': self.url,
            'body': self.body,
            'timestamp': self._timestamp.strftime(DATETIME_FORMAT)
        }
        return data

    def import_dict(self, data):
        self.date = datetime.datetime.strptime(data['date'], DATETIME_FORMAT)
        self.url = data['url']
        self.body = data['body']
        self._timestamp = datetime.datetime.strptime(data['timestamp'],
                                                     DATETIME_FORMAT)


def tag_delete(post_):
    return BeautifulSoup(post_, 'lxml').get_text().strip()
    # return re.sub(r'<([A-Za-z1-9!/ ])*>', ' ', post_).strip()



if __name__ == '__main__':
    post = '''
    <!DOCTYPE html>
        <html>
            <body>  
                <h1>Header</h1>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
<b>Praesent rutrum tortor ac turpis venenatis, sit amet ullamcorper leo vestibulum.</b>
<i>Quisque lacinia, ex nec convallis congue, turpis sapien facilisis magna, non ultricies purus est id purus. </i>
Nunc ullamcorper magna ac libero porta, sit amet malesuada sapien posuere. In urna est, bibendum luctus metus non, dictum aliquet sem. 
Nulla euismod a elit a dapibus. Nulla varius quam purus, ac bibendum leo suscipit non. Fusce euismod odio non quam consequat suscipit. 
Fusce imperdiet diam ut molestie placerat. Sed ornare justo quam, sed convallis est interdum sit amet. </p>           
            </body>
        </html>
    '''

    print(tag_delete(post))
