from django.conf import settings


def google_analytics(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID}
