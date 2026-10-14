from app.core.config import Settings


def test_settings_load_from_explicit_values() -> None:
    settings = Settings(
        _env_file=None,
        postgres_user="test_user",
        postgres_password="test_pass",
        postgres_host="localhost",
        postgres_port=5433,
        postgres_db="test_db",
    )
    assert settings.postgres_db == "test_db"
    assert "test_user" in settings.database_url
    assert "test_db" in settings.database_url


def test_cors_origins_parses_comma_separated_list() -> None:
    settings = Settings(_env_file=None, cors_allowed_origins="http://a.test, http://b.test")
    assert settings.cors_origins == ["http://a.test", "http://b.test"]
