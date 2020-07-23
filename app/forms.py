#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/venv_rl_webapp/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, HiddenField, IntegerField, SelectField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Regexp
import sqlite3
db_path = 'rl_stats.db'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('SIGN IN')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
                message='Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords must match.")
    ])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('REGISTER')

    
    def validate_username(self, username):
        #user = User.query.filter_by(username=username.data).first()
        conn = sqlite3.connect(db_path)
        cur = conn.execute("SELECT * FROM users WHERE username=?", (username.data,))
        if cur.fetchone() is not None:
            raise ValidationError('Please use a different username.')
        conn.close()

class GameDataForm(FlaskForm):
    gamemode = HiddenField('Game Mode', validators=[DataRequired()])
    partied = BooleanField('Partied')
    fov = IntegerField('FOV')
    team = SelectField("Team", choices=[('Blue'),('Orange'),('Club Colors')])