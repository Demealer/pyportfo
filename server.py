from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        name = data["name"]
        response = data["response"]
        file = database.write(f'\n{name}, {email}, {response}')


def write_to_csv(info):
    with open('database2.csv', mode='a', newline='') as database2:
        email = info["email"]
        name = info["name"]
        response = info["response"]
        csv_w = csv.writer(database2, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_w.writerow([name, email, response])


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:sitename>')
def anysite(sitename):
    return render_template(sitename)


@app.route('/<username>/<int:post_id>')
def greetings(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to db.'
    else:
        return 'Something went wrong!'
