# from flask import render_template
import connexion
import requests
import os

# Create the application instance
app = connexion.App(__name__, specification_dir='./configs')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

def controller():
    """ This is the test call requests to ping server 
    """
    GOTIFY_URL = os.getenv("gotify_url")
    GOTIFY_USER = os.getenv("gotify_user")
    GOTIFY_password = os.getenv("gotify_password")

    r = requests.get(GOTIFY_URL)

    print(r.text)


# Create a URL route in our application for "/"
#@app.route('/')
#def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
 #   return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)