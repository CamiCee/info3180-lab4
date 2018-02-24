from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UpLoadForm(FlaskForm):
    file=FileField('Images', validators=[FileRequired(), FileAllowed(['jpg','png'],'Images Only!')])
    

