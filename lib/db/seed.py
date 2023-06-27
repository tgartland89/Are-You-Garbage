from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Question, Result, Player, PlayerResult

engine = create_engine('sqlite:///AYG.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_questions_and_results():
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

    results = {
        7: "Garbage - MAMA MIA!! You are 100'%' GARBAGIO!",
        4: "Trashy - Congrats, you're only a bit Trashy",
        1: "Classy - You made it baby!!! You're clean livin' & classy!"
    }

    for question_text in questions:
        question = Question(question_text=question_text)
        session.add(question)

    session.commit()

    for player in session.query(Player):
        yes_count = 0
        for player_question in session.query(Question):
            answer = click.prompt(player_question.question_text + " (Yes/No): ")
            if answer.lower() == "yes":
                yes_count += 1
            player_result = PlayerResult(player=player, question=player_question, score=yes_count)
            session.add(player_result)

        if yes_count >= 7:
            result_text = results[7]
        elif yes_count >= 4:
            result_text = results[4]
        else:
            result_text = results[1]

        result = Result(result_text=result_text)
        player_result = PlayerResult(player=player, result=result, score=yes_count)
        session.add(result)
        session.add(player_result)

    session.commit()

seed_questions_and_results()
