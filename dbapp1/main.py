from app import db, Message, app
from flask import request, render_template

db.create_all()


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


if __name__ == '__main__':
    app.run(debug=True)
