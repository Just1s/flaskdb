from app import db, Message, app
from flask import request, render_template

db.create_all()


@app.route('/')
def index():
    all_messages = Message.query.all()
    return render_template('messages.html', messages_list=all_messages)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        query = Message(name, email, message)
        db.session.add(query)
        db.session.commit()
        return render_template('greetings.html', vardas=name)
    elif request.method == 'GET':
        return render_template('login.html')


@app.route('/filtruoti', methods=['GET', 'POST'])
def filtras():
    if request.method == 'POST':
        email = request.form['email']
        all_messages = Message.query.filter_by(email=email)
        return render_template('filtruoti.html', email=email, messages_list=all_messages)
    elif request.method == 'GET':
        return render_template('ivest_email.html')


if __name__ == '__main__':
    app.run(debug=True)
