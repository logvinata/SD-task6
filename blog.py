"""You are to implement 3 types of pages in your Blog App:
1. Main page: displaying posts list, link to each post, link to new post creation page.
2. Post page: a post header, its contents, automatically generated creation date.
    Links to the main page and new post creation page.
3. New post creation page: a form with a header and post contents. Link to the main page.

Notes:
1. There should be navigation between pages in your App, as mentioned.
2. You shouldn't use any database or dive into html layout – the purpose of this assignment is to get acquainted
    with flask's methods.
3. HTML-page example:
    https://github.com/girafe-ai/msai-python/blob/master/week11_django/seminar/testsite/leads/templates/index.html – feel free to use and modify.
4. HTML elements:
    https://www.w3schools.com/TAGS/default.ASP, https://developer.mozilla.org/en-US/docs/Web/HTML/Element
5. Solution should be presented as an opened Pull Request in your GitHub repository from the branch with task solution
    to the branch without task solution."""

# thanks to https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2&t=673s
# for the really helpful video

# to lunch: write in conda terminal
# set FLASK_APP=blog.py
# flask run
# get "Running on http://127.0.0.1:5000 (Press CTRL+C to quit)"
# use http://localhost:5000/
# in case of changes - stop the server and run again
# alternatively - use debug mode
# stop server; set FLASK_DEBUG=1; run server

# import flask

from flask import Flask, render_template, url_for, flash, redirect, request
import forms

app = Flask(__name__)  # instantiate application

posts = [
    {
        "author": "to_Kima",
        "title": "Blog Post 1",
        "content": "Lorem ipsum dolor sit amet",
        "date": "April 1, 2022",
    },
    {
        "author": "to_Kima",
        "title": "Blog Post 2",
        "content": "consectetur adipiscing elit",
        "date": "April 1, 2022",
    }

]


@app.route('/')  # home page
@app.route('/home')
def home():
    return render_template("home.html", posts=posts, title="Home Page")


@app.route('/contacts')  # contacts page
def contacts():
    return render_template("contacts.html", title="Contacts")


@app.route('/post/new', methods=['GET', 'POST'])  # contacts page
def new_post():
    form = forms.PostForm()
    if form.validate_on_submit():
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template("new_post.html", title="New Post", form=form)


if __name__ == '__main__':  # this is instead of CLI commands to run in debug mode
    app.run(debug=True)
# use python route\file.py to lunch
