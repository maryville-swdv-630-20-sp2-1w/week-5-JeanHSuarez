
"""
Run with python3.
This singleton is used to connect to the database. 
There should just be one instance to connect to the db.
The said instance bears the credentials for the connection.
It can be checked that the same instance,
was used for the var connect_1 and connect_2 (Please see main function). 

"""

class Singleton(type):
   __instance = None

   def __init__(cls, dbname, username, password, **kwargs):
        super().__init__(dbname, username, password)
        cls._instance = None

   def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class MyConnection(metaclass=Singleton):
    
	def __init__(cls, dbname, username, password, **kwargs):
		cls.dbname = dbname
		cls.username = username
		cls.password = password

    
def main():
   connect_1 = MyConnection(dbname="mysql1", username="jsuarez", password="password")
   connect_2 = MyConnection(dbname="postgres1", username="jsuarez", password="password")
   print(connect_1 == connect_2)
   print (connect_1)

if __name__ == "__main__":
	
	main()

 