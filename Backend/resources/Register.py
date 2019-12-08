from flask_restful import Resource
from flask import request
from models import db, User
# from models import db, User, UserSchema
import random
import string

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

        # Generate a unique api key
        unique_key = False
        while not unique_key:
            new_api_key = self.generate_key()
            key_match = User.query.filter_by(api_key=new_api_key).first()
            if not key_match:
                unique_key = True

        user = User(
            api_key=new_api_key,
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

    def generate_key(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(50))
