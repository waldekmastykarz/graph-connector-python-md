from kiota_http.middleware import BaseMiddleware
import httpx

class DebugHandler(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def send(
        self, request: httpx.Request, transport: httpx.AsyncBaseTransport
    ) -> httpx.Response:
        print()
        print(f"Request: {request.method} {request.url}")
        for key, value in request.headers.items():
            print(f"{key}: {value}")
        if request.content:
            print()
            print("Request body:")
            print(request.content.decode())

        response: httpx.Response = await super().send(request, transport)

        print()
        print("Response headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        if "Content-Length" in response.headers and int(response.headers["Content-Length"]) > 0:
            print()
            print("Response body:")
            response_content = await response.read()
            print(f"Response content: {response_content.decode()}")