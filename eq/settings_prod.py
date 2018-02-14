import os


DEBUG = False

GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID', '')


RAVEN_CONFIG = {
    'dsn': os.getenv('SENTRY_DNS', ''),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}