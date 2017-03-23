from flask import Flask, request, render_template, redirect, flash, url_for

import hackbright

app = Flask(__name__)
app.secret_key = 'screaming_darkness'


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    first_name, last_name, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html") 


@app.route("/student-add")
def student_add():
    """Add a student."""

    return render_template("make_student.html")

@app.route("/student-added", methods=['POST'])
def added():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)
    flash("Thanks for entering a new student!")

    # url_for e
    print url_for('get_student', github=github)
    return redirect(url_for('get_student', github=github))


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
