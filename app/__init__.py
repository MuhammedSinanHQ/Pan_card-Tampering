from flask import Flask
import os

app = Flask(__name__)

# Use ProductionConfig when FLASK_ENV is production, otherwise use DevelopmentConfig
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

from app import views
  