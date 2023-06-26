from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the database engine from the sqlalchemy url on line 58 of alembic.ini
engine = create_engine('sqlite:///AYG.db')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Define the Result model
class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def __repr__(self):
        return f"Result(name={self.name}, score={self.score})"

# Create the 'results' table if it doesn't exist
Base.metadata.create_all()

# Rest of the code remains the same...
questions = [
    "Did you have an above-ground pool as a kid?",
    "Did you drink milk with dinner as a kid?",
    "Are you leaving more than $200 in the envelope at a close friend's or family member's wedding?",
    "Have you ever hidden from the cops for lighting off fireworks?",
    "Do you always tip 20/'%' or more?",
    "Have you dined and dashed?",
    "Has anyone ever had a power of attorney over you?",
    "Have you or anyone in your family represented themselves in court?",
    "Do you keep your opened syrup in the pantry?",
    "Do you keep your opened ketchup in the fridge?"
]

# Initialize the score
score = 0

# Welcome message
print("Welcome to Aunt Tuddie's basement!! Who do I have the privilege of judging today?")
name = input(">> Enter name: ")
print(f"\nHello {name}! Don't forget to rate, review, and subscribe to AYG on Youtube, Patreon, & Instagram to keep those numbers (voice cue from Toby- 'THROUGH THE ROOF')\n")

# starting the game/ Ask the questions
print("COOKING… Now let's start the show. You will need to answer the following yes or no questions which will determine if you're class or a big ol' piece of trash!\n")

for question in questions:
    answer = input(f"{question} >> ")
    if answer.lower() == "yes":
        score += 1

# Store the result in the database using SQLAlchemy
result = Result(name=name, score=score)
session.add(result)
session.commit()

# Determine the result based on the score
if score >= 7:
    result_text = "Garbage - MAMA MIA! You are 100/'%' GARBAGIO!"
elif score >= 4:
    result_text = "Trashy - Congrats, you're only a bit Trashy"
else:
    result_text = "Classy - You made it baby! You're clean livin' & classy!"

# Display the result
print("\nResults:")
print(result_text)
