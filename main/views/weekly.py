from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.utils import redirect

from .. import db
from ..models import Monday,Tuesday,Wednesday,Thursday,Friday
from main.forms import DiaryForm


from main import db
from main.forms import AddWeekly
from main.models import User

bp = Blueprint('weekly', __name__, url_prefix='/weekly')

@bp.route('/')
def weekly():
    form = AddWeekly()  # CSRF 토큰이 포함된 폼 생성
    monday = Monday.query.all()
    tuesday = Tuesday.query.all()
    wednesday = Wednesday.query.all()
    thursday = Thursday.query.all()
    friday = Friday.query.all()

    return render_template(
        'weekly/todo.html',
        monday=monday, tuesday=tuesday, wednesday=wednesday,
        thursday=thursday, friday=friday, form=form  # 템플릿으로 폼 전달
    )

@bp.route('/update_status/<day>/<int:item_id>/<status>', methods=['POST'])
def update_status(day, item_id, status):
    # 선택된 요일과 항목에 따라 상태 업데이트
    task = None
    if day == 'monday':
        task = Monday.query.get(item_id)
    elif day == 'tuesday':
        task = Tuesday.query.get(item_id)
    elif day == 'wednesday':
        task = Wednesday.query.get(item_id)
    elif day == 'thursday':
        task = Thursday.query.get(item_id)
    elif day == 'friday':
        task = Friday.query.get(item_id)

    if task:
        task.todo = status  # 'O' 또는 'X' 저장
        db.session.commit()

    return '', 204  # 성공적인 요청, 응답 없음


@bp.route('/write', methods=['GET', 'POST'])
def write():
    form = AddWeekly()

    if form.validate_on_submit():
        # 선택한 요일에 따라 다른 모델에 저장
        selected_day = form.day.data  # 사용자가 선택한 요일 ('월', '화', ...)

        # 사용자가 입력한 content 내용
        content_data = form.content.data
        content_highlight= form.highlight.data

        # 선택된 요일에 따라 해당 테이블에 저장
        if selected_day == '월':
            entry = Monday(content=content_data,highlight=content_highlight)
        elif selected_day == '화':
            entry = Tuesday(content=content_data,highlight=content_highlight)
        elif selected_day == '수':
            entry = Wednesday(content=content_data,highlight=content_highlight)
        elif selected_day == '목':
            entry = Thursday(content=content_data,highlight=content_highlight)
        elif selected_day == '금':
            entry = Friday(content=content_data,highlight=content_highlight)

        # 데이터베이스에 저장
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('weekly.weekly'))  # 새로고침

    return render_template('weekly/add_todo.html', form=form)




