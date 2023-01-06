from fastapi import HTTPException

from ..dependencies import AuthHeaders

from ..clients.internal.users import UsersClient
from ..data.adapter import MongoDbClient


class LayawayService:
    def __init__(self) -> None:
        self.users_client = UsersClient()
        self.mongo_client = MongoDbClient()

    async def __get_logged_user(self, headers: AuthHeaders):
        user = await self.users_client.get_logged_user(headers.to_dict())
        if not user:
            raise HTTPException(401, "Invalid Credentials")
        return user

    async def __validate_document_existence(self, user_id: str):
        return self.mongo_client.find_one_by_id_user(user_id) is not None
