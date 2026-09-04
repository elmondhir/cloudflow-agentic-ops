from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CloudFlow Agentic Operations"
    app_env: str = "development"

    foundry_project_endpoint: str = ""
    foundry_model_deployment: str = ""

    snowflake_account: str = ""
    snowflake_user: str = ""
    snowflake_password: str = ""
    snowflake_database: str = ""
    snowflake_schema: str = ""
    snowflake_warehouse: str = ""
    snowflake_role: str = ""

    snowflake_mcp_token: str = ""
    snowflake_mcp_url: str = ""

    airflow_base_url: str = "http://localhost:8080"
    airflow_username: str = ""
    airflow_password: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()