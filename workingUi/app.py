from flask import Flask, render_template, request, redirect, url_for, flash, session

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

# @app.route("/")
# def login():
#     return render_template("login.html")

@app.route('/')
def main_dashboard():
    return render_template('dashboard.html')

@app.route("/dashboard", methods=["POST"])
def dashboard():
    user_id = request.form["userid"]
    email = request.form["email"]
    
    if user_id in users and users[user_id]["email"] == email:
        session["user_id"] = user_id
        return render_template("dashboard.html", user=users[user_id])
    else:
        flash("User not found or incorrect email")
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
