from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Student(db.Model):
    pk = db.Column(db.Integer(), primary_key=True)
    last_name = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30))

    group_pk = db.Column(db.Integer(), db.ForeignKey("group.pk", name="Group"))
    group = db.relationship("Group", back_populates="students")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
class Group(db.Model):
    pk = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    students = db.relationship("Student", back_populates="group")

    def __str__(self):
        return f"{self.name}"