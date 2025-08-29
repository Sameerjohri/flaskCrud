from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
				
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"		


db = SQLAlchemy(app)							
app.app_context().push()




class Employee(db.Model):						
    sno = db.Column(db.Integer, primary_key = True)			
    name = db.Column(db.String(200), nullable = False)			
    address = db.Column(db.String(500), nullable = False)		
    joined_date = db.Column(db.DateTime, default=datetime.utcnow)	

    def __repr__(self):
        return f"{self.sno} - {self.name}"
    



@app.route("/")
def hello_world():
    employee = Employee(name = "Employee Name", address = "Employee Address")   
    db.session.add(employee)
    db.session.commit()
    allemployee = Employee.query.all()				
    return render_template("index.html", allemployee=allemployee)

@app.route("/about")
def about():
    return "<p>This is about page!</p>"

@app.route("/display")
def display():
    allemployee = Employee.query.all()
    print(allemployee)
    return "This is page 2"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)			