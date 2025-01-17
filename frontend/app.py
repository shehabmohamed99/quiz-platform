from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

db_host = os.getenv('DB_HOST')
db_client = os.getenv('DB_CLIENT')
db_users = os.getenv('DB_USERS')
db_quizzes = os.getenv('DB_QUIZZES')
host = os.getenv("APP_HOST", "127.0.0.1")  
port = int(os.getenv("APP_PORT", 5000))


app.secret_key = os.urandom(24)

# MongoDB connection with your specific configuration
client = MongoClient('mongodb://{db_host}:27017/')
db = client['{db_client}']  # Updated database name
users = db['{db_users}']  # Collection reference
quizzes = db['{db_quizzes}']  # Collection reference

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashpass = generate_password_hash(request.form['password'])
            users.insert_one({
                'username': request.form['username'],
                'password': hashpass,
                'score': 0
            })
            return redirect(url_for('login'))
        
        flash('Username already exists!')
        return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_user = users.find_one({'username': request.form['username']})

        if login_user:
            if check_password_hash(login_user['password'], request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('index'))

        flash('Invalid username/password combination')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/quiz')
def quiz():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Convert cursor to list to make it reusable
    available_quizzes = list(quizzes.find())
    print("Found quizzes:", available_quizzes)  # Debug print
    return render_template('quiz.html', quizzes=available_quizzes)

@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        quiz_id = int(quiz_id)
    except ValueError:
        flash('Invalid quiz ID')
        return redirect(url_for('quiz'))

    quiz = quizzes.find_one({'_id': quiz_id})
    print("Found quiz:", quiz)  # Debug print
    
    if not quiz:
        flash('Quiz not found')
        return redirect(url_for('quiz'))
    
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = quiz['correct_option']
        
        score = 1 if user_answer == correct_answer else 0
        
        # Update user's score
        users.update_one(
            {'username': session['username']},
            {'$inc': {'score': score}}
        )
        
        if score == 1:
            flash('Correct answer! You earned 1 point!')
        else:
            flash(f'Wrong answer. The correct answer was option {correct_answer}.')
        return redirect(url_for('leaderboard'))
        
    return render_template('take_quiz.html', quiz=quiz)

@app.route('/leaderboard')
def leaderboard():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    leaders = users.find().sort('score', -1).limit(10)
    return render_template('leaderboard.html', leaders=leaders)

if __name__ == '__main__':
    app.run(host='host', port='port')