from app import db
from flask import jsonify


def all_posts():
    list_posts = list(db.posts.find())
    new_posts = []
    for post in list_posts:
        del post["_id"]
        new_posts.append(post)
    return jsonify(list_posts)

def new_post(post_insert):
    db.posts.insert_one(post_insert.__dict__)
    del post_insert.__dict__["_id"]
    return new_post

def verify_keys(data):
    keys = ["title", "author", "tags", "content"]
    for key in data:
        if not key in keys:
            raise KeyError

def len_posts():
    return len(list(db.posts.find()))