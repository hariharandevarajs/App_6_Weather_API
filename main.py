"""
first create for testing Purpose
"""


# from flask import Flask,render_template
#
# app = Flask("Website")
# @app.route("/home/")
# def home():
#     return render_template("tutorial.html")
# @app.route("/about/")
# def About():
#     return render_template("about.html")
# app.run(debug=True)

"""
Now we dont need those tutorial and 
about page - we were created for testing 
so remove from template folder or drag out from that folder 
and create home.html
"""

from flask import Flask,render_template

app = Flask("Website")
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<station>/<date>")
def About(station,date):
    template = 23
    return {"station":station,
            "date":date,
            "template":template}
app.run(debug=True)