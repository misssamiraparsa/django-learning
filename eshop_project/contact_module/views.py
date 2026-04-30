from django.shortcuts import render, redirect
from django.views import View

from .forms import ContactUsForm, ContactUsModelForm
from django.views.generic.edit import FormView, CreateView

from .models import ContactUs


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm

    success_url = '/contact-us/'


#  def form_valid(self, form):
#     form.save()
#    return super().form_valid(form)

class CreateProfileView(View):
    def get(self, request):
        return render(request, 'contact_module/create_profile_page.html')

    def post(self, request):
        print(request.FILES)
        return redirect('/contact-us/create-profile')
