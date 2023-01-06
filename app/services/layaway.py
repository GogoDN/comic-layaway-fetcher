from fastapi import HTTPException

from ..dependencies import AuthHeaders, SortParams

from ..clients.internal.users import UsersClient
from ..data.adapter import MongoDbClient


class LayawayService:
    def __init__(self) -> None:
        self.users_client = UsersClient()
        self.mongo_client = MongoDbClient()

    def __get_logged_user(self, headers: AuthHeaders):
        user = self.users_client.get_logged_user(headers.to_dict())
        if not user:
            raise HTTPException(401, "Invalid Credentials")
        return user

    def __get_layaway(self, user_id: str):
        layaway = self.mongo_client.find_one_by_user_id(user_id)
        if not layaway:
            raise HTTPException(404, "Layaway not found")
        return layaway

    def __sort_comics(self, comics: list, sort_param: str):
        if not sort_param:
            return

        reverse = False
        if sort_param[0] == "-":
            sort_param = sort_param[1:]
            reverse = True
        comics.sort(key=lambda x: x[sort_param], reverse=reverse)

    def get_comic_list(self, headers: AuthHeaders, params: SortParams):
        user = self.__get_logged_user(headers)
        layaway = self.__get_layaway(user.get("id"))
        comics = layaway.get("comics")
        self.__sort_comics(comics, params.sortBy)
        return {"comics": comics}
