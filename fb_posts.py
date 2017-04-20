import facebook
import csv
import pprint

APP_ID= '119610841474711'
APP_SECRET= 'acd9a657733dd91434a6f94df2f71124'

USER_ID = '1546116578732756'


class ReadFBPosts:

    def __init__(self):
        """
        get access token tot FB page by app_id and app_secret
        app_id and app_secret from https://developers.facebook.com

        """
        access_token = facebook.GraphAPI.get_app_access_token(
            facebook.GraphAPI, APP_ID, APP_SECRET, offline=True)
        self.conn = facebook.GraphAPI(access_token=access_token, version=2.7)


    # def add_fb_post():
    #     return connect_to_fb().put_object(parent_object=USER_ID, connection_name='feed',
    #                  message='FB API works!')

    def read_all_posts(self):
        """read user feed by user id"""
        return self.conn.get_connections(id=USER_ID, connection_name='feed')


def save_all_posts_to_txt():
    posts = ReadFBPosts().read_all_posts()
    list_ = posts['data']
    with open('posts.txt', 'wt') as text_file:
        for line in list_:
            text_file.write(str(line) + '\n')


def save_all_posts_to_csv():
    posts = ReadFBPosts().read_all_posts()
    list_ = posts['data']
    keys = ['story', 'message', 'created_time', 'id']
    with open('posts.csv', 'wt') as text_file:
        dict_writer = csv.DictWriter(text_file, keys, delimiter=' ', quoting=csv.QUOTE_ALL)
        dict_writer.writeheader()
        dict_writer.writerows(list_)


if __name__ == '__main__':
    pprint.pprint(ReadFBPosts().read_all_posts())

#save_all_posts_to_txt()
#save_all_posts_to_csv()
