from flask import render_template,redirect,url_for, flash,request
from . import auth
from flask_login import login_user
from ..models import User
from .forms import LoginForm,RegistrationForm,AdminRegistrationForm,AdminLoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message






@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "online shopping login"
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data,role=form.role.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to blog","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))



@auth.route('/adminLogin',methods=['GET','POST'])
def login_admin():
    adminLogin_form = AdminLoginForm()
    if adminLogin_form.validate_on_submit():

        user = User.query.filter_by(email = adminLogin_form.email.data).first()
        if user is not None and user.verify_password(adminLogin_form.password.data):
            login_user(user,adminLogin_form.remember.data)
            return redirect(request.args.get('next') or url_for('auth.admin'))

        flash('Invalid username or Password')
       

    return render_template('auth/adminLogin.html',adminLogin_form = adminLogin_form)

@auth.route('/admin')
def admin():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to Online shopping dashboard'
    return render_template('auth/admin.html',title = title)


@auth.route('/adminregister',methods = ["GET","POST"])
def register_admin():
    form =  AdminRegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data, role=form.role.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to online shopping","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login_admin'))
    return render_template('auth/adminregister.html',adminRegistrationForm = form)

@auth.route('/adminLogout')
@login_required
def logout_admin():
    logout_user()
    return redirect(url_for("main.index"))


# @auth.route('/result')
# @roles_accepted('/admin')
# def result():
#     if not current_user.is_authenticated:
#         return redirect(url_for('.login'))
#     else:
#         return redirect(url_for('admin/user/'))