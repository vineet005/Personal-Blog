"""
To make an app basic framework.
run "/" and "/vin" differently to see their output respectively.
above line elements are called "endpoints"
"""
#make static and template folder in webfla_sk folder
# static folder is public which will show the user all the files and folders which are used to make the website.
# template folder is private


# render_template is used to return a file as shown below

from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/about")
def hey():
    name="Vineet Thakran" #jinja templating(you can use this variable in your html code now by using {{variable_name }}
    return render_template('about.html',vin=name)


# app.run is used to run the app in all OSs and app.run(debug=True) is used to detect the change we have done automatically in the app.
app.run(debug=True)