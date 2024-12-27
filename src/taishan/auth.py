import base64
import binascii

from starlette.authentication import AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            raise AuthenticationError("Authorization Failed")

        params = conn.headers["Authorization"].split()
        if len(params) != 2:
            raise AuthenticationError("Authorization Failed")

        scheme = params[0].lower()
        auth_code = params[1]
        if scheme == "basic":
            try:
                decoded = base64.b64decode(auth_code).decode("ascii")
            except (ValueError, UnicodeDecodeError, binascii.Error):
                raise AuthenticationError("Invalid basic auth credentials")
            username, _, password = decoded.partition(":")
            # TODO: verify username and password here
            return AuthCredentials(["authenticated"]), SimpleUser(username)

        elif scheme == "bearer":
            username, _, token = auth_code.partition(".")
            # TODO: verify username and token here
            return AuthCredentials(["authenticated"]), SimpleUser(username)
        else:
            raise AuthenticationError("Authorization Failed")
