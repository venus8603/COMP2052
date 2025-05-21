class Receta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    ingredientes = db.Column(db.Text, nullable=False)
    instrucciones = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
