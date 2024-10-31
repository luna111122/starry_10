from flask import Blueprint,url_for, request, render_template
from werkzeug.utils import redirect

from datetime import datetime, timezone
from .. import db
from ..models import Diary,Monday,Tuesday,Wednesday,Thursday,Friday, Highlight,goals
from main.forms import goal


from main.forms import DiaryForm



bp = Blueprint('main',__name__,url_prefix='/main')

@bp.route('/', methods=['GET','POST'])
def mypage():

    goalls=goals.query.all()
    # 요일별로 모든 하이라이트 데이터를 가져옴
    highlights = {
        'monday': Monday.query.filter(Monday.highlight == '하이라이트').all(),
        'tuesday': Tuesday.query.filter(Tuesday.highlight == '하이라이트').all(),
        'wednesday': Wednesday.query.filter(Wednesday.highlight == '하이라이트').all(),
        'thursday': Thursday.query.filter(Thursday.highlight == '하이라이트').all(),
        'friday': Friday.query.filter(Friday.highlight == '하이라이트').all(),
    }
    # 템플릿에 하이라이트 데이터 전달
    return render_template('mypage.html', highlights=highlights,goalls=goalls)

@bp.route('/goal', methods=['POST','GET'])
def goalling():
    goal_form=goal()
    if request.method=='POST' and goal_form.validate_on_submit():
            goal_db = goals(content=goal_form.content.data,
                          day=goal_form.day.data

                          )
            db.session.add(goal_db)
            db.session.commit()


            return redirect(url_for('main.mypage'))  # URL로 리디렉션


    return render_template('goal.html', form=goal_form)

@bp.route('/intro')
def intro():
    return render_template('intro.html')

@bp.route('/result')
def result():
    ehappy=Diary.query.filter(Diary.emotion=='좋음').all()
    happy = len(ehappy)
    enormal = Diary.query.filter(Diary.emotion == '보통').all()
    normal = len(enormal)
    ebad = Diary.query.filter(Diary.emotion == '나쁨').all()
    bad = len(ebad)

    max_emotion = max(
        {'감정': '좋음', 'count': happy},
        {'감정': '보통', 'count': normal},
        {'감정': '나쁨', 'count': bad},
        key=lambda x: x['count']
    )

    dsmartphone = Diary.query.filter(Diary.distract == '스마트폰').all()
    smartphone = len(dsmartphone)
    dschedule = Diary.query.filter(Diary.distract == '일정').all()
    schedule = len(dschedule)
    dfatigue = Diary.query.filter(Diary.distract == '피로').all()
    fatigue = len(dfatigue)
    detc = Diary.query.filter(Diary.distract == '기타').all()
    etc = len(detc)

    max_distraction = max(
        {'방해': '스마트폰', 'count': smartphone},
        {'방해': '일정', 'count': schedule},
        {'방해': '피로', 'count': fatigue},
        {'방해': '기타', 'count': etc},
        key=lambda x: x['count']
    )

    monday = Monday.query.all()
    tuesday = Tuesday.query.all()
    wednesday = Wednesday.query.all()
    thursday = Thursday.query.all()
    friday = Friday.query.all()

    # 각 요일별 O와 X의 개수 계산
    counts = {
        'monday': {'O': sum(1 for task in monday if task.status == 'O'),
                   'X': sum(1 for task in monday if task.status == 'X')},
        'tuesday': {'O': sum(1 for task in tuesday if task.status == 'O'),
                    'X': sum(1 for task in tuesday if task.status == 'X')},
        'wednesday': {'O': sum(1 for task in wednesday if task.status == 'O'),
                      'X': sum(1 for task in wednesday if task.status == 'X')},
        'thursday': {'O': sum(1 for task in thursday if task.status == 'O'),
                     'X': sum(1 for task in thursday if task.status == 'X')},
        'friday': {'O': sum(1 for task in friday if task.status == 'O'),
                   'X': sum(1 for task in friday if task.status == 'X')}
    }




    return render_template('result.html',max_emotion=max_emotion,max_distraction=max_distraction,
                           smartphone=smartphone,schedule=schedule,fatigue=fatigue,etc=etc,monday=monday, tuesday=tuesday,
                           wednesday=wednesday, thursday=thursday,
                           friday=friday, counts=counts)

