from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/medical_records"
app.config["MONGO_URI"] = "mongodb+srv://2004gayi:medi@cluster0.epaknql.mongodb.net/medical_records"
app.secret_key = 'your_secret_key'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = generate_password_hash(request.form['pass'])
            users.insert_one({
                'name': request.form['username'],
                'password': hashpass,
                'email': request.form['email'],
                'user_type': request.form['user_type']
            })
            session['username'] = request.form['username']
            return redirect(url_for('profile'))

        flash('Username already exists. Please choose a different one.')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if check_password_hash(login_user['password'], request.form['pass']):
                session['username'] = request.form['username']
                return redirect(url_for('index'))

        flash('Invalid username/password combination.')
    return render_template('login.html')


@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    users = mongo.db.users
    user = users.find_one({'name': session['username']})

    if request.method == 'POST':
        appointment = {
            'user_id': user['_id'],
            'username': session['username'],
            'specialist': request.form['specialist'],
            'doctor': request.form['doctor'],
            'date': request.form['date'],
        }

        mongo.db.appointments.insert_one(appointment)

        flash('Appointment created successfully.')
        return redirect(url_for('appointments'))

    appointments = mongo.db.appointments.find({'user_id': user['_id']})

    return render_template('appointments.html', appointments=appointments)

@app.route('/my_appointments')
def my_appointments():
    if 'username' not in session:
        return redirect(url_for('login'))

    users = mongo.db.users
    user = users.find_one({'name': session['username']})
    appointments = mongo.db.appointments.find({'user_id': user['_id']})

    return render_template('my_appointments.html', appointments=appointments)

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    users = mongo.db.users
    user = users.find_one({'name': session['username']})

    appointments = mongo.db.appointments.find({'user_id': user['_id']})

    return render_template('profile.html', user=user, appointments=appointments)



@app.route('/health_details')
def health_details():
    return render_template("health_details.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)