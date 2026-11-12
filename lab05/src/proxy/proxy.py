from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def query(self, sql):
        pass

class RealDatabase(Database):
    def query(self, sql):
        print("Executing query:", sql)

class DatabaseProxy(Database):
    def __init__(self, has_access):
        self.real_database = RealDatabase()
        self.has_access = has_access
    def query(self, sql):
        if self.has_access:
            self.real_database.query(sql)
        else:
            print("Access denied. Query cannot be executed.")