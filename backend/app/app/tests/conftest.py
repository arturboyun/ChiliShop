from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

from app.core.config import settings
from app.main import app
from app.tests.utils.user import authentication_token_from_username
from app.tests.utils.utils import get_superuser_token_headers


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as cli:
        yield cli


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> Dict[str, str]:
    return get_superuser_token_headers(client)


@pytest.fixture(scope="module")
def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return authentication_token_from_username(
        client=client, username=settings.USERNAME_TEST_USER, db=db
    )
