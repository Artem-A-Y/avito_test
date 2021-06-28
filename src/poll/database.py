# -*- coding: utf-8 -*-
# описываем подключение и конфигурацию сессии

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings
from .tables import Polls, AnswerOptions


engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False},
)

Session = sessionmaker(  # ?!
    engine,
    autocommit=False,
    autoflush=False,
)

# Команды в Python Console:
# from poll.database import engine (1)
# from poll.tables import Base (2)
# Base.metadata.create_all(engine) (3) - Создал БД
# from poll.tables import Polls, AnswerOptions
# from poll.database import add_db, review_db


# Команды в Python Console: add_db() этот метод для теста. Которым я добавляю начальные данные в БД
def add_db():
    session = Session()
    session.add_all([
        Polls(survey_name='Какой город самый красивый'),
    ])

    def add():
        session = Session()
        p = session.query(Polls).get(1)
        session.add_all([
            AnswerOptions(variant='Москва', polls=p),
            AnswerOptions(variant='Казань', polls=p),
            AnswerOptions(variant='Самара', polls=p),
        ])
        session.commit()

    session.commit()
    add()


def review_db():
    session = Session()
    print(session.query(Polls).all(), session.query(Polls.id).all())
    print(session.query(AnswerOptions).all(), session.query(AnswerOptions.poll_id).all())
