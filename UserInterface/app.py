from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cpsc408!@localhost/creditapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        email = request.form['email']

        cur = db.engine.connect()
        cur.execute("SELECT * FROM users WHERE userid = %s AND email = %s", (userid, email))
        account = cur.fetchone()

        if account:
            login_user(User(userid))
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form['userid']
        email = request.form['email']

        cur = db.engine.connect()
        cur.execute("INSERT INTO users (userid, email) VALUES (%s, %s)", (userid, email))
        db.session.commit()
        cur.close()

        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

from collections import defaultdict

@app.route('/dashboard')
@login_required
def dashboard():
    cur = db.engine.connect()
    cur.execute("SELECT * FROM transactions WHERE user_id = %s", (current_user.id,))
    transactions = cur.fetchall()
    cur.close()

    # Calculate the data for the pie chart
    category_totals = defaultdict(float)
    for transaction in transactions:
        category_totals[transaction['merchant_categoryid']] += transaction['amount']

    pie_chart_data = [
        {'category': category, 'total': total}
        for category, total in category_totals.items()
    ]

    # Calculate the data for the bar chart
    budget_totals = defaultdict(float)
    for transaction in transactions:
        budget_totals[transaction['budget_category']] += transaction['amount']

    bar_chart_data = [
        {'budget_category': category, 'total': total}
        for category, total in budget_totals.items()
    ]

    return render_template('dashboard.html', transactions=transactions, pie_chart_data=pie_chart_data, bar_chart_data=bar_chart_data)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
