import click
from .yaml_loader import load_course
from .export import export_course


@click.command()
@click.argument('input_path')
@click.argument('output_path')
def cli(input_path, output_path):
    """
        Convert a YAML course into a JSON course.
    """
    course = load_course(input_path)
    export_course(output_path, course)


if __name__ == '__main__':
    cli()
