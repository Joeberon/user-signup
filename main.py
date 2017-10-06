from flask import Flask, request, redirect
import cgi
import os
import jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods= ['POST'])
def sign_up():
    user = request.form['username']
    pw=request.form['password']
    vp=request.form['verify password']
    email=request.form['email']
    userError=""
    pwError=""
    vpError=""
    emailError=""
    if user=="" or len(user) < 3 or len(user) > 20:
        userError="Must be greater than 3 characters or less than 20."

    if pw=="" or len(pw) <3 or len(pw) > 20:
        pwError="Must be greater than 3 characters or less than 20."

    if vp != pw:
        vpError="must be the same as your password."
    if email:
        if len(email) < 3 or len(user) > 20:
            emailError="Must be greater than 3 characters or less than 20."
        if "@" not in email or "." not in email:
            emailError="must have one '@' and one '.'"
        email.count('@')
        email.count(".")
    if userError or pwError or vpError or emailError:
        template=jinja_env.get_template("username.html")
        return template.render(userError=userError,
                                        pwError=pwError, vpError=vpError,emailError=emailError)
    template= jinja_env.get_template('hello_form.html')
    return template.render(name=user)

    return template.render()

@app.route('/', methods=['GET'])
def index():
    template = jinja_env.get_template('username.html')
    return template.render()


app.run()