from openfga_sdk.client import OpenFgaClient
from openfga_sdk.client.configuration import ClientConfiguration
from backend.config import settings

async def get_fga_client():
    configuration = ClientConfiguration(
        api_url=settings.FGA_API_URL,
        store_id=settings.FGA_STORE_ID,
        model_id=settings.FGA_MODEL_ID,
        credentials={
            "method": "client_credentials",
            "configuration": {
                "client_id": settings.FGA_CLIENT_ID,
                "client_secret": settings.FGA_CLIENT_SECRET,
                "api_audience": settings.AUTH0_AUDIENCE,
                "api_issuer": f"https://{settings.AUTH0_DOMAIN}/"
            }
        }
    )
    return OpenFgaClient(configuration)

async def check_access(user_id: str, relation: str, object_id: str):
    async with await get_fga_client() as fga_client:
        response = await fga_client.check(
            body={
                "tuple_key": {
                    "user": f"user:{user_id}",
                    "relation": relation,
                    "object": f"document:{object_id}"
                }
            }
        )
        return response.allowed
