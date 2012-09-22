from handlers.base import BaseHandler
from tornado.web import RequestHandler

import psycopg2

import logging
logger = logging.getLogger('boilerplate.' + __name__)

try:
	conn = psycopg2.connect("dbname=address_book_db user=convolu")
except:
	print "Could not connect to address_book_db"

class WelcomeHandler(BaseHandler):
    def get(self):
        self.render("index.html")

    def post(self):
       	self.write("this is a handler")

class CreateUserHandler(BaseHandler):
	def get(self):
		self.render("user.html")

class AddContactHandler(BaseHandler):
	def get(self):
		self.write("this is a handler")

class ViewAddressBookHandler(BaseHandler):
	def get(self):
		cur = conn.cursor()

		cur.execute("SELECT * from USERS2")

		users = cur.fetchall()

		cur.close()


		#import pdb; pdb.set_trace()

		self.render("viewusers.html", users=users)


class AddCustomerHandler(BaseHandler):
	def post(self):
		firstname = self.get_arguments('firstname', strip=True)
		lastname  = self.get_arguments('lastname', strip=True)
		email     = self.get_arguments('email', strip=True)

		cur = conn.cursor()

		cur.execute("INSERT INTO USERS2 (name, surname, email) VALUES (%s, %s, %s)", (firstname, lastname, email))

		conn.commit()

		cur.close()