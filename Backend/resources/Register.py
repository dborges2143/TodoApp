from flask_restful import Resource
from flask import request
from models import db, User
# from models import db, User, UserSchema

# user_schema = UserSchema()


class Register(Resource):

    def get(self):
        users = User.query.all()
        # users = user_schema.dump(users).data
        user_list = []
        for user in users:
            user_list.append(user.serialize())
        return {"status": "success", "data": user_list}, 200

    def post(self):
        # get username, email, password
        # check if username exists
        # check if the email exsits
        # create a user
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input data provided'}, 400

        # data, errors = user_schema.load(json_data)
        # if errors:
        #     return errors, 422
        username = User.query.filter_by(username=json_data['username']).first()
        if username:
            return {'message': 'Username already exists'}, 400

        email = User.query.filter_by(emailaddress=json_data['email']).first()
        if email:
            return {'message': 'Email already exists'}, 400

        user = User(
            username=json_data['username'],
            first_name=json_data['firstname'],
            last_name=json_data['lastname'],
            password=json_data['password'],
            emailaddress=json_data['email']
        )

        db.session.add(user)
        db.session.commit()

        # result = user_schema.dump(user).data
        result = User.serialize(user)

        return {"status": 'success', 'data': result}, 201
