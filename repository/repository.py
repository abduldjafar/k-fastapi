from config.config import Config



class Repository(object):
    def __init__(self):
        self.database = Config()
        self.database.init()

    def __change_list_of_objectid_to_str(self,list_of_dicts):
        for data in list_of_dicts:
            data.update((key, str(value)) for key, value in list_of_dicts.items() if key == "_id")
        return list_of_dicts

    def get_users(self):
        datas = [data for data in self.database.user.find()]
        
        return self.__change_list_of_objectid_to_str(datas)
