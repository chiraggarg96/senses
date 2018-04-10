from flask import Flask,render_template, request
from scrape_test import start_work
app = Flask(__name__)


@app.route('/')
def main():
     
     return render_template('register.html')


@app.route('/handle_data', methods=['POST'])
def reply():
     x = request.form['inputID']
     sample=start_work(x)
     print(sample)
     return render_template('out.html',plane=sample)



if __name__ == "__main__":
	app.run(port=5004)