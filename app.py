from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup.html', methods =['GET', 'POST'])
def  get_request():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        print('got post request')
        print(request.form)
        


if __name__ == "__main__":
	app.run()