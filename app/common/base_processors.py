from django.conf import settings

def main_context_processor(request):
    my_dict = {
        'website_address' : settings.WEBSITE_ADDRESS,
        'website_name_str' : settings.WEBSITE_NAME_STR,
        'website_name_slug': settings.WEBSITE_NAME_SLUG,
        'maintenance' : settings.WEBSITE_STATUS,
    }

    return my_dict


def emailing_context_preocessor(request):
    my_dict = {
        'emailer_team' : settings.EMAILER_TEAM
        }
    return my_dict
