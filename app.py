from flask import Flask 

from routes.main_routes import main
from routes.blog_routes import blog 
from routes.auth_routes import auth 

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(auth)

app.register_blueprint(blog, url_prefix="/blog")

if __name__ == "__main__":
    app.run(debug=True)
