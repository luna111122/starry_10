from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from datetime import datetime
class DiaryForm(FlaskForm):
    title= StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    emotion= RadioField('감정', choices=[('좋음', '좋음'),('보통','보통'),('나쁨','나쁨')], validators=[DataRequired()])
    distract = RadioField('방해', choices=[('스마트폰', '스마트폰'), ('일정', '일정'), ('피로', '피로'),('기타', '기타')], validators=[DataRequired()])
    todo = RadioField('일정', choices=[('O', 'O'), ('X', 'X')], validators=[DataRequired()])





class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class AddWeekly(FlaskForm):
    day = RadioField('요일', choices=[('월', '월'), ('화', '화'), ('수', '수'), ('목', '목'),('금', '금')],
                          validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    highlight = RadioField('하이라이트', choices=[('일반', '일반'), ('하이라이트', '하이라이트')], validators=[DataRequired()])

class goal(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])
    day = TextAreaField('내용', validators=[DataRequired()])