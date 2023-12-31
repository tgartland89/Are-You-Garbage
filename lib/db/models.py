from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# one of my realted tables- this is realted to queston and results 
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)

# one of my realted tables- this is realted to players and results
# here is also where I can perfom full crud tied to my seed_questions_and_results in cli.py 
class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(String)

# one of my realted tables- this is realted to queston and players 
class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    result_text = Column(String)

class PlayerResult(Base):
    __tablename__ = 'player_results'

# class represents the association table between Player and Question in a many to many reltionshipe. 
# The table has three foreign key columns: player_id, question_id, and result_id. 
# These foreign keys establish the relationship between the Player, Question, and Result entities.

    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'), primary_key=True)
    result_id = Column(Integer, ForeignKey('results.id'))
    score = Column(Integer)

    player = relationship('Player')
    question = relationship('Question')
    result = relationship('Result')

class AddedQuestion(Base):
    __tablename__ = 'added_questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(String)

# Create the database engine
engine = create_engine('sqlite:///AYG.db')

# Create all tables defined in the models
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Close the session when you're done
session.close()