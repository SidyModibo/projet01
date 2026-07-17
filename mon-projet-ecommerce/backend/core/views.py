# backend/core/views.py
from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API E-commerce</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #2563eb; }
            ul { list-style: none; padding: 0; }
            li { padding: 10px; margin: 5px 0; background: #f3f4f6; border-radius: 5px; }
            a { color: #2563eb; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>🚀 API E-commerce</h1>
        <p>Bienvenue sur l'API de votre site e-commerce</p>
        <h2>Endpoints disponibles :</h2>
        <ul>
            <li><a href="/admin/">📊 Admin</a></li>
            <li><a href="/api/users/">👤 Utilisateurs</a></li>
            <li><a href="/api/products/">📦 Produits</a></li>
            <li><a href="/api/orders/">📋 Commandes</a></li>
            <li><a href="/api/docs/">📚 Documentation Swagger</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)