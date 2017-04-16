import facebook
import csv

app_id='119610841474711'
app_secret='acd9a657733dd91434a6f94df2f71124'

USER_ID = '1546116578732756'

class ReadFBPosts():

    def get_access_token(self):
        """
        get access token tot FB page by app_id and app_secret
        app_id and app_secret from https://developers.facebook.com

        """
        return facebook.GraphAPI.get_app_access_token(facebook.GraphAPI, app_id, app_secret, offline=True)



    def connect_to_fb(self):
        return facebook.GraphAPI(access_token=self.get_access_token(), version=2.7)


    # def add_fb_post():
    #     return connect_to_fb().put_object(parent_object=USER_ID, connection_name='feed',
    #                  message='FB API works!')

    def read_all_posts(self):
        """read user feed by user id"""
        return ReadFBPosts().connect_to_fb().get_connections(id=USER_ID, connection_name='feed')


    def save_all_posts_to_txt(self):
        posts = ReadFBPosts().read_all_posts()
        list = posts['data']
        with open('posts.txt', 'wt') as text_file:
            for line in list:
                text_file.write(str(line) + '\n')


    def save_all_posts_to_csv(self):
        posts = ReadFBPosts().read_all_posts()
        list = posts['data']
        keys = ['story', 'message', 'created_time', 'id']
        with open('posts.csv', 'wt') as text_file:
            dict_writer = csv.DictWriter(text_file, keys, delimiter=' ', quoting=csv.QUOTE_ALL)
            dict_writer.writeheader()
            dict_writer.writerows(list)


print(ReadFBPosts.read_all_posts(ReadFBPosts))

ReadFBPosts.save_all_posts_to_txt(ReadFBPosts)
ReadFBPosts.save_all_posts_to_csv(ReadFBPosts)
