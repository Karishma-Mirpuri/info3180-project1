"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify
from forms import UserForm
from werkzeug.utils import secure_filename
from models import UserProfile
import smtplib, time


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="")
    
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    
    file_folder = app.config["UPLOAD_FOLDER"]
    #Validation not saving data to database.
    user_form = UserForm()
    
    
    if request.method =='POST': #and user_form.validate_on_submit():
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        gender = request.form['gender']
        biography = request.form['biography']
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        pic.save(os.path.join(file_folder, filename))
        
        user = UserProfile(date=time.strftime("%c"), first_name=firstname, last_name=lastname, age=age, gender=gender, biography=biography, pic=filename)
        db.session.add(user)
        db.session.commit()
        flash('Profile has been created!')
        return render_template('home.html')

    else:
        return render_template('profile.html')
        
@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    users = UserProfile.query.all()
    if request.method =='POST':#and request.headers['Content-Type'] == "application/json":
        list = [] 
        for user in users:
            list.append({'userid':user.id})
        return jsonify(users=list)
    else:
        return render_template('profiles.html', users=users)
    
@app.route('/profile/<int:id>')
def userProfile(id):
    users = UserProfile.query.filter_by(id=id).first()
    if request.method =='POST': #and request.headers['Content-Type'] == "application/json":
        jsonuser = {}
        jsonuser["id"] = users.id
        jsonuser["date"] = users.date
        jsonuser["age"] = users.age
        jsonuser["gender"] = users.gender
        jsonuser["biography"] = users.biography
        jsonuser["pic"] = users.pic
        return jsonify(jsonuser)
        #list = [{'userid':users.id, 'date':users.date, 'age':users.age, 'gender':users.gender, 'biography':users.biography, 'pic':users.filename}]
        #return jsonify(users=list)
    else:
        return render_template('userProfile.html', users=users)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")