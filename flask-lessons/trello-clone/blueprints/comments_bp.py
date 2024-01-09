from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.comment import Comment, CommentSchema
from auth import authorize

comments_bp = Blueprint("comments", __name__, url_prefix="/<int:card_id>/comments")

# Get All Comments
# @comments_bp.route("/")
# @jwt_required()
# def get_all_comments():
#     # call is_admin check function
#     admin_required()

#     stmt = db.select(Comment)
#     comments = db.session.scalars(stmt) #.all()
#     # dumps returns string, dump return list of dicts
#     return CommentSchema(many=True, exclude=["user.comments"]).dump(comments)

# # Get a single Comment 
# @comments_bp.route("/<int:id>")
# @jwt_required()
# def get_single_comment(id):
#     # call is_admin check function
#     admin_required()
    
#     # Find comment ID in database 
#     stmt = db.select(Comment).filter_by(id=id) # where(Comment.id == id)
#     comment = db.session.scalar(stmt)

#     # If comment ID doesn't exist return 404
#     if not comment:
#         return {"Error": "Comment not Found"}, 404
    
#     # dumps returns string, dump return list of dicts
#     # print(comment.user) # Now that we have established user as a nested property of comment we can access 
#     return CommentSchema().dump(comment)

# Add a comment
@comments_bp.route("/", methods=["POST"])
@jwt_required()
def create_comment(card_id):

    comment_info = CommentSchema(only=["message"]).load(request.json)
    comment = Comment(
        message = comment_info["message"],
        card_id = card_id,
        user_id = get_jwt_identity()
    )
    db.session.add(comment)
    db.session.commit()
    return CommentSchema().dump(comment), 201


# Update a comment 
# # PUT /cards/card_id/comments/comment_id
@comments_bp.route("/<int:comment_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_comment(card_id, comment_id):
    comment_info = CommentSchema(only=["message"]).load(request.json)
    stmt = db.select(Comment).filter_by(id=comment_id)
    comment = db.session.scalar(stmt)
    authorize(comment.user_id)
    if not comment:
        return {"Error" : "Comment Not Found"}, 404

    #update comment using a dict get (ensures if there is no message property it will not change)
    comment.message = comment_info.get("message", comment.message)
    
    # do not need to add comment (already a db object) just commit to save changes to db
    db.session.commit()
    return CommentSchema().dump(comment), 200

#delete a comment
@comments_bp.route("/<int:comment_id>", methods=["DELETE"])
@jwt_required()
def delete_comment(card_id, comment_id):
    stmt = db.select(Comment).filter_by(id=comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        authorize(comment.user_id)
        db.session.delete(comment)
        db.session.commit()
        return {}, 200
    else:
        return {"Error" : "Comment not found"}, 404

# ------------------------Error Handler --------------

# @app.errorhandler(IntegrityError)
# def integrity_error(err):
#     # print(err)
#     print((err.__dict__))
#     return {"error": str(err)}