class FBAccountsError(Exception):
    pass


def get_fb_accounts(filename='fb_accounts.txt'):

    """
    Read text file with URL addresses and return a list with these addresses.

    Example:
        file.txt:
    https://www.facebook.com/example_1
    https://www.facebook.com/example_2
        list:
    ['https://www.facebook.com/example_1', 'https://www.facebook.com/example_2']
    """
    try:
        with open(filename, 'r') as fb_accounts:
            return fb_accounts.read().split('\n')
    except FileNotFoundError:
        raise FBAccountsError
