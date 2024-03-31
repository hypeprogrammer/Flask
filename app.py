# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import User
from werkzeub.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

if __name__ == "__main__":
	app.run(debug=True)
	
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route("/signup", methods=["GET", "POST"])
def sighup():
	form = RegistrationForm()
	if form.validata_on_submit():
		hashed_password = generate_password_hash(form.password.data)
		new_user = User(username=form.username.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		flash('계정생성완료')
		return redirect(url_for('login'))
	return render_template('signup.html', title='Sign Up', form=form)
	
