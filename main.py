import mysql.connector.errors as e

try:
    import file.py  #'file.py' to get the username and password for connecting database
except Exception:
    pass

try:
    import base.py  #'base.py' - base program
except e.ProgrammingError:
    print('''\nDirectory with the given credentials cannot be found
STATUS : Connection Unsuccessful!''')
except Exception:
    pass


