from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"


class FaqView(TemplateView):
    template_name = "faq.html"

