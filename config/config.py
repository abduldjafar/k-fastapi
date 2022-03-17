from webbrowser import get
from toml import load
from pymongo import MongoClient
import pymongo


class Config(object):
    __mongodb_host = None
    __mongodb_port = None
    __mongodb_db = None
    __mongodb_user = None
    __mongodb_password = None

    def __init__(self):
        self.config = load("config.toml")
        Config.__mongodb_host = self.config["mongodb"]["url"]
        Config.__mongodb_port = self.config["mongodb"]["Port"]
        Config.__mongodb_db = self.config["mongodb"]["database"]
        Config.__mongodb_user = self.config["mongodb"]["user"]
        Config.__mongodb_password = self.config["mongodb"]["password"]
        self.mongoconn = None
        self.user=self.config["collections"]["users"]
        self.vendor=self.config["collections"]["vendor"]
        self.item=self.config["collections"]["item"]
        self.address=self.config["collections"]["address"]
        self.questions=self.config["collections"]["questions"]
        self.house_part=self.config["collections"]["house_part"]
        self.house_part_category=self.config["collections"]["house_part_category"]
        self.house_part_subcategory=self.config["collections"]["house_part_subcategory"]
        self.Items_sku=self.config["collections"]["Items_sku"]
        self.chart=self.config["collections"]["chart"]
        self.checkout=self.config["collections"]["checkout"]
        self.checkout_id=self.config["collections"]["checkout_id"]
        self.transaction=self.config["collections"]["transaction"]
        self.content=self.config["collections"]["content"]
        self.content_tags=self.config["collections"]["content_tags"]
        self.content_sub_tags=self.config["collections"]["content_sub_tags"]
        self.content_sub_sub_tags=self.config["collections"]["content_sub_sub_tags"]
        self.mico_values=self.config["collections"]["mico_values"]
        self.bad_item=self.config["collections"]["bad_item"]
        self.country=self.config["collections"]["country"]
        self.admin=self.config["collections"]["admin"]
        self.persona_question=self.config["collections"]["persona_question"]
        self.persona_answer=self.config["collections"]["persona_answer"]
        self.persona_bucket=self.config["collections"]["persona_bucket"]
        self.country_city=self.config["collections"]["country_city"]
        self.user_persona_answer=self.config["collections"]["user_persona_answer"]
        self.persona=self.config["collections"]["persona"]

    
    def get_mongodb_host(self):
        return Config.__mongodb_host
    
    def get_mongodb_port(self):
        return Config.__mongodb_port
    
    def get_mongodb_db(self):
        return Config.__mongodb_db
    
    def get_mongodb_user(self):
        return Config.__mongodb_user
    
    def get_mongodb_password(self):
        return Config.__mongodb_password
    
    def __set_mongodb_conn(self):
        CONNECTION_STRING = "mongodb+srv://{}:{}@{}/myFirstDatabase".format(self.get_mongodb_user(),self.get_mongodb_password(),self.get_mongodb_host())
        client = MongoClient(CONNECTION_STRING)
        self.mongoconn = client[self.get_mongodb_db()]

    
    def __set_collections(self):
        self.user=self.mongoconn[self.user]
        self.vendor=self.mongoconn[self.vendor]
        self.item=self.mongoconn[self.item]
        self.address=self.mongoconn[ self.address]
        self.questions=self.mongoconn[self.questions]
        self.house_part=self.mongoconn[self.house_part]
        self.house_part_category=self.mongoconn[self.house_part_category]
        self.house_part_subcategory=self.mongoconn[self.house_part_subcategory]
        self.Items_sku=self.mongoconn[self.Items_sku]
        self.chart=self.mongoconn[self.chart]
        self.checkout=self.mongoconn[self.checkout]
        self.checkout_id=self.mongoconn[self.checkout_id]
        self.transaction=self.mongoconn[self.transaction]
        self.content=self.mongoconn[self.content]
        self.content_tags=self.mongoconn[self.content_tags]
        self.content_sub_tags=self.mongoconn[self.content_sub_tags]
        self.content_sub_sub_tags=self.mongoconn[self.content_sub_sub_tags]
        self.mico_values=self.mongoconn[self.mico_values]
        self.bad_item=self.mongoconn[self.bad_item]
        self.country=self.mongoconn[self.country]
        self.admin=self.mongoconn[self.admin]
        self.persona_question=self.mongoconn[self.persona_question]
        self.persona_answer=self.mongoconn[self.persona_answer]
        self.persona_bucket=self.mongoconn[self.persona_bucket]
        self.country_city=self.mongoconn[self.country_city]
        self.user_persona_answer=self.mongoconn[self.user_persona_answer]
        self.persona=self.mongoconn[self.persona]
    
    def init(self):
        self.__set_mongodb_conn()
        self.__set_collections()
    
    
    


