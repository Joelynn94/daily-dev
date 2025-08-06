from django.conf import settings

def vite_context(request):
    """Add Vite development context to templates."""
    return {
        'USE_VITE_DEV_SERVER': getattr(settings, 'USE_VITE_DEV_SERVER', False)
    }
