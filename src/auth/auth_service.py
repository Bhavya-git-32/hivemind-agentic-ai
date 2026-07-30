from src.auth.jwt_handler import create_access_token

# Demo user database
fake_user_db = {
    "admin": {
        "username": "admin",
        "password": "admin123"
    }
}


class AuthService:

    @staticmethod
    def login(username: str, password: str):

        user = fake_user_db.get(username)

        if user is None:
            return None

        if user["password"] != password:
            return None

        token = create_access_token(
            {
                "sub": username
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }