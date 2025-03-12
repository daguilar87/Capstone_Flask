from flask import Flask

from config import Config

from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/shop*": {"origins": "*"}})
cors = CORS(app, resources={r"/shops*": {"origins": "*"}})
cors = CORS(app, resources={r"/shop/<productid>*": {"origins": "*"}})
cors = CORS(app, resources={r"/api/contact*": {"origins": "*"}})


login = LoginManager()
moment = Moment(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
# set up a re-route for unauthorized access
login.login_view = 'auth.loginPage'

from . import routes