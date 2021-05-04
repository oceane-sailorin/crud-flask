import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from app import create_app, db,  sport
from app.sport import Wintersport

app = create_app('dev')


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        name = Wintersport(name=request.form.get("name"))
        db.session.add(name)
        db.session.commit()

    wintersports = Wintersport.query.all()
    return render_template("home.html", wintersports=wintersports)

@app.route("/update", methods=["POST"])
def update():
    newsport = request.form.get("newsport")
    currentsport = request.form.get("currentsport")
    wintersport = Wintersport.query.filter_by(name=currentsport).first()
    wintersport.name = newsport
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run()
