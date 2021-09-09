from os import environ
from argparse import ArgumentParser

DEFAULT_CONFIG = 'apps/tndc_api/etc/config.yaml'
environ['PYTHONPATH'] = "."
environ['PYTHONDONTWRITEBYTECODE'] = "true"


def get_args():
    parser = ArgumentParser("Development Server")
    parser.add_argument(
        '-c', '--config', action='store', default=DEFAULT_CONFIG, type=str,
        help="Specify the config file to use")
    parser.add_argument(
        '--port', action='store', type=int, default=5000,
        help='Specify the port to use.')
    return parser.parse_args()


def main(args):
    pass


if __name__ == "__main__":
    main(get_args())
