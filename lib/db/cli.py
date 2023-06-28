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

    for index, question in enumerate(questions[:10]):
        answer = input(question.question_text + " (Yes/No)").lower()
        if answer == "yes":
            score += 1

        # Assign the question_id based on the loop index
        question_id = index + 1

        session.add(
            PlayerResult(
                player=player,
                question_id=question_id,
                score=score,
                result_id=None  # Assign None initially
            )
        )

    session.commit()

    if score >= 7:
        result_id = 7
    elif score >= 4:
        result_id = 4
    else:
        result_id = 1

    result_text = session.query(Result).filter_by(id=result_id).first().result_text

    # Update the result_id for the PlayerResult objects
    player_results = session.query(PlayerResult).filter_by(player=player).all()
    for player_result in player_results:
        player_result.result_id = result_id

    session.commit()

    click.echo("drum roll please...")
    click.echo(result_text)
    
def main():
    cli()


if __name__ == '__main__':
    main()