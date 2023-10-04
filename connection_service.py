from graph_service import GraphService

class ConnectionService:
    async def create_connection():
        print("Creating connection...")
        await GraphService.client.external().connections().post(ConnectionConfiguration.external_connection())
        print("DONE")
