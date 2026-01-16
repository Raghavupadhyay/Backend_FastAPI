from fastapi_jwt_auth import AuthJWT
from app.core.config import settings

class JWTConfig:
    authjwt_secret_key: str = settings.JWT_SECRET

@AuthJWT.load_config
def get_jwt_config():
    return JWTConfig()
