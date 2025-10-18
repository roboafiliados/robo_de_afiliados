from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def panel():
    return render_template('index.html', message="Painel do Robô Ativo!")
