from ...backend_config.environment import EnvEntry


ENV_HOST = EnvEntry("CLEARML_API_HOST", "TRAINS_API_HOST")
ENV_WEB_HOST = EnvEntry("CLEARML_WEB_HOST", "TRAINS_WEB_HOST")
ENV_FILES_HOST = EnvEntry("CLEARML_FILES_HOST", "TRAINS_FILES_HOST")
ENV_ACCESS_KEY = EnvEntry("CLEARML_API_ACCESS_KEY", "TRAINS_API_ACCESS_KEY")
ENV_SECRET_KEY = EnvEntry("CLEARML_API_SECRET_KEY", "TRAINS_API_SECRET_KEY")
ENV_AUTH_TOKEN = EnvEntry("CLEARML_AUTH_TOKEN")
ENV_VERBOSE = EnvEntry("CLEARML_API_VERBOSE", "TRAINS_API_VERBOSE", type=bool, default=False)
ENV_HOST_VERIFY_CERT = EnvEntry("CLEARML_API_HOST_VERIFY_CERT", "TRAINS_API_HOST_VERIFY_CERT", type=bool, default=True)
ENV_CONDA_ENV_PACKAGE = EnvEntry("CLEARML_CONDA_ENV_PACKAGE", "TRAINS_CONDA_ENV_PACKAGE")
ENV_NO_DEFAULT_SERVER = EnvEntry("CLEARML_NO_DEFAULT_SERVER", "TRAINS_NO_DEFAULT_SERVER", type=bool, default=True)
ENV_DISABLE_VAULT_SUPPORT = EnvEntry('CLEARML_AGENT_DISABLE_VAULT_SUPPORT', type=bool)
