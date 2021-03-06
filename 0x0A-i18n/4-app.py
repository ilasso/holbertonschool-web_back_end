#!/usr/bin/env python3
"""
1-app.py: basic app using babel
"""
from flask import Flask, jsonify, render_template, request
from flask_babel import Babel, gettext

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


@app.route('/', methods=['GET'], strict_slashes=False)
def main():
    """
    defines main route to the app and render html
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    """
    if request.args.get('locale') in cfg.LANGUAGES:
        return request.args.get('locale')
    return request.accept_languages.best_match(cfg.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
