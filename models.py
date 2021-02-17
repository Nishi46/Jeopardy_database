from app import db

class Jeo(db.Model):
    __tablename__ = 'allc'

    number = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    question = db.Column(db.String())
    answer = db.Column(db.String())

    def __init__(self, category,question,asnwer,number):
    self.category = category
    self.question = question      
    self.answer = answer
    self.number = number

   

    def serialize(self):
        return {
            'category': self.category, 
            'question': self.question,
            'answer': self.answer,
            'number':self.number
        }