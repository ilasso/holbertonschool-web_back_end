#!/usr/bin/env python3
"""
1-app.py: basic app using babel
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    config babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


cfg = Config()
app.config['BABEL_DEFAULT_LOCALE'] = cfg.BABEL_DEFAULT_LOCALE
app.config['BABEL_DEFAULT_TIMEZONE'] = cfg.BABEL_DEFAULT_TIMEZONE

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=['GET'], strict_slashes=False)
def main():
    """
    defines main route to the app and render html
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    by this priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    """
    # 1 - from url parameters
    if request.args.get('locale') in cfg.LANGUAGES:
        return request.args.get('locale')
    # 2 - from user settings
    try:
        lang = g.user.get('locale')
        if lang in cfg.LANGUAGES:
            return g.user['locale']
    except AttributeError:
        pass
    # 3 from request header
    if request.headers.get('locale'):
        return request.headers.get('locale')
    # 4 default locale
    return request.accept_languages.best_match(cfg.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """ getting timezone"""
    try:
        tmz = pytz.timezone(request.args.get('timezone'))
        return tmz
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    try:
        stmz = g.user.get('timezone')
        tmz = pytz.timezone(stmz)
        return tmz
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    except AttributeError:
        pass
    print(f"default")
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """ get user by ID"""
    try:
        user_id = request.args.get('login_as')
        return users[int(user_id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """before request"""
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
