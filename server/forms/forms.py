from flask import Blueprint, current_app as app, render_template, make_response
from ..models import db, User
from datetime import datetime as dt

# Blueprint configuration
form_bp = Blueprint(
    'form_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@form_bp.route('/forms/register')
def register():
    username = "test"
    email = "test@email"
    if username and email:
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="This is a test user",
            admin=False
        )
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{new_user} successfully created!")
    # return render_template(
    #     'register.html',
    #     static_folder = 'static'
    # )

@form_bp.route('/forms/login')
def login():
    return render_template(
        'login.html',
        static_folder = 'static'
    )

@form_bp.route('/forms/get_details')
def get_details():
    current_user = User.query.filter_by(username='test').first()
    return make_response(f"{current_user.email}")
