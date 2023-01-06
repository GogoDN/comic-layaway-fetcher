from fastapi import Header, Query, HTTPException

from typing import Union


class AuthHeaders:
    def __init__(
        self,
        x_user_id: str = Header(""),
        x_token: str = Header(""),
    ) -> None:
        self.x_user_id = x_user_id
        self.x_token = x_token

    def to_dict(self):
        return {
            "X-User-Id": self.x_user_id,
            "X-Token": self.x_token,
        }


class SortParams:
    ALLOWED_PARAMS = [
        "title",
        "-title",
        "characters",
        "-characters",
        "onSaleDate",
        "-onSaleDate",
    ]

    def __init__(self, sortBy: Union[str, None] = Query(None)):
        self.sortBy = sortBy

    def validate_params(self):
        if self.sortBy is not None and self.sortBy not in self.ALLOWED_PARAMS:
            raise HTTPException(
                400,
                "sortBy param must be one of [ {} ]".format(
                    ", ".join(self.ALLOWED_PARAMS)
                ),
            )
