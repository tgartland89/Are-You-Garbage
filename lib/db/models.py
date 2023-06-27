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

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    player_name = Column(String)
    player_result = Column(String)

    player = relationship('Player')

    def __init__(self, player_id, player_name, player_result):
        self.player_id = player_id
        self.player_name = player_name
        self.player_result = player_result