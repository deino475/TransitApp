#Import Flask library and extensions
from flask import Flask, request, make_response

#Import Third-Party libraries
from dotenv import load_dotenv

#Import standard libraries
import os

#Import custom files
from models import db

load_dotenv(verbose=True)

app = Flask(__name__)

#APP CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#INITIALIZE APP EXTENSIONS
db.init_app(app)

@app.route('/', methods = ['GET'])
def index_view():
	return "{}".format(request.environ['REMOTE_ADDR'])

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)