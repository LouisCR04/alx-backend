#!/usr/bin/env python3
# 7-app.py

""" i18n Exercises(Internationalization) """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime
from datetime import timezone as tmzn
from pytz import timezone
import pytz.exceptions

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Helps to configure available languages in the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

def get_user():
    """
    Returns a user dictionary or None if ID value can't be found
    or if 'login_as' URL parameter was not found
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None

def get_locale():
    """ Chooses best language using best_match from request module """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc

    if g.user:
        loc = g.user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc

    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc

@app.before_request
def before_request():
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    fmt = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(fmt)

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """
    Select and return appropriate timezone
    """
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return dflt

babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Default route """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
