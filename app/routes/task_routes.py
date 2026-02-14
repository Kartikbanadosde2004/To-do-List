from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Task
from app.routes import main_bp


@main_bp.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    priority = request.form.get('priority', 'medium')
    
    if not title:
        flash('Task title is required')
        return redirect(url_for('main.dashboard'))
    
    task = Task(title=title, priority=priority, user_id=current_user.user_id)
    db.session.add(task)
    db.session.commit()
    
    flash('Task added successfully')
    return redirect(url_for('main.dashboard'))


@main_bp.route('/update_task/<int:task_id>', methods=['POST'])
@login_required
def update_task(task_id):
    task = Task.query.filter_by(task_id=task_id, user_id=current_user.user_id).first()
    
    if not task:
        flash('Task not found')
        return redirect(url_for('main.dashboard'))
    
    action = request.form.get('action')
    
    if action == 'toggle':
        task.is_completed = not task.is_completed
        db.session.commit()
        flash(f'Task marked as {"completed" if task.is_completed else "incomplete"}')
    
    return redirect(url_for('main.dashboard'))


@main_bp.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(task_id=task_id, user_id=current_user.user_id).first()
    
    if not task:
        flash('Task not found')
        return redirect(url_for('main.dashboard'))
    
    db.session.delete(task)
    db.session.commit()
    
    flash('Task deleted successfully')
    return redirect(url_for('main.dashboard'))
