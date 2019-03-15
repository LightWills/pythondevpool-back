from app import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    login = db.Column(db.String(20))
    desc = db.Column(db.Text())

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def from_json(json):
        return User(name=json['name'], lastname=json['lastname'], login=json['login'], desc=json['desc'])
