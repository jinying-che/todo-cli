#!/usr/bin/env python3
import click

@click.group()
def cli():
    pass

@click.command()
def add():
    click.echo('Added a new task')

@click.command()
@click.option('--tag', default="", help='task tag')
@click.option('--status', default="todo", help='task status')
def ls():
    click.echo('Listed all tasks')

def done(task):
    click.echo(f"{task} done!")

cli.add_command(add)
cli.add_command(ls)

if __name__ == '__main__':
    cli()
