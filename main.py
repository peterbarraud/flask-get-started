from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template("index.html")

@app.route('/hellothere/<firstname>/<lastname>', methods=['GET'])
def hellothere(firstname, lastname):
    return 'Hello ' + firstname + ' ' + lastname

@app.route('/squarethenumber/', methods=['POST'])
def squareit():
    number = int(request.form['pickanumber'])
    return 'And the square is: {}'.format(number*number)

if __name__ == "__main__":
    app.run()