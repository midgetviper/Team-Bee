from flask import Flask, render_template, request, redirect, url_for, session
import pymysql.cursors

app = Flask(__name__)

# db_caretaker = PyMySQL.connect('localhost', 'root', 'Frogger4962', 'caretaker')
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Frogger4962',
                             db='TeamBee',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )
@app.route('/')
def main():
    #    username = request.cookies.get('username')
    # username = session['username']
    return render_template('index.html')


@app.route('/signup.html', methods=['GET', 'POST'])
def signup_data():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        input_email = request.form['email']
        input_name = request.form['name']
        input_password = request.form['password']
        try:
            with connection.cursor() as cursor:
                """create a new record"""
                sql = 'INSERT INTO Caretaker (`email`, `password`, `name`) VALUES(%s, %s, %s)'
                cursor.execute(sql, (input_email, input_password, input_name))
                connection.commit()
                return redirect(url_for('main'))

        finally:
            return

        # return(input_email, input_name, input_password)


"""Need to compare a database entry and a string sensibly"""
@app.route('/login.html', methods=['GET', 'POST'])
def login_data():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `password` FROM `Caretaker` WHERE `email`=%s"
                cursor.execute(sql, request.form['email'])
                result = cursor.fetchone()
            print(result['password'])
            if result['password'] == request.form['password']:
                #session['username'] = input_email
                return render_template('home.html')
            else:
                return redirect(url_for('main'))
        finally:
            return


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('logout.html')


"""takes patient phone no. name and creates an id which it then stored in the database"""


@app.route('/PatientRegistration.html', methods=['GET', 'POST'])
def patient_registration():
    if request.method == 'GET':
        return render_template('/PatientRegistration.html')
    elif request.method == 'POST':
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO Patient (`name`, `phoneNumber`) VALUES(%s, %s)'
                cursor.execute(sql, (request.form['name'], request.form['number']))
                result = cursor.fetchnone()
                print(result['id'])
                result['id'] = cursor.lastrowid()
                connection.commit()
            return render_template('/thankYou.html')

        finally:
            return "fail"

"""secret keys"""
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()