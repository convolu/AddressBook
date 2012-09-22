from handlers.foo import FooHandler
from handlers.welcome import WelcomeHandler, \
	CreateUserHandler, AddContactHandler, ViewAddressBookHandler, \
	AddCustomerHandler

url_patterns = [
    (r"/", WelcomeHandler),
    (r"/createuser", CreateUserHandler),
    (r"/addcontact", AddContactHandler),
    (r"/viewaddressbook", ViewAddressBookHandler),
    (r"/addcustomer", AddCustomerHandler),
]
