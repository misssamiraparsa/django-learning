from django.views.generic import ListView

from site_module.models import SiteSetting
from .forms import ContactUsForm, ContactUsModelForm
from django.views.generic.edit import FormView, CreateView
from .models import ContactUs, UserProfile


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting

        return context

#  def form_valid(self, form):
#     form.save()
#    return super().form_valid(form)

def store_file(file):
    with open('temp/image.jpg , "wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'

# def get(self, request):
#     form = ProfileForm()
#    return render(request, 'contact_module/create_profile_page.html', {
#       'form' : form
#  })

# def post(self, request):
#   submitted_form = ProfileForm(request.POST, request.FILES)

#  if submitted_form.is_valid():
#     #store_file(request.FILES['image'])
#    profile = UserProfile(image=request.FILES["user_image"])
#   profile.save()
#  return redirect('/contact-us/create-profile')

# return render(request, 'contact_module/create_profile_page.html', {
#       'form': submitted_form
#  })

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'
