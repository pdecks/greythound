"""Application Engineer Coding Exercise for Slack
by Tricia Decker 12/5/2015
"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# raise an error if undefined variable used in Jinja2
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage."""

    return render_template('home.html')


@app.route('/calvin')
def show_cal():
    """Calvin's Profile."""

    return render_template('calvin.html')


@app.route('/hobbes')
def show_hobbes():
    """Hobbes' Profile."""

    return render_template('hobbes.html')


if __name__ == "__main__":

    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()