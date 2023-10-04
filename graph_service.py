from configparser import SectionProxy
from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient, GraphRequestAdapter
from msgraph_core import GraphClientFactory
from httpx import AsyncClient

class GraphService:
    _client: GraphServiceClient
    _http_client: AsyncClient
    
    @staticmethod
    @property
    def client() -> GraphServiceClient:
        if (GraphService._client == None):
            config = SectionProxy
            with open('config.ini', 'r') as f:
                config.read_file(f)
            
            tenant_id = config['AZURE']['TENANT_ID']
            client_id = config['AZURE']['CLIENT_ID']
            client_secret = config['AZURE']['CLIENT_SECRET']

            credential = ClientSecretCredential(tenant_id, client_id, client_secret)
            middleware = GraphClientFactory.get_default_middleware()
            http_client = GraphClientFactory.create_with_custom_middleware(middleware)

            adapter = GraphRequestAdapter(credential, http_client)
            
            GraphService._client = GraphServiceClient(credential,
                                                     scopes=['https://graph.microsoft.com/.default'],
                                                     request_adapter=adapter)

        return GraphService._client
    
    @staticmethod
    @property
    def http_client() -> AsyncClient:
        return GraphService._http_client