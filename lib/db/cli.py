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

    if score >= 7:
        result_text = session.query(Result).filter_by(id=7).first().result_text
    elif score >= 4:
        result_text = session.query(Result).filter_by(id=4).first().result_text
    else:
        result_text = session.query(Result).filter_by(id=1).first().result_text

    player_result = PlayerResult(player=player, result=Result(result_text=result_text), score=score)
    session.add(player_result)
    session.commit()

    click.echo(f"drum roll please...: {result_text}")

def main():
    cli()

if __name__ == '__main__':
    main()
