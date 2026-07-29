from django.http import JsonResponse


def custom_404(request, exception=None):
    return JsonResponse(
        {"error": {"status": 404, "message": "The requested resource was not found."}},
        status=404,
    )


def custom_500(request):
    return JsonResponse(
        {
            "error": {
                "status": 500,
                "message": "Internal server error. Please try again later.",
            }
        },
        status=500,
    )
