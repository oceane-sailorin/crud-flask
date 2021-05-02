import os
from flask import Flask
from flask import render_template
from flask import request
from app import create_app, db,  sport
from app.sport import Wintersport

app = create_app('dev')


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        name = Wintersport(wintersport=request.form.get("name"))
        db.session.add(name)
        db.session.commit()

    wintersports = Wintersport.query.all()
    return render_template("home.html", wintersports=wintersports)


if __name__ == '__main__':
    app.run()
