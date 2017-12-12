from app import db

class Student(db.Model):
	id = db.Column('student_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	city = db.Column(db.String(50))  
	addr = db.Column(db.String(200))
	pin = db.Column(db.String(10))

	def __init__(self, name, city, addr, pin):
		self.name = name
		self.city = city
		self.addr = addr
		self.pin = pin

	def __repr__(self):
		return '<Student %r>' % (self.name)


class User(db.Model):
	id = db.Column('user_id',db.Integer, primary_key=True)
	firstname = db.Column(db.String(64), index=True, unique=True)
	lastname = db.Column(db.String(64), index=True, unique=True)
	city = db.Column(db.String(50), index=True, unique=True)
	address = db.Column(db.String(200), index=True, unique=True)
	pincode = db.Column(db.String(10), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(120), index=True, unique=True)

	def __init__(self, firstname, lastname, city, address, pincode, email, password):
		self.firstname = firstname
		self.lastname - lastname
		self.city = city
		self.address = address
		self.pincode = pincode
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % (self.firstname)
