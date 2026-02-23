import os
import sys
from contextlib import contextmanager
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError

from typing import Iterator, Optional
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from models.database.user import User
from api.auth.authentication import (
    hash_password,
    verify_password,
)

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

    @contextmanager
    def get_session(self) -> Iterator[Session]:
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()

    def create_user(self, email: str, plain_password: str) -> User:
        """Create user with automatic password hashing."""
        with self.get_session() as session:
            hashed_password = hash_password(plain_password)
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

    def authenticate_user(self, email: str, plain_password: str) -> Optional[User]:
        """Verify credentials and return user if valid."""
        with self.get_session() as session:
            user = session.query(User).filter(User.email == email).first()
            if not user:
                return None
            if not verify_password(plain_password, user.hashed_password):
                return None
            return user
