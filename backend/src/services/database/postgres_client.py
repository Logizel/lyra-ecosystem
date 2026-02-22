import os

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError

from typing import Iterator
from models.database.user import User
from dotenv import load_dotenv

load_dotenv()


class PostgresClient:
    def __init__(self) -> None:
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            raise RuntimeError("DATABASE_URL is not set!")

        self.engine = create_engine(
            self.database_url,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True,
        )

        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
        )

    # Methods should be at class level, NOT inside __init__
    @contextmanager
    def get_session(self) -> Iterator[Session]:
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()

    def create_user(self, email: str, hashed_password: str) -> User:
        with self.get_session() as session:
            user = User(email=email, hashed_password=hashed_password)
            session.add(user)

            try:
                session.commit()
                session.refresh(user)
                return user
            except IntegrityError:
                session.rollback()
                raise

    def get_user_by_email(self, email: str) -> "User | None":
        with self.get_session() as session:
            return session.query(User).filter(User.email == email).first()
