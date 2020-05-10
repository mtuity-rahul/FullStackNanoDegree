from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
## dialect://username:password@host:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db instance
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename_ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<Person ID:' + str(self.id) + ', name: ' + self.name + '>'


db.create_all()


@app.route('/')
def index():
    person = Person.query.first()
    # person_like = Person.query.filter(Person.name.like('%a%%'))
    # print(person_like)
    return 'Hello ' + person.name
