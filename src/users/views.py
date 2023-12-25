from flask import Blueprint, render_template

users_bp = Blueprint('users_bp', __name__,
                     template_folder='templates',
                     static_folder='static',
                     url_prefix='/users')


@users_bp.route('/')
def users():
    title = 'Список пользователей - МВ проект \'Scripts DataBase\' - Камила Титова'
    return render_template('users/users_list.html', title=title)
