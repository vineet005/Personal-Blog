"""
Simple bootstrap site
"""
"""
To make an app basic framework.
run "/" and "/vin" differently to see their output respectively.
above line elements are called "endpoints"
"""


from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/about")
def hey():
    name="Vineet Thakran"
    return render_template('about.html',vin=name)


app.run(debug=True)