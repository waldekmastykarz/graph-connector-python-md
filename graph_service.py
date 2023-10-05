import configparser
from azure.identity import ClientSecretCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphServiceClient, GraphRequestAdapter
from msgraph_core import GraphClientFactory

_config = configparser.ConfigParser()
_config.read("config.ini")

_tenant_id = _config["AZURE"]["TENANT_ID"]
_client_id = _config["AZURE"]["CLIENT_ID"]
_client_secret = _config["AZURE"]["CLIENT_SECRET"]

_credential = ClientSecretCredential(_tenant_id, _client_id, _client_secret)
_auth_provider = AzureIdentityAuthenticationProvider(_credential)
_middleware = GraphClientFactory.get_default_middleware(None)
http_client = GraphClientFactory.create_with_custom_middleware(_middleware)
_adapter = GraphRequestAdapter(_auth_provider, http_client)

graph_client = GraphServiceClient(_credential,
                                  scopes=[
                                      "https://graph.microsoft.com/.default"],
                                  request_adapter=_adapter)
