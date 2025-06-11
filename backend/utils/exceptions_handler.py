from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, AuthenticationFailed):
            response.status_code = status.HTTP_401_UNAUTHORIZED

        if isinstance(response.data, dict):
            messages = []
            for key, value in response.data.items():
                if isinstance(value, list):
                    messages.append(f"{key}: {', '.join(str(v) for v in value)}")
                else:
                    messages.append(f"{key}: {value}")
            message = " | ".join(messages)
        else:
            message = str(response.data)
        return Response({"message": message}, status=response.status_code)
    return Response(
        {"message": "Something went wrong"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
