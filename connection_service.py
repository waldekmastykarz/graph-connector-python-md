from connection_configuration import external_connection
from graph_service import graph_client

async def _create_connection():
  print('Creating connection...');
  await graph_client.external.connections.post(external_connection)
  print('Connection created');

async def create_connection():
  await _create_connection()