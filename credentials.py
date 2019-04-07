class Credentials:
    """
    Class that generates new instances of user application credentials
    """

    credentials_list = []

    def __init__(self, account_name, account_user_name, account_password):
        '''
        __init__ method that defines properties for our credentials objects.
        '''

        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_password = account_password
