from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(String)

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    result_text = Column(String)

class PlayerResult(Base):
    __tablename__ = 'player_results'

    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'), primary_key=True)
    result_id = Column(Integer, ForeignKey('results.id'))
    score = Column(Integer)

    player = relationship('Player')
    question = relationship('Question')
    result = relationship('Result')
