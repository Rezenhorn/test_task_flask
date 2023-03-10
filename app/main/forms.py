from flask_wtf import FlaskForm  # flask-wtf это обертка пакета wtforms
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import Optional, URL


class LinkForm(FlaskForm):
    link = URLField(
        'Ccылка',
        validators=[Optional(), URL(message='Неверный URL')]
    )
    submit = SubmitField('Отправить')


class CSVForm(FlaskForm):
    csv_file = FileField(
        'CSV файл с ссылками',
        validators=[
            Optional(), FileAllowed(['csv'], 'Разрешены только .csv файлы')
        ]
    )
    submit = SubmitField('Отправить')


class SearchForm(FlaskForm):
    domain = StringField('Домен')
    domain_zone = StringField('Доменная зона')
    submit = SubmitField('Найти')
