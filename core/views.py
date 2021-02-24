from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Feature, Pricing
from .forms import ContactForm


# Class based view to create my index
class IndexView(FormView):  # My view is a web page that has a form (contact form)
    template_name = 'index.html'  # Definition of my template
    form_class = ContactForm  # Definition of the class belongs my form
    success_url = reverse_lazy('index')  #  If all things works, after submit we going back to index

    # Has something in the context of the page? If yes, we get
    # Override method, get the context, add data and return context
    # For the last, in the templates we can iterate the data
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['service'] = Feature.objects.order_by('?').all()
        context['title'] = Pricing.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar email!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

