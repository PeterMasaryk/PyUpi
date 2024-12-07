from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.contracts.UserRequest import UserRequest
from app.models.UserModel import UserModel
from app.dependencies import SessionDep
from uuid import uuid4

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=201)
def create_user(request: UserRequest, session: SessionDep) -> str:
    user = UserModel(
        id=str(uuid4()), username=request.username, email=request.email, star_sign=None
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user.id


@router.get("/")
def get_users(session: SessionDep) -> list[UserModel]:
    users = session.exec(select(UserModel)).all()

    return users


@router.get("/{user_id}")
def get_user(user_id: str, session: SessionDep) -> UserModel:
    user = session.get(UserModel, user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail=f"Could not find user with id {user_id}."
        )

    return user


@router.delete("/{user_id}")
def delete_user(user_id: str, session: SessionDep) -> str:
    user = session.get(UserModel, user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail=f"Could not find user with id {user_id}."
        )

    session.delete(user)
    session.commit()

    return f"User with id {user_id} has been deleted."


@router.put("/{user_id}")
def update_user(request: UserRequest, user_id: str, session: SessionDep) -> str:
    user = session.get(UserModel, user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail=f"Could not find user with id {user_id}."
        )

    if request.username:
        user.username = request.username
    if request.email:
        user.email = request.email

    session.commit()
    return f"User with id {user_id} has been updated."
