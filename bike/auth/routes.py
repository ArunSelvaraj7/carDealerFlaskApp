from bike.auth import auth
from flask import render_template,request,redirect,flash,url_for
from bike.auth.forms import Registration_form, Login_form
from bike.auth.models import Users
from bike import login_manager,bcrypt
from flask_login import login_user,logout_user,login_required

@auth.route('/register', methods=['GET','POST'])
@login_required
def register():
    form=Registration_form()
    if form.validate_on_submit():
        Users.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('auth.do_the_login'))
    return render_template('register.html',form=form)


@auth.route('/login', methods=['GET','POST'])
def do_the_login():
    form=Login_form()
    if form.validate_on_submit():
        user=Users.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash("Invalid credentials! Please try again")
            return redirect(url_for('auth.do_the_login'))
        login_user(user,remember=form.stay_logged_in.data)
        flash('Logged in successfully!')
        return redirect(url_for('main.display_route'))
    return render_template('login.html',form=form)

@auth.route('/logout')
@login_required
def do_the_logout():
    logout_user()
    flash("Signed out successfully!")
    return redirect(url_for('main.display_route'))

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

