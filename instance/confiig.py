MOVIE_API_KEY = '52aa730a904ebb3fec8e777c735c94a1'
SECRET_KEY = 'kamikaze'
email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")