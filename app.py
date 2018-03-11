from flask import Flask, render_template, request, session, redirect, url_for, escape
import pymysql.cursors

app = Flask(__name__)

#db_caretaker = PyMySQL.connect('localhost', 'root', 'Frogger4962', 'caretaker')
connection = pymysql.connect(host='localhost',
                               user = 'root',
                               password = 'Frogger4962',
                               db = 'TeamBee',
                               charset = 'utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor
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


if __name__ == "__main__":
	app.run()