import httpx
import time
from kiota_http.middleware import BaseMiddleware
from kiota_abstractions.serialization.parse_node_factory_registry import ParseNodeFactoryRegistry
from msgraph.generated.models.external_connectors.connection_operation import ConnectionOperation
from msgraph.generated.models.external_connectors.connection_operation_status import ConnectionOperationStatus

class CompleteJobWithDelayHandler(BaseMiddleware):
    def __init__(self, delayMs: int) -> None:
        super().__init__()
        self.delayMs = delayMs

    async def send(
        self, request: httpx.Request, transport: httpx.AsyncBaseTransport
    ) -> httpx.Response:
        response: httpx.Response = await super().send(request, transport)

        location = response.headers.get("Location")
        if location:
            print(f"Location: {location}")

            if "/operations/" not in location:
                # not a job URL we should follow
                return
          
            print(f"Waiting {self.delayMs}ms before following location {location}...")
            time.sleep(self.delayMs / 1000)
            await self.send(request, transport)
            return

        if "/operations/" not in request.url:
            # not a job
            return
        
        if not response.is_success:
            print("Response is not OK")
            return

        body_bytes = response.read()
        parse_node = ParseNodeFactoryRegistry.get_root_parse_node("application/json", body_bytes)
        operation: ConnectionOperationStatus = parse_node.get_object_value(ConnectionOperation.create_from_discriminator_value)

        if operation.status == ConnectionOperationStatus.Inprogress:
            print(f"Waiting ${self.delayMs}ms before trying again...")
            time.sleep(self.delayMs / 1000)
            await self.send(request, transport)
