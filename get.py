import sqlite3
import getpass
from django.middleware.csrf import CsrfViewMiddleware
#u = input('User: ')
p = getpass.getpass('Password: ')

# Connect to database
db = sqlite3.connect('db.sqlite3')
c = db.cursor()

# Execute sql statement and grab all records where the "usuario" and
# "senha" are the same as "user" and "password"
#c.execute('SELECT * FROM auth_user WHERE username = ?', (u))
c.execute('SELECT * FROM auth_user WHERE passwd = ?', (p))
# If nothing was found then c.fetchall() would be an empty list, which
# evaluates to False 
if c.fetchall():
    print('Welcome')
else:
    print('Login failed')