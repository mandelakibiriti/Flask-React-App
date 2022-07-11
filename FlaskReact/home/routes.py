from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/')
@home_bp.route('/home')
# Homepage
def home():
    return render_template (
        'index.html',
        title = "Hello React"
        )