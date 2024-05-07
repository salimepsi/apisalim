from fastapi import APIRouter


router = APIRouter()


@router.get("/user")
async def read_item():
    return {"user_name": "pierre"}

@router.get("/user_all")
async def get_all():
    return [{"user_name":"amadou"}, {"user_name2": "salim"}]
