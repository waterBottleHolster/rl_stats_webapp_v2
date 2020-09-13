import os
from app import create_app, db
from app.models import User, Role, game_event
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

# I'm not sure what the following lines do
#@app.shell_context_processor
#def make_shell_context():
#    return dict(db=db, User=User, Role=Role)