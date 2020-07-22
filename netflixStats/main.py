import click
from netflixstats.netflix_stats import NetflixStats


@click.command()
@click.option('--print_out', default=True)
@click.option('--run', default=True)
@click.option('--file', default=None)
def cli(print_out, run, file):
    cc = NetflixStats(print_out, run, file)


if __name__ == '__main__':
    cli()
