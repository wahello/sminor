from .models import Category

# ná í alla flokka
def categories_processor(request):
    heim = Category.objects.get(name="Heimilistæki")
    raf = Category.objects.get(name="Söludeild rafbúnaðar")
    return {
        'catHeim': heim,
        'catRaf': raf
        }
