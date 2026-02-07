from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime, timedelta
from calendar import monthcalendar
from .models import GymVisit

# Create your views here.
#define API endpoints/logic

@login_required
def calendar_view(request):
    """Display the gym calendar"""
    # Get current month/year or from query params
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    # Get all gym visits for this user this month
    visits = GymVisit.objects.filter(
        user=request.user,
        date__year=year,
        date__month=month
    )
    
    # Set of date strings (YYYY-MM-DD) for this month for quick lookup
    visited_dates = {v.date.isoformat() for v in visits}
    
    # Get calendar for this month (list of weeks, each week = list of day numbers, 0 = empty)
    cal = monthcalendar(year, month)
    # Build grid with (day_number, date_str) for each cell so the template can toggle by date
    calendar_days = []
    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append((0, None))
            else:
                row.append((day, f"{year}-{month:02d}-{day:02d}"))
        calendar_days.append(row)

    # Calculate previous and next months
    if month == 1:
        prev_month, prev_year = 12, year - 1
    else:
        prev_month, prev_year = month - 1, year
    
    if month == 12:
        next_month, next_year = 1, year + 1
    else:
        next_month, next_year = month + 1, year
    
    context = {
        'calendar_days': calendar_days,
        'visited_dates': visited_dates,
        'year': year,
        'month': month,
        'month_name': datetime(year, month, 1).strftime('%B'),
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
        'total_visits': visits.count(),
    }
    
    return render(request, 'calendar.html', context)

@login_required
def toggle_visit(request):
    """Add or remove a gym visit for a specific date"""
    if request.method == 'POST':
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Try to get existing visit
        visit = GymVisit.objects.filter(user=request.user, date=date).first()
        
        if visit:
            # Remove visit if it exists
            visit.delete()
            return JsonResponse({'status': 'removed'})
        else:
            # Add visit if it doesn't exist
            GymVisit.objects.create(user=request.user, date=date)
            return JsonResponse({'status': 'added'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
