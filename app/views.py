from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
from django.http import FileResponse


def home(request):
    context = {"page": "Home"}
    return render(request, "app/index.html", context)


def about(request):
    context = {"page": "About"}
    return render(request, "app/about.html", context)


def contact(request):
    context = {"page": "Contact"}

    if request.method == "POST":
        # Récupérer les données du formulaire
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # Validation basique
        if name and email and subject and message:
            # Ici, vous pouvez ajouter la logique d'envoi d'email
            # Par exemple, utiliser django.core.mail.send_mail()
            # ou un service d'email tiers

            # Pour l'instant, on ajoute un message de succès
            from django.contrib import messages

            messages.success(
                request,
                "Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.",
            )

            # Optionnel : rediriger pour éviter la resoumission du formulaire
            from django.shortcuts import redirect

            return redirect("contact")
        else:
            from django.contrib import messages

            messages.error(request, "Veuillez remplir tous les champs du formulaire.")

    return render(request, "app/contact.html", context)


def robots_txt(request):
    """Serve robots.txt file with dynamic sitemap URL"""
    host = request.get_host()
    protocol = "https" if request.is_secure() else "http"
    base_url = f"{protocol}://{host}"

    robots_content = f"""User-agent: *

Allow: /favicon.ico

Allow: /static/

Disallow:

Sitemap: {base_url}/sitemap.xml
"""
    return HttpResponse(robots_content, content_type="text/plain")


def sitemap_xml(request):
    """Generate and serve sitemap.xml"""
    host = request.get_host()
    protocol = "https" if request.is_secure() else "http"
    base_url = f"{protocol}://{host}"

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>{base_url}/</loc>
        <lastmod>2025-12-07</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{base_url}/a-propos/</loc>
        <lastmod>2025-12-07</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{base_url}/contact/</loc>
        <lastmod>2025-12-07</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>"""

    return HttpResponse(sitemap, content_type="application/xml")


def favicon_view(request):
    favicon_path = os.path.join(settings.STATIC_ROOT, "favicon.ico")
    return FileResponse(open(favicon_path, "rb"), content_type="image/x-icon")
