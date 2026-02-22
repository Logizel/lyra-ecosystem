import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from api.auth.authentication import (
    hash_password,
    verify_password,
    create_jwt_token,
    verify_jwt_token,
)


def main():
    print("Testing authentication utilities...\n")

    # Test 1: Password hashing
    print("1. Testing password hashing...")
    plain_password = "my_secure_password123"
    hashed = hash_password(plain_password)
    print(f"   Plain:  {plain_password}")
    print(f"   Hashed: {hashed[:30]}...")

    # Test 2: Password verification (correct)
    print("\n2. Testing password verification (correct)...")
    is_valid = verify_password(plain_password, hashed)
    print(f"   Valid: {is_valid}")
    assert is_valid is True

    # Test 3: Password verification (wrong)
    print("\n3. Testing password verification (wrong)...")
    is_valid = verify_password("wrong_password", hashed)
    print(f"   Valid: {is_valid}")
    assert is_valid is False

    # Test 4: JWT token creation
    print("\n4. Testing JWT token creation...")
    user_id = "58d01fe9-2e02-41f3-80ed-6f8cf2b1b42a"
    token = create_jwt_token(user_id)
    print(f"   Token: {token[:50]}...")

    # Test 5: JWT token verification
    print("\n5. Testing JWT token verification...")
    verified_user_id = verify_jwt_token(token)
    print(f"   Original ID: {user_id}")
    print(f"   Verified ID: {verified_user_id}")
    assert user_id == verified_user_id

    # Test 6: Invalid token
    print("\n6. Testing invalid token...")
    invalid_result = verify_jwt_token("invalid.token.here")
    print(f"   Result: {invalid_result}")
    assert invalid_result is None

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    main()
