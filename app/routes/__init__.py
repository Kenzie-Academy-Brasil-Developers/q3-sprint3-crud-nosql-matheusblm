from flask import Flask


def init_app(app: Flask):
    from app.routes.user_routes import posts
    posts(app)

