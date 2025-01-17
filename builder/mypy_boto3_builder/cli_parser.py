import argparse
from pathlib import Path

from mypy_boto3_builder.service_name import ServiceName


def get_absolute_path(path: str) -> Path:
    return Path(path).absolute()


def get_service_name(name: str) -> ServiceName:
    try:
        return ServiceName(name)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Unknown service {name}")


def get_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        "mypy_boto3_builder", description="Builder for mypy-boto3."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Show debug messages"
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="Show package version"
    )
    parser.add_argument(
        "-f", "--format", action="store_true", help="Format output with black"
    )
    parser.add_argument(
        "--skip-master", action="store_true", help="Whether to skip master module"
    )
    parser.add_argument(
        "--skip-services", action="store_true", help="Whether to skip service modules"
    )
    parser.add_argument(
        "output_path", metavar="OUTPUT_PATH", help="Output path", type=get_absolute_path
    )
    parser.add_argument(
        "-s",
        "--services",
        dest="service_names",
        nargs="*",
        metavar="SERVICE_NAME",
        help="List of AWS services, by default ",
        type=get_service_name,
        default=ServiceName.items(),
    )
    return parser
