import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, PlayerResult, Result, Question, AddedQuestion


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

    for index, question in enumerate(questions):
        answer = click.prompt(question.question_text + " (Yes/No)").lower()
        if answer == "yes":
            score += 1

        # Assign the question_id based on the loop index
        question_id = index + 1

        player_result = PlayerResult(
            player=player,
            question_id=question_id,  # Assign the question_id
            result=Result(result_text=""),  # Placeholder, will be updated later
            score=score
        )
        session.add(player_result)

    session.commit()

    if score >= 7:
        result_text = session.query(Result).filter_by(id=7).first().result_text
    elif score >= 4:
        result_text = session.query(Result).filter_by(id=4).first().result_text
    else:
        result_text = session.query(Result).filter_by(id=1).first().result_text

    # Update the result_text for the PlayerResult record
    player_result.result.result_text = result_text
    session.commit()

    click.echo(f"drum roll please...: {result_text}")

    add_question = click.confirm("Would you like to add a question?")

    if add_question:
        new_question_text = click.prompt("Enter your question:")
        added_question = AddedQuestion(question_text=new_question_text)
        session.add(added_question)
        session.commit()

        click.echo("Question added successfully!")

    session.close()


def main():
    cli()


if __name__ == '__main__':
    main()