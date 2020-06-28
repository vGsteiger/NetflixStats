import click

class NetflixStats:
    def __init__(self, print_out, run):
        self.print_out = print_out
        self.run = run

@click.command()
@click.option('--print_out', default=True)
@click.option('--run', default=True)
def cli(print_out, run):
    cc = NetflixStats(print_out, run)

if __name__ == '__main__':
    cli()