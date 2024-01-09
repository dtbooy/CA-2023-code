from flask import jsonify, abort
from flask_jwt_extended import get_jwt_identity
from models.user import User
from setup import db


def authorize(user_id=None):
    # check is_admin
    identity = get_jwt_identity()
    stmt = db.select(User).where(User.id == identity)
    user = db.session.scalar(stmt)
    if not (user.is_admin or (user_id and identity == user_id)):
        return abort(jsonify(error=401, description="You are not authorised to perform this action.")), 401
        #abort(make_response(jsonify(message="Must be admin to proceed"), 401))

