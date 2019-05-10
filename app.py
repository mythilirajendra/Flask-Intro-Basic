from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)

@app.route('/shopping')
def shopping():
    food = ['Salads', 'Fruits', 'Oatmeal', 'Juice', 'Sandwich']
    return render_template("shopping.html", food=food)

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)

@app.route('/post/<int:post_id>')
def show_id(post_id):
    return '<h2>Your ID is %d</h2>' %post_id

@app.route('/beach', methods=['GET','POST'])
def sand():
    if request.method == 'POST':
        return '<h2>You are using</h2><h3> POST </h3><h2>method</h2'
    else:
        return "<h2> You're using: %s" %request.method


if __name__ == '__main__':
    app.run(debug=True)
