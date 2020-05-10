import mysql.connector as connector


class SQLConnector:
    def __init__(self, data=None):
        self.data = data
        connection_ = {"host": "192.168.43.65",
                       "user": "pacuser",
                       "password": "pacuser"
                       }
        self.connection = connector.connect(**connection_).cursor()
    
    def show_dbs(self):
        self.connection.execute("SHOW DATABASES")
        for i in self.connection:
            print(i)
        
    def write_db(self, data):
        
        pass
    
    def read_db(self, data):
        pass
    
    def update_db(self, data):
        pass
    
    def delete_db(self, data):
        pass


if __name__ == '__main__':
    x = SQLConnector()
    x.show_dbs()
