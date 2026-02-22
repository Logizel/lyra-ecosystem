import uuid
from src.services.database.postgres_client import PostgresClient
from src.models.database.user import User


def main():
    client = PostgresClient()

    email = "test@example.com"

    # Check if user already exists
    existing_user = client.get_user_by_email(email)
    if existing_user:
        print(f"User already exists: {existing_user.email} (ID: {existing_user.id})")
    else:
        # Create new user
        try:
            user = client.create_user(email, "hashedpwd123")
            print(f"Created user: {user.email} (ID: {user.id})")
        except Exception as e:
            print(f"Failed to create user: {e}")
            return

    # Fetch user
    found_user = client.get_user_by_email(email)
    if found_user:
        print(f"User fetched: {found_user.email} (ID: {found_user.id})")
    else:
        print("User not found")


if __name__ == "__main__":
    main()
