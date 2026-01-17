from .models import Course, News

def global_navbar_data(request):
    navbar_courses = Course.objects.filter(is_active=True).order_by('-created_at')[:6]
    navbar_news = News.objects.all().order_by('-published_date')[:6]
    
    return {
        'navbar_courses': navbar_courses,
        'navbar_news': navbar_news,
    }