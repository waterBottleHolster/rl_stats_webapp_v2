#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/venv_rl_webapp/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, \
    HiddenField, IntegerField, SelectField, BooleanField, TextAreaField, \
    RadioField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Regexp
from app.helper_objects import rl_vehicle_list, rl_gamemode_list
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
    partied = BooleanField(u'Partied Up?')
    team = SelectField(u'Team', choices=[('blue','Blue'),('orange','Orange'), ('club_colors','Club Colors')])
    vehicle = SelectField(u'Vehicle', choices=rl_vehicle_list)
    topper = BooleanField(u'Topper')
    antenna = BooleanField(u'Antenna')
    notes = TextAreaField(u'Notes')
    result = HiddenField(validators=[DataRequired()])
    gamemode = HiddenField(validators=[DataRequired()])
    fov = HiddenField(validators=[DataRequired()])
    distance = HiddenField(validators=[DataRequired()])
    height = HiddenField(validators=[DataRequired()])
    angle = HiddenField(validators=[DataRequired()])


class AnalyzeForm(FlaskForm):
    team = RadioField(u'Team', choices=[('Blue', 'BLUE'), ('Orange', 'ORANGE'), ('Club Colors', 'CLUB')])

    gamemode = SelectMultipleField(u'Game Mode', choices=rl_gamemode_list)

    vehicle = SelectMultipleField(u'Vehicle', choices=rl_vehicle_list)

    submit = SubmitField('Apply')