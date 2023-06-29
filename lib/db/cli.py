import click
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, PlayerResult, Result, Question, AddedQuestion
import pyfiglet

def create_session():
    engine = create_engine('sqlite:///AYG.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def seed_questions_and_results(name):
    session = create_session()

    questions = [
        "Did you have an above-ground pool as a kid?",
        "Did you drink milk with dinner as a kid?",
        "Are you leaving more than $200 in the envelope at a close friend's or family member's wedding?",
        "Have you ever hidden from the cops for lighting off fireworks?",
        "Do you always tip 20% or more?",
        "Have you dined and dashed?",
        "Has anyone ever had a power of attorney over you?",
        "Have you or anyone in your family represented themselves in court?",
        "Do you keep your opened syrup in the pantry?",
        "Do you keep your opened ketchup in the fridge?"
    ]

    # Fetch the added questions from the database
    added_questions = session.query(AddedQuestion).all()
    existing_questions = session.query(Question).filter(Question.question_text.in_(questions)).all()
    existing_question_texts = set(question.question_text for question in existing_questions)

    for added_question in added_questions:
        if added_question.question_text not in existing_question_texts:
            questions.append(added_question.question_text)

    for question_text in questions:
        if question_text not in existing_question_texts:
            question = Question(question_text=question_text)
            session.add(question)

    session.commit()

    # Create a player with the given name
    player = Player(name=name)
    session.add(player)
    session.commit()

    for player in session.query(Player):
        yes_count = 0
        for player_question in session.query(Question):
            answer = input(f"{player_question.question_text} (Yes/No): ")
            if answer.lower() == "yes":
                yes_count += 1
            player_result = PlayerResult(player=player, question=player_question, score=yes_count)
            session.add(player_result)

        if yes_count >= 7:
            result_id = 7
        elif yes_count >= 4:
            result_id = 4
        else:
            result_id = 1

        # Retrieve the corresponding Result object based on the result_id
        result = session.query(Result).filter_by(id=result_id).first()

        # Assign the result object to player_result.result
        player_result.result = result

    session.commit()

    session.close()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
def start(name):
    session = create_session()
    player = Player(name=name)
    session.add(player)
    session.commit()

    title = pyfiglet.figlet_format("Are You Garbage?")
    click.echo(title)
    click.echo("Welcome to Are you Garbage?! Who do I have the pleasure of judging today?")
    click.echo()
    click.echo(f"Thank you, {name}! Don't forget to rate, review, and subscribe on YouTube, Spotify, and Apple to keep those numbers THROUGH THE ROOF!")
    click.echo("Now let's start the show!")
    click.echo()

    # Retrieve all questions from the database
    all_questions = session.query(Question).all()

    # Shuffle the questions randomly
    random.shuffle(all_questions)

    # Select the first 10 questions
    selected_questions = all_questions[:10]

    score = 0

    for index, question in enumerate(selected_questions):
        answer = click.prompt(question.question_text + " (Yes/No)").lower()
        if answer == "yes":
            score += 1

        player_result = PlayerResult(
            player=player,
            question=question,
            score=score
        )
        session.add(player_result)

    session.commit()

    if score >= 7:
        result_id = 7
    elif score >= 4:
        result_id = 4
    else:
        result_id = 1

    # Retrieve the corresponding Result object based on the result_id
    result = session.query(Result).filter_by(id=result_id).first()

    # Assign the result object to the player_result.result
    player_result.result = result

    session.commit()

    drum_roll = pyfiglet.figlet_format("Drum Roll Please")
    result_text = result.result_text
    result_text_ascii = pyfiglet.figlet_format(result_text)

    click.echo(drum_roll)
    click.echo(result_text_ascii)
    click.echo()

    add_question = click.confirm("Would you like to add a question?")

    if add_question:
        session.add_all([AddedQuestion(question_text=click.prompt("Enter your question:"))])
        session.commit()

        click.echo("Question added successfully!")

    session.close()



def main():
    cli()


if __name__ == '__main__':
    main()