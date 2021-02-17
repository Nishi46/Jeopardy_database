from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/Jeopardy'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://qskrwmanwdpwkt:73686aaef11ee6ab8d28884d7e2c529b86751b8935daab2b7d90dfca89cba64c@ec2-54-159-138-67.compute-1.amazonaws.com:5432/d594189knldorf'
sslmode=require
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__='allc'
    
    category = db.Column(db.String())
    question = db.Column(db.String())
    answer= db.Column(db.String(),primary_key=True)
    def __init__(self,question,answer,category):
         
         self.category = category
         self.question = question
         self.answer = answer
        
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():  
    if request.method == 'POST':
        question = request.form['Question']
        answer = request.form ['Answer']
        category = request.form['Category']
        allc=Data(question,answer,category)
        db.session.add(allc)
        db.session.commit()
   
    return render_template("success.html")



if __name__ == '__main__':
    app.debug=True
    app.run()
