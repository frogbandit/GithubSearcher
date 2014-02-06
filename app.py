from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True 

@app.route("/")
def hello():
	return render_template("hello.html")


@app.route("/name")

def name():
	return "James"

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		response = requests.get(url)
		response_dict = response.json()
		return render_template("results.html", api_data=response_dict)
	if request.method == "GET":
		return render_template("search.html")
	
if __name__ == "__main__" : 
	app.run(host="0.0.0.0")
