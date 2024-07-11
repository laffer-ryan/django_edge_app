from pathlib import Path
from functools import lru_cache
from decouple import Config, RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_ENV = BASE_DIR / '.env'
REPO_DIR = BASE_DIR.parent
REPO_DIR_ENV = BASE_DIR / '.env'
REPO_DIR_ENV_WEB = BASE_DIR / '.env.web'

@lru_cache
def get_config():
    if BASE_DIR_ENV.exists():
        return Config(RepositoryEnv(str(BASE_DIR_ENV)))
    elif REPO_DIR_ENV_WEB.exists():
        return Config(RepositoryEnv(str(REPO_DIR_ENV_WEB)))
    elif REPO_DIR_ENV.exists():
        return Config(RepositoryEnv(str(REPO_DIR_ENV)))
    from decouple import config
    return config

config = get_config()

