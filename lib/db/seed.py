from sqlalchemy.orm import sessionmaker
from models import Player, Question, Result, engine, Base

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add questions
questions = [
    "Did you have an above-ground pool as a kid?",
    "Did you drink milk with dinner as a kid?",
    "Are you leaving more than $200 in the envelope at a close friend's or family member's wedding?",
    "Have you ever hidden from the cops for lighting off fireworks?",
    "Do you always tip 20'%' or more?",
    "Have you dined and dashed?",
    "Has anyone ever had a power of attorney over you?",
    "Have you or anyone in your family represented themselves in court?",
    "Do you keep your opened syrup in the pantry?",
    "Do you keep your opened ketchup in the fridge?"
]

for text in questions:
    question = Question(text=text)
    session.add(question)

session.commit()

# Add results
results = [
    (7, 10, "Garbage - MAMA MIA!! You are 100'%' GARBAGIO!"),
    (4, 6, "Trashy - Congrats, you're only a bit Trashy"),
    (1, 3, "Classy - You made it baby!!! You're clean livin' & classy!")
]
for score_range, description in results:
    result = Result(score_range=score_range, description=description)
    session.add(result)

session.commit()

# Close the session
session.close()
