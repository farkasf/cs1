from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key'

users = {
    'marvin': {'password': 'marvin', 'balance': 1000},
    'hacker': {'password': 'hacker', 'balance': 0}
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('bank'))
        else:
            flash("Invalid credentials, please try again.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/bank')
def bank():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = session['username']
    balance = users[user]['balance']
    return render_template('bank.html', username=user, balance=balance)

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = int(request.form['amount'])
        recipient = request.form['recipient']
        sender = session['username']
        
        if sender in users and recipient in users:
            users[sender]['balance'] -= amount
            users[recipient]['balance'] += amount
            flash(f"Transferred ${amount} to {recipient}")
            return redirect(url_for('bank'))
    return render_template('transfer.html')

@app.route('/csrf_attack')
def csrf_attack():
    return render_template('csrf.html')

if __name__ == '__main__':
    app.run(debug=True)
