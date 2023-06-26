from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    text = Column(String)


class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    score_range = Column(String)
    description = Column(String)


class PlayerResult(Base):
    __tablename__ = 'player_results'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    result_id = Column(Integer, ForeignKey('results.id'))

    player = relationship(Player)
    result = relationship(Result)
