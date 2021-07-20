from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


## Initialize App and Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfB76O6dobzWlSihBXox7C0sKlR6b'
Bootstrap(app)

todo_tasks = ['Do Laundry', 'Do Check-ins', 'Wipe Counters', 'Vacuum']
completed_tasks = []


## Short Form to Add Tasks
class AddForm(FlaskForm):
    task = StringField(label="Task To Add:", validators=[DataRequired()])
    submit = SubmitField(label="+")


@app.route('/', methods = ["GET", "POST"])
def home():
    form = AddForm()

    if form.validate_on_submit():
        todo_tasks.append(request.form.get("task"))
        return redirect(url_for('home'))

    return render_template("index.html", todo_tasks=todo_tasks, completed_tasks=completed_tasks, form=form)


@app.route('/complete/<task>')
def complete(task):
    completed_tasks.append(task)
    todo_tasks.remove(task)
    return redirect(url_for('home'))

@app.route('/decomplete/<task>')
def decomplete(task):
    todo_tasks.append(task)
    completed_tasks.remove(task)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)