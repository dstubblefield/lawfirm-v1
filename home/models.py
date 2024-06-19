from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    parent_page_type = ["wagtailcore.Page"]
    template = "home/home_page.html"
    description = RichTextField(blank=True) 
    
    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ] 
