from repository.repository import Repository


class Services(object):

    def __init__(self):
        self.repository = Repository()
    
    def get_users(self):
        return self.repository.get_users()