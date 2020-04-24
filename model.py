from db import db


class Download_Record(db.Model):
    __tablename = 'A_Download_Record'
    Id = db.Column(db.Integer,primary_key=True)
    User_Email = db.Column(db.String(64))
    Veri_Code = db.Column(db.String(24))

