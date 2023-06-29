from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, PlayerResult, Result, Question, AddedQuestion, Base

def seed_questions_and_results():
    # Create the database engine
    engine = create_engine('sqlite:///AYG.db')

    # Create all tables defined in the models
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the existing questions from the database
    existing_questions = session.query(Question).all()
    existing_question_texts = set(question.question_text for question in existing_questions)

    # Fetch the added questions from the database
    added_questions = session.query(AddedQuestion).all()

    for added_question in added_questions:
        if added_question.question_text not in existing_question_texts:
            question = Question(question_text=added_question.question_text)
            session.add(question)

    session.commit()

    # Close the session when you're done
    session.close()
    
if __name__ == '__main__':
    seed_questions_and_results()
