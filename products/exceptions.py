from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        message = (
            response.data.get("detail")
            if isinstance(response.data, dict)
            else response.data
        )
        response.data = {
            "error": {
                "status": response.status_code,
                "message": message,
            }
        }

    return response
