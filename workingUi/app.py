from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Sample data for demonstration purposes only
users = {
    "user1": {
        "email": "user1@example.com",
        "credit_cards": [
            {"card_id": 1, "card_provider": "Visa"},
            {"card_id": 2, "card_provider": "Mastercard"}
        ],
        "transactions": [
            {"transaction_id": 1, "card_id": 1, "amount": 100, "category_id": 1, "date": "2023-05-01"},
            {"transaction_id": 2, "card_id": 1, "amount": 50, "category_id": 2, "date": "2023-05-02"},
        ]
    }
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["userid"]
        email = request.form["email"]
    
        if user_id in users and users[user_id]["email"] == email:
            session["user_id"] = user_id
            return redirect(url_for("dashboard"))
        else:
            flash("User not found or incorrect email")
            return render_template("login.html")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        flash("POST request received")
        return redirect(url_for("dashboard"))

    user_id = session["user_id"]
    return render_template("dashboard.html", user=users[user_id])


@app.route("/transaction_history")
@login_required
def transaction_history():
    return render_template("transactionhis.html")

@app.route("/budget_breakdown")
@login_required
def budget_breakdown():
    return render_template("bargraph.html")

@app.route("/spending_by_category")
@login_required
def spending_by_category():
    return render_template("pichart.html")

@app.route('/logout')
def logout():
    # your logout logic here
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    user = {
        'username': 'Chuck Norris',
        'name': 'Chuck Norris',
        'email': 'user1@example.com',
        'age': 30
    }
    return render_template('profile.html', title='Profile', user=user)

@app.route('/')
def index():
    return render_template('index.html', title='Home')


if __name__ == "__main__":
    app.run(debug=True)
