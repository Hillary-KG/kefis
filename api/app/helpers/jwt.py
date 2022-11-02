from datetime import datetime
from flask_jwt_extended import (create_access_token,
                                create_refresh_token, jwt_required, get_jwt_identity)

# Function to sign Tokens


def sign_token(details):
    try:
        # payload to use as we sign the token
        payload = {
            '_id': details['user_id']
        }

        # jwt_extended
        access_token = create_access_token(identity=payload)
        refresh_token = create_refresh_token(identity=payload)

        return access_token, refresh_token
    except Exception as e:
        exception = f"{datetime.now()}: {str(e)}"
        # log error here
        print(str(exception))
        return None, None