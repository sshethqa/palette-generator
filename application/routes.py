from application import app, generate, db
from application.models import User, Palette, Colour
from application.forms import UserForm, PaletteForm
from flask import render_template, url_for, redirect, request
from os import getenv

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title='Home', hostname=getenv('HOSTNAME'))

@app.route('/palette', methods=['GET','POST'])
def get_palette():
    if request.method == 'GET':
        return redirect(url_for('home'))
    palette = generate.palette()
    name = generate.name()
    return render_template('index.html', title=name, palette=palette, hostname=getenv('HOSTNAME'))

# @app.route('/palette/add', methods=['GET','POST'])
# def add_palette():
#     form = PaletteForm()
#     palette = request.json()
#     if request.method == 'POST':
#         colours = []
#         for panel in palette['panels']:
#             colours.append(
#                 Colour(
#                     red = panel['colour']
#                 )
#             )

#         db.session.add(
#             user_name = form.user_name.data,
#             first_name = form.first_name.data,
#             last_name = form.last_name.data
#         )
#         db.session.commit()
#     return redirect(url_for('home'))

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About', hostname=getenv('HOSTNAME'))

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    form = UserForm()
    if request.method == 'POST':
        db.session.add(
            User(
                user_name = form.user_name.data,
                first_name = form.first_name.data,
                last_name = form.last_name.data
            )
        )
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_user.html', title='Add User', form=form, hostname=getenv('HOSTNAME'))
