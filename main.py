import argparse
import asyncio
from connection_service import create_connection

_parser = argparse.ArgumentParser(description="Ingest local markdown files to Microsoft 365")
_subparsers = _parser.add_subparsers(title="Command to run", dest="subcommand", required=True)
_subparsers.add_parser("create-connection", help="Creates external connection")
_subparsers.add_parser("load-content", help="Loads content into the external connection")
_args = _parser.parse_args()

if _args.subcommand == "create-connection":
    asyncio.run(create_connection())
elif _args.subcommand == "load-content":
    print("Loading content...")
