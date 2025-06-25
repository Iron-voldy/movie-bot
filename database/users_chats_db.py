from pymongo import MongoClient
from info import DATABASE_NAME, DATABASE_URI, IMDB, IMDB_TEMPLATE, MELCOW_NEW_USERS, P_TTI_SHOW_OFF, SINGLE_BUTTON, SPELL_CHECK_REPLY, PROTECT_CONTENT

class Database:
    
    def __init__(self, uri, database_name):
        self._client = MongoClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.grp = self.db.groups
        self.req = self.db.requests
        self.sttg = self.db.settings

    def new_user(self, id, name):
        return dict(
            id=id,
            name=name
        )

    def new_group(self, id, title):
        return dict(
            id=id,
            title=title
        )

    async def add_user(self, id, name):
        user = self.new_user(id, name)
        self.col.insert_one(user)

    async def find_join_req(self, id):
        return bool(self.req.find_one({'id': id}))

    async def add_join_req(self, id):
        self.req.insert_one({'id': id})

    async def del_join_req(self):
        self.req.drop()

    async def is_user_exist(self, id):
        user = self.col.find_one({'id': int(id)})
        return bool(user)

    async def total_users_count(self):
        return self.col.count_documents({})


    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        self.col.delete_many({'id': int(user_id)})

    async def add_chat(self, chat, title):
        chat_data = self.new_group(chat, title)
        self.grp.insert_one(chat_data)

    async def get_chat(self, chat):
        chat = self.grp.find_one({'id': int(chat)})
        return bool(chat)
    
    async def get_sttg(self):
        return self.sttg.find_one({'_id': 'sttg'})

    async def update_sttg(self, sttg):
        if not self.sttg.find_one({'_id': 'sttg'}):
            self.sttg.insert_one({'_id': 'sttg'})
        self.sttg.update_one({'_id': 'sttg'}, {'$set': sttg})

    async def total_chat_count(self):
        return self.grp.count_documents({})

    async def get_all_chats(self):
        return self.grp.find({})

    async def get_db_size(self):
        return self.db.command("dbstats")['dataSize']


db = Database(DATABASE_URI, DATABASE_NAME)
