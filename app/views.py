from app import app, db, request, flash, url_for, redirect, render_template
from app.models import Student

#@app.route('/')
#def show_all():
#	return render_template('show_all.html', students = Student.query.all())

#@app.route('/new', methods = ['GET', 'POST'])
#def new():
#	if request.method == 'POST':
#		if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#			flash('Please enter all the fields', 'error')
#		else:
#			student = Student(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])         
#			db.session.add(student)
#			db.session.commit()
#			flash('Record was successfully added', 'success')
#			return redirect(url_for('show_all'))
#
#	return render_template('new.html')


@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		if not request.form['email'] or not request.form['password']: 
			flash('Please enter all the fields', 'error')
		else:
			if str(request.form['email']) == str('admin') and str(request.form['password']) == str('admin'): 
				return redirect(url_for('show_users'))

	return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	print("1")
	if request.method == 'POST':
		print("2")
		#if not request.form['firstname'] or not request.form['lastname'] or not request.form['city'] or not request.form['address'] or not request.form['pincode'] or not request.form['email'] or not request.form['password']:
		#	print("3")
		#	flash('Please enter all the fields', 'error')
		#else:
		#	print("4")
		user = User(request.form['firstname'], request.form['lastname'], request.form['city'], request.form['address'], request.form['pincode'], request.form['email'], request.form['password'])
		print("5")
		db.session.add(user)
		print("6")
		db.session.commit()
		print("7")
		flash('Record was successfully added', 'success')
		print("8")
		return redirect(url_for('show_users'))

	print("9")
	return render_template('register.html')

@app.route('/show_users')
def show_users():
	return render_template('show_users.html', users = User.query.all())
