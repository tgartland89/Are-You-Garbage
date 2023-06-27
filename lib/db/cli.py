import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, PlayerResult, Result, Question


def create_session():
    engine = create_engine('sqlite:///AYG.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


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

    click.echo(f"Welcome, {name}! Let's play 'Are you Garbage?'")

    questions = session.query(Question).all()
    score = 0

    for question in questions:
        answer = click.prompt(question.question_text + " (Yes/No)").lower()
        if answer == "yes":
            score += 1

    # Get the current question from the database
    current_question = session.query(Question).filter_by(active=True).first()

    # Create a new PlayerResult instance with the provided question_id
    player_result = PlayerResult(player=player, result=None, question=current_question, score=score)

    # Add the player_result to the session and commit the changes
    session.add(player_result)
    session.commit()

    result = session.query(Result).filter(Result.id == 7).first()
    if not result:
        if score >= 7:
            result = session.query(Result).filter(Result.id == 7).first()
    elif score >= 4:
        result = session.query(Result).filter(Result.id == 4).first()
    else:
        result = session.query(Result).filter(Result.id == 1).first()

    if result:
        result_text = result.result_text
    player_result = PlayerResult(player=player, result=result, score=score)
    session.add(player_result)
    session.commit()

    click.echo(f"drum roll please...: {result_text}")


def main():
    cli()


if __name__ == '__main__':
    main()
