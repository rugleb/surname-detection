from environs import Env

__all__ = (
    "env",
)

env = Env()  # type: Env

HOST = env.str("HOST", "0.0.0.0")
PORT = env.int("PORT", "8080")

BIND = f"{HOST}:{PORT}"
