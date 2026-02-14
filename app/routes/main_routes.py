from flask import render_template
from flask_login import login_required, current_user
from app.routes import main_bp


@main_bp.route('/')
@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)
