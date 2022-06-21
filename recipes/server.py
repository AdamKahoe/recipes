from flask_app import app

from flask_app.controllers import users, recipes
from flask_app.models import user, recipe

if __name__=="__main__":
    app.run(debug=True)