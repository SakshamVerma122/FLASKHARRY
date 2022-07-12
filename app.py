from flask import Flask,render_template

# Here a flask app is created
app = Flask(__name__)

# These are related to decorators with parameters
# These are different routes to pages

# This is the home page
@app.route('/')
def hello_world():
    # return render_template("index.html")
    return 'Hello, World!'

@app.route("/renderedpage")
def renderedpage():
    return render_template("Rendertemp.html")


@app.route('/product')
def product():
    return 'product routed'

# This is debug the app
if __name__ == "__main__":
    # Debug is true as to get errors in browser only just like any webdevelopement app
    app.run(debug = True,port=8000)