import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# TODO  данные будут сырые не привязаны ни к чему, поскольку у нас не будет пользователя.

# TODO все таблицы будут наследоваться от базового класса. Создадим его:
Base = declarative_base()


class Polls(Base):
    __tablename__ = 'polls'

    id = sa.Column(sa.Integer, primary_key=True)
    survey_name = sa.Column(sa.Text, nullable=False, unique=True)

    answer_options = relationship('AnswerOptions', backref='polls', lazy='dynamic')

    def __repr__(self):
        return '< Polls {} >'.format(self.survey_name)


class AnswerOptions(Base):
    __tablename__ = 'answer_options'

    id = sa.Column(sa.Integer, primary_key=True)
    variant = sa.Column(sa.String, nullable=False, unique=True)

    poll_id = sa.Column(sa.Integer, sa.ForeignKey('polls.id'))

    def __repr__(self):
        return '< AnswerOptions {} >'.format(self.variant)

