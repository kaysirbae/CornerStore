import myapp
from myapp.models import User
from myapp import db

user = User('admin','adminemail1@cornerstore.com')
user.set_password('Security1')
user.set_admin('True')
db.session.add(user)
db.session.commit()

agency = User('Default Agency','thisistheagency@cornerstore.com')
agency.set_password('password')
agency.set_agency('True')
db.session.add(agency)
db.session.commit()