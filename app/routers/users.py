from fastapi import APIRouter
from fake_data import users as user_data

users = APIRouter(
    prefix="",
    tags=["isers"],
    responses={404: {"description": "Not found"}},
)

# get user by id
@users.get("/{item_id}")
async def get_user_by_id(item_id: int):
    print(item_id)
    return user_data[item_id]