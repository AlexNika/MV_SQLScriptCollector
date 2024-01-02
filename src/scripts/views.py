from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from src import db
from src.scripts.models import Script

from src.scripts.forms import AddScriptForm
from src.users.models import User

scripts_bp = Blueprint("scripts", __name__,
                       template_folder="templates",
                       static_folder="static",
                       url_prefix="/scripts")


@scripts_bp.route("/")
@login_required
def scripts_list():
    title = "Список SQL скриптов - МВ проект 'Scripts DataBase' - Камила Титова"
    if current_user.is_authenticated:
        if current_user.allow_see_others:
            scripts = Script.query.all()
        else:
            scripts = Script.query.filter_by(user_id=current_user.id).all()
        return render_template('scripts/scripts_list.html', title=title, scripts=scripts)
    flash("You are not authenticated. Please login.", "danger")
    return render_template("core/index.html")


@scripts_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_script():
    form = AddScriptForm(request.form)
    form.user_id.choices = []
    users = User.query.all()
    form.user_id.choices = [user.email for user in users]
    if form.validate_on_submit():
        script = Script(name=form.name.data, description=form.description.data, code=str(form.code.data),
                        user_id=form.user_id.data)
        db.session.add(script)
        db.session.commit()
        flash(f"SQL script {form.name.data} was successfully added to DB", "success")
        return redirect(url_for("scripts.scripts_list"))
    return render_template("scripts/add_script.html", users=users, form=form)

