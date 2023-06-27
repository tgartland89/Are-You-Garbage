from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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
    result_id = Column(Integer, ForeignKey('results.id'))
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    score = Column(Integer)

    player = relationship('Player')
    result = relationship('Result')
    question = relationship('Question')

# Create the database engine
engine = create_engine('sqlite:///AYG.db')

# Create all tables defined in the models
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Now you can use the session and interact with the database
# For example, creating a new player
player = Player(name='Tom')
session.add(player)
session.flush()  # This flushes the session to generate an ID for the new player

question_id = 1  # Replace with the actual question ID
player_result = PlayerResult(player_id=player.id, question_id=question_id, score=5)
session.add(player_result)
session.commit()


# Close the session when you're done
session.close()