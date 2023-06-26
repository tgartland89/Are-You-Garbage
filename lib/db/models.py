from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='questions')

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    answer_text = Column(String(255))
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship('Question', backref='answers')

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    result_text = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='results')
