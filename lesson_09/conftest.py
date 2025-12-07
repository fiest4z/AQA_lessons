import pytest
from database import SessionLocal, engine, Base


@pytest.fixture(scope="session")
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
