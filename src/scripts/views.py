from flask import Blueprint, render_template, request, redirect, url_for

from src.scripts.models import Script

scripts_bp = Blueprint('scripts', __name__,
                       template_folder='templates',
                       static_folder='static',
                       url_prefix='/scripts')


@scripts_bp.route('/')
def scripts_list():
    title = 'Список SQL скриптов - МВ проект \'Scripts DataBase\' - Камила Титова'
    return render_template('scripts/scripts_list.html', title=title)


# @scripts_bp.route("/create", methods=["GET", "POST"])
# def script_record_create():
#     if request.method == "POST":
#         script = Script(
#             name=request.form["name"],
#             description=request.form["email"],
#             code=request.form["code"],
#             author=request.form["author"],
#             author_id=request.form["author"],
#         )
#         # db.session.add(script)
#         # db.session.commit()
#         return redirect(url_for("script_detail", id=script.id))
#
#     return render_template("scripts/create.html")
