from app.controllers.user_controller import new_post, all_posts, verify_keys
from flask  import Flask, jsonify, request
from app.clases.user_class import Post
from datetime import datetime
from app import db

def posts(app: Flask):

    @app.get('/posts')
    def get_all_posts():
        return all_posts(), 200

    @app.post('/posts')
    def create_post():
        list_post = Post(**request.get_json())
        new_post(list_post)
        return jsonify(list_post.__dict__), 201

    @app.get('/posts/<int:id>')
    def get_post_by_id(id):
        try:
            list_post = db.posts.find_one({"id": id})
            del list_post["_id"]
            return jsonify(list_post), 200
        except TypeError: 
            return jsonify(message = "Post nao encontrado"), 404

    @app.delete('/posts/<int:id>')
    def delete_post(id):
        try:
            list_post = db.posts.find_one({"id": id})
            db.posts.delete_one(list_post)
            del list_post["_id"]
            return jsonify(list_post), 202
            
        except TypeError: 
            return jsonify(msg= "Post nao encontrado"), 404
    
    @app.patch('/posts/<int:id>')
    def update_post(id):
        try:
            verify_keys(request.get_json())
            db.posts.update_one({"id": id}, {"$set": {**request.get_json(), "updated_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}})
            list_post = db.posts.find_one({"id": id})
            del list_post["_id"]
            return jsonify(list_post), 200
        except KeyError:
            return jsonify(msg="Chaves erradas"), 400
        except TypeError:
            return jsonify(msg= "Post nao encontrado"), 404
