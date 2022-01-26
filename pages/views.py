from django.template.response import TemplateResponse

def home_page_view(request):
    return TemplateResponse(request, 'home.html', {})