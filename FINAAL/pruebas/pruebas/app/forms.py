class RecetaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    ingredientes = TextAreaField('Ingredientes', validators=[DataRequired()])
    instrucciones = TextAreaField('Instrucciones', validators=[DataRequired()])
    submit = SubmitField('Guardar Receta')
