from flask import Flask, render_template, request, session, redirect, url_for, escape
import pymysql.cursors
import os
from urllib.parse import urlparse
import urllib.parse

app = Flask(__name__)
print("hello human")

#db_caretaker = PyMySQL.connect('localhost', 'root', 'Frogger4962', 'caretaker')
db_name = 'TeamBee'
host = 'localhost'
user = 'root'
password = 'Frogger4962'
db_port = 3306

print("before cleardb dtabase url parsing")
if ('CLEARDB_DATABASE_URL' in os.environ):
    url = os.environ.get('CLEARDB_DATABASE_URL')
    urllib.parse.uses_netloc.append('mysql')

    url = urlparse(url)
    db_name = url.path[1:]
    host = url.hostname
    user = url.username
    password = url.password
    host = url.hostname
    dbPort = url.port

print(host, db_port, user, password, db_name)

connection = pymysql.connect(  host = host,
                               port = db_port,
                               user = user,
                               password = password,
                               db = db_name,
                               charset = 'utf8mb4',
                               cursorclass = pymysql.cursors.DictCursor
                               )


@app.route('/')
def main():
    return render_template('index.html')



@app.route('/signup.html', methods =['GET', 'POST'])
def  signup_data():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        input_email = request.form['email']
        input_name = request.form['name']
        input_password = request.form['password']
        try:
            with connection.cursor() as cursor:
                """create a new record"""
                sql = "INSERT INTO `login` (`name`, `password`, `email`) VALUES (%s, %s)"
                cursor.execute(sql,(input_name, input_password, input_email))
                connection.commit()
        finally:
            connection.close()

        return(input_email, input_name, input_password)


@app.route('/login.html', methods = ['GET', 'POST'])
def login_data():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            input_email = request.form['email']
            input_password = request.form['password']
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `passwords`, FROM `login` WHERE `email`=%s"
                cursor.execute(sql, (input_email,))
                result = cursor.fetchone()
                stored_password = result['password']
                if input_password == stored_password:
                    session['email'] = request.form['email']
                    return redirect(url_for('index'))
                else:
                    print('password incorrect')

        finally:
            connection.close()


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


print("before if name")
if __name__ == "__main__":
    print("inside if name")
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, port=port)