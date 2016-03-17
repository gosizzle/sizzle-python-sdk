import click

import sizzle

@click.command('sizzle')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(sizzle.has_legs)
