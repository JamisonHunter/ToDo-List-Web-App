# Jamison Hunter
# June 12, 2023
# todo_list

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder = "templates")

# tHis list of todos will be appended with multiple dictionaries.
todos = [{"task" : "Sample ToDo", "done" : False}]

@app.route("/")
def index():
    return render_template("index_html.html", todos = todos)

@app.route("/add", methods = ["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task" : todo, "done" : False})
    return redirect(url_for("index_html"))

# Implement editor here. 
  
if __name__ == "__main__":
    app.run(debug = True)
