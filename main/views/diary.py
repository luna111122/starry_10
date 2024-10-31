from flask import Blueprint,url_for, request, render_template
from werkzeug.utils import redirect

from datetime import datetime, timezone
from .. import db
from ..models import Diary
from main.forms import DiaryForm


from openai import OpenAI
import os


from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),  # this is also the default, it can be omitted
)
client=OpenAI()
completion = client.completions.create(model='curie')
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
bp = Blueprint('diary',__name__,url_prefix='/diary')


def generate_chatgpt_response(script):
    try:
        response=client.chat.completions.create(
            messages = [
                {"role": "system", "content": "You are an empathetic mentor and a scientific advisor. "
                                              "When responding to the user's diary entry, provide emotional support and understanding. "
                                              "Additionally, include scientifically-backed advice or facts to help the user improve their well-being. "
                                              "Your tone should be kind, thoughtful, and balanced between empathy and practical guidance.\n\n"
                                              f"User's diary entry: {script}\n\nResponse:"},
                {"role": "user", "content": script}
            ],
            model = "gpt-3.5-turbo"
        )


        return response.choices[0].text.strip()
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"



bp = Blueprint('diary',__name__,url_prefix='/diary')

@bp.route('/advice', methods=['GET', 'POST'])
def advice():
    if request.method == 'POST':
        # 폼에서 script 데이터를 가져옵니다.
        script = request.form.get('script')
        feedback = generate_chatgpt_response(script)
        return render_template('diary/advice.html', script=script, feedback=feedback)
    else:
        # GET 요청 시 일기 내용을 입력하는 폼을 렌더링합니다.
        script = request.form.get('script')
        feedback = generate_chatgpt_response(script)
        return render_template('diary/advice.html', script=script, feedback=feedback)



@bp.route('/write', methods=('POST','GET'))
def write():
    form= DiaryForm()
    if request.method=='POST' and form.validate_on_submit():
        diary = Diary(title=form.title.data,
                      content=form.content.data,
                      emotion=form.emotion.data,
                      distract=form.distract.data,
                      todo=form.todo.data




                      )
        db.session.add(diary)
        db.session.commit()
        return render_template('diary/result.html',form=form)
    return render_template('diary/write.html',form=form)




@bp.route('/all')
def all():
    diaries = Diary.query.order_by(Diary.id.desc())
    return render_template('diary/all.html', diaries=diaries)


@bp.route('/emotion/happy')
def happy():
    happy = Diary.query.filter_by(emotion='좋음').order_by(Diary.id.desc())


    return render_template('diary/emotion/happy.html', happy=happy)

@bp.route('/emotion/normal')
def normal():

    normal = Diary.query.filter_by(emotion='보통').order_by(Diary.id.desc())


    return render_template('diary/emotion/normal.html',  normal=normal)

@bp.route('/emotion/bad')
def bad():
    bad = Diary.query.filter_by(emotion='나쁨').order_by(Diary.id.desc())


    return render_template('diary/emotion/bad.html', bad=bad)

@bp.route('/distract/smartphone')
def smartphone():

    smartphone = Diary.query.filter_by(distract='스마트폰').order_by(Diary.id.desc())

    return render_template('diary/distract/smartphone.html', smartphone=smartphone )
@bp.route('/distract/schedule')
def schedule():

    schedule = Diary.query.filter_by(distract='일정').order_by(Diary.id.desc())

    return render_template('diary/distract/schedule.html',schedule=schedule  )
@bp.route('/distract/fatigue')
def fatigue():

    fatigue = Diary.query.filter_by(distract='피로').order_by(Diary.id.desc())

    return render_template('diary/distract/fatigue.html', fatigue=fatigue )
@bp.route('/distract/etc')
def etc():

    etc = Diary.query.filter_by(distract='기타').order_by(Diary.id.desc())

    return render_template('diary/distract/etc.html', etc=etc )


