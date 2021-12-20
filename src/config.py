import os


class AppConfig:
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    APP_SECRET: str = os.getenv(
        "APP_SECRET",
        "MGExYmQ4ZDRiNjQ5NGE1YzkxMDFmM2IxMTcxMTYyNjMxOTA5MGQxZGVmYzI0Njk3OWRlNWYyYjZmY2YxNDQ0Y2NiNGYzYzY0ZTg0NjQ0NjU4NzQ4YmJkYTVkZjQzMWI3"
    )
    CLIMSOFT_DB_URI: str = os.getenv(
        "CLIMSOFT_DB_URI",
        "mysql+mysqldb://root:password@test_opencdms_climsoft_db:3306/climsoft"
    )
    AUTH_DB_URI: str = os.getenv(
        "AUTH_DB_URI",
        "postgresql+psycopg2://postgres:password@test_opencdms_auth_db:5432/auth"
    )
    SURFACE_DB_NAME: str = os.getenv(
        "SURFACE_DB_NAME",
        "surface"
    )
    SURFACE_DB_USER: str = os.getenv(
        "SURFACE_DB_USER",
        "postgres"
    )
    SURFACE_DB_PASSWORD: str = os.getenv(
        "SURFACE_DB_PASSWORD",
        "password"
    )
    SURFACE_DB_HOST: str = os.getenv(
        "SURFACE_DB_HOST",
        "localhost"
    )
    SURFACE_DB_PORT: str = os.getenv(
        "SURFACE_DB_PORT",
        "25432"
    )

    SURFACE_SECRET_KEY: str = os.getenv("SURFACE_SECRET_KEY")


app_config = AppConfig()
