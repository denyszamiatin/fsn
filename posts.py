import datetime
from bs4 import BeautifulSoup
from langdetect import detect


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
    return ' '.join(BeautifulSoup(post_, 'lxml').get_text().split())


def detect_language(post_):
    return detect(post_)

if __name__ == '__main__':
    post1 = '''In the beautiful city of Verona, where our story takes place, 
    a long-standing hatred between two families erupts into new violence, 
    and citizens stain their hands with the blood of their fellow citizens. 
    Two unlucky children of these enemy families become lovers and commit suicide. 
    Their unfortunate deaths put an end to their parents' feud. For the next two hours, 
    we will watch the story of their doomed love and their parents' anger, which 
    nothing but the children’s deaths could stop. If you listen to us patiently, 
    we’ll make up for everything we’ve left out in this prologue onstage.'''
    post2 = '''Zwei Hдuser waren—gleich an Wьrdigkeit—
    Hier in Verona, wo die Handlung steckt,
    Durch alten Groll zu neuem Kampf bereit,
    Wo Bьrgerblut die Bьrgerhand befleckt.
    Aus dieser Feinde unheilvollem Schoя
    Das Leben zweier Liebender entsprang,
    Die durch ihr unglьckselges Ende bloя
    Im Tod begraben elterlichen Zank.'''
    post3 = '''Однаково шляхетні дві сім'ї
    В Вероні пишній, де проходить дія,
    Збували в ворожнечі дні свої.
    Аж враз кривава скоїлась подія.
    Коханців двоє щирих,запальних
    Ворожі ті утроби породили;
    Нещастя сталося у сім'ях тих,-
    Вони одвічні звади припинили.'''

    print(detect_language(post1), detect_language(post2), detect_language(post3))
