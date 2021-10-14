from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app.core.security import verify_password
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_username, random_lower_string


def test_create_user(db: Session) -> None:
    username = random_username()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    assert user.username == username
    assert hasattr(user, "hashed_password")


def test_authenticate_user(db: Session) -> None:
    username = random_username()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    authenticated_user = crud.user.authenticate(db, username=username, password=password)
    assert authenticated_user
    assert user.username == authenticated_user.username


def test_not_authenticate_user(db: Session) -> None:
    username = random_username()
    password = random_lower_string()
    user = crud.user.authenticate(db, username=username, password=password)
    assert user is None


def test_check_if_user_is_active(db: Session) -> None:
    username = random_username()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active is True


def test_check_if_user_is_active_inactive(db: Session) -> None:
    username = random_username()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password, disabled=True)
    user = crud.user.create(db, obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active


def test_check_if_user_is_superuser(db: Session) -> None:
    username = random_username()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is True


def test_check_if_user_is_superuser_normal_user(db: Session) -> None:
    username = random_username()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is False


def test_get_user(db: Session) -> None:
    password = random_lower_string()
    username = random_username()
    user_in = UserCreate(username=username, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    user_2 = crud.user.get(db, id=user.id)
    assert user_2
    assert user.username == user_2.username
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_update_user(db: Session) -> None:
    password = random_lower_string()
    username = random_username()
    user_in = UserCreate(username=username, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    new_password = random_lower_string()
    user_in_update = UserUpdate(password=new_password, is_superuser=True)
    crud.user.update(db, db_obj=user, obj_in=user_in_update)
    user_2 = crud.user.get(db, id=user.id)
    assert user_2
    assert user.username == user_2.username
    assert verify_password(new_password, user_2.hashed_password)
