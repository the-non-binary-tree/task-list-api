from flask import current_app
from app import db
# from .goal import Goal

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed_at = db.Column(db.DateTime, default=None)
    accessible = db.Column(db.Boolean, default=True, nullable=True)
    goal_id= db.Column(db.Integer, db.ForeignKey('goal.id'), nullable = True, default=None)
    goal = db.relationship('Goal', back_populates='tasks')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_complete': True if self.completed_at else False
        }
    
    def to_dict_with_goal(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_complete': True if self.completed_at else False,
            'goal_id': self.goal_id
        }