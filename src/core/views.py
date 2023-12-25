from flask import Blueprint, render_template

core_bp = Blueprint('core', __name__,
                    template_folder='templates',
                    static_folder='static',
                    )


@core_bp.route('/')
def home():
    title = 'Главная - МВ проект \'Scripts DataBase\' - Камила Титова'
    return render_template('core/index.html', title=title)
