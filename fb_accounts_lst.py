def get_fb_accounts(fb_accounts_lst=None):

    """
    Read text file with URL addresses and return a list with these addresses.

    Example:
        file.txt:
    https://www.facebook.com/example_1
    https://www.facebook.com/example_2
        list:
    [https://www.facebook.com/example_1\n, https://www.facebook.com/example_2]
    """

    if fb_accounts_lst is None:
        fb_accounts_lst = []
    with open('fb_accounts.txt', 'r') as fb_accounts:
        for line in fb_accounts:
            fb_accounts_lst.append(line)
    return(fb_accounts_lst)