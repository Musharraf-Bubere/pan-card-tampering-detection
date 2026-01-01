from flask import Flask

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

from app.views import main   # ✅ IMPORT THE BLUEPRINT
app.register_blueprint(main)  # ✅ REGISTER IT