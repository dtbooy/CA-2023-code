from flask import Blueprint, request
from setup import db, bcrypt
from sqlalchemy.exc import IntegrityError
from models.user import User, UserSchema
from flask_jwt_extended import create_access_token
from datetime import timedelta

users_bp = Blueprint('users', __name__, url_prefix="/users")

# we use /users/register as the path needs to be a resource type / element 
@users_bp.route('/register', methods=["POST"])
def register():
    try:
        # Parse incoming POST body through schema
        user_info = UserSchema(exclude=['id', 'is_admin']).load(request.json) 
        # UserSchema validates the request.json against the fields in the schema
        # NOTE: we exclude id from the schema as this is autogenerated - we exclude is_admin to stop registering as an admin

        # Create new user with the parsed data
        user = User(
            email=user_info['email'],
            password=bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
            name=user_info.get('name', "")
        )
        # print(user.__dict__)

        # Add and commit the new user to the database
        db.session.add(user)
        db.session.commit()
        # print(user_info)
        # print(request.json) # request object contains all the information about the incoming request

        #return the new user with 201 code
        return UserSchema(exclude=['password']).dump(user), 201
    
    except IntegrityError:
        return {"error" : "Email address already in use"}, 409

@users_bp.route('/login', methods=["POST"])
def users_login():
    # 1. PArse incoming POST body through the ma schema
    user_info = UserSchema(exclude=['id', 'name','is_admin']).load(request.json) 
    print(user_info)

    # 2. Select user with email  that matches one in the POST body
    stmt = db.select(User).where(User.email == user_info['email']) #, User.password == bcrypt.generate_password_hash(user_info["password"]).decode('utf8'))
    user = db.session.scalar(stmt)

    # 3. Check Email exists & verify password hash
    if user and bcrypt.check_password_hash(user.password, user_info["password"]):
        # 4. Create JWT token
        token = create_access_token(identity=user.email, expires_delta=timedelta(hours=2)) # can add additional claims, additional_claims={'email' : user.email, 'name' : user.name})
        # 5 return Token
        return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}, 200
    else:
        return {"Error": "Invalid username or password"}, 401
