from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import never_cache
from ratelimit.decorators import ratelimit
from .forms import ContactForm

@ratelimit(key='ip', rate='5/h', method='POST', block=True)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            try:
                send_mail(
                    subject=f"[Portfolio] {msg.subject or 'Nouveau message'} – {msg.name}",
                    message=f"De: {msg.name}\nEmail: {msg.email}\n\n{msg.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, 'Votre message a bien été envoyé ! Je vous répondrai rapidement.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'active': 'contact'})