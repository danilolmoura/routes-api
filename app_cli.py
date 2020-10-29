import click

from graph import graph

@click.group()
def cli():
    pass

@cli.command()
@click.option('--file_path', '-f')
def check_route(file_path):
    """[summary]

    Args:
        file_path ([str]): [path to CSV file]
    """

    g = graph.create_graph(file_path)
    while(True):
        route = input('please enter the route: ')
        if not route:
            print('Exiting program')
            break

        initial_position, final_position = route.split('-')
        best_route_price = graph.get_best_route_price(g, initial_position, final_position)
        print('best route:', best_route_price)

if __name__ == '__main__':
    cli()