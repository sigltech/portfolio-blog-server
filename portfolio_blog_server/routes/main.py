from flask import Blueprint, request, jsonify, make_response, current_app as app
from ..models.posts import Post
from ..database.db import db
from functools import wraps
import uuid
import jwt
import datetime

main_routes = Blueprint("main", __name__)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Post.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'token is invalid'})
        return f(current_user, *args, **kwargs)
    return decorator  

@main_routes.route("/posts", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        def post_serializer(post):
            return {
            "id": post.id,
            "content": post.content,
            "title": post.title,
            "date_posted": post.date_posted,
            "description": post.description
            }
        all_posts = Post.query.all()
        return jsonify([*map(post_serializer, all_posts)]),200
    else:
        date = datetime.date.strftime(datetime.date.today(), "%b-%d, %Y")
        post_content = request.json
        post = Post(
            id = f'{uuid.uuid1()}',
            content = post_content['content'],
            title = post_content['title'],
            date_posted = date,
            description = post_content['description']
        )
        db.session.add(post)
        db.session.commit()
        return jsonify({"message": "Post created successfully."}), 201

@main_routes.route("/post/<id>", methods=["GET","PUT", "DELETE"])
def change_post(id):
    if request.method == "PUT":
        content = request.json
        post = Post.query.filter_by(id=id).first()
        # post.description = content["description"]
        post.title = content["title"]
        db.session.commit()
        return jsonify({"message": "Post updated successfully."}), 200
    elif request.method == "GET":
        post = Post.query.filter_by(id=id).first()
        return jsonify({
            "id": post.id,
            "content": post.content,
            "title": post.title,
            "date_posted": post.date_posted,
            "description": post.description
        }), 200
    else:
        post = Post.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()
        return jsonify({"message": "Post deleted successfully."}), 200
