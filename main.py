import asyncio
from connection_service import create_connection
from args import args

if args.subcommand == "create-connection":
    asyncio.run(create_connection())
elif args.subcommand == "load-content":
    print("Loading content...")
