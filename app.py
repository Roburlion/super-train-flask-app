#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, render_template, jsonify

app = Flask(__name__)

list = ["a", "b", "c"]

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/templates")
def templates():
    return render_template("template.html", list=list)

@app.route("/api")
def api():
    response = {
        "message": "API response"
    }
    return jsonify(response)