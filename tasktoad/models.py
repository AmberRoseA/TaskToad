from tasktoad import db


class Today(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return self



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return self



class Tasks(db.Model):
    # Task Model's Schema
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(35), unique=True, nullable=False)
    #  Consider some options no have nullable=false - Task description - Task Due 
    task_description = db.Column(db.Text, nullable=False)
    task_importance = db.Column(db.Boolean, default=False, nullable=False)
    task_due = db.Column(db.DateTime, nullable=False)
    #  difficulty_level = db.Column() revisit 


    def __repr__(self):
        return self



"""class Important(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):



class Planned(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return self
"""







