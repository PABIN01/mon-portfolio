from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        # Rate limiting manuel : 5 messages par heure par IP
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
        cache_key = f'contact_ratelimit_{ip}'
        attempts = cache.get(cache_key, 0)

        if attempts >= 5:
            messages.error(request, 'Trop de messages envoyés. Veuillez réessayer dans une heure.')
            return redirect('contact')

        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            cache.set(cache_key, attempts + 1, 3600)  # 1 heure
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