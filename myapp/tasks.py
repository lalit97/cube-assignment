from celery import shared_task
from .models import Rule, Event
from django.db.models import Count, Sum
from django.utils import timezone
from .utils import create_log


TASK_RUN_TIME = 120


@shared_task
def check_events():
    rules = Rule.objects.all()
    task_window = timezone.now() - timezone.timedelta(seconds=TASK_RUN_TIME)
    events = Event.objects.filter(created_at__gte=task_window)

    for rule in rules:
        if rule.count:
            qs = events.values('user').annotate(count=Count('user'))
            for item in qs:
                if item.get('count') == rule.count:
                    message = f"{rule.name} triggered for {item.get('user')}!\n"
                    create_log(message)

        if rule.total_value:
            window = timezone.now() - timezone.timedelta(seconds=rule.timeframe)
            qs = events.filter(
                created_at__gte=window
                ).values(
                    'user'
                ).annotate(
                    count=Count('user'), 
                    total=Sum('value')
                )
            for item in qs:
                if item.get('count') >= rule.count and item.get('total') >= rule.total_value:
                    message = f"{rule.name} triggered for {item.get('user')}!\n"
                    create_log(message)

        
        if rule.noun == 'fdbk':
            qs = events.filter(noun='fdbk')
            for item in qs:
                user = item.user
                fail_time = timezone.now() - timezone.timedelta(seconds=rule.timeframe)
                bill_pay_events = events.filter(
                    noun='bill',
                    user=user,
                    created_at__gte=fail_time,
                )
                if not bill_pay_events.exists():
                    message = f'{rule.name} triggered for {user}!\n'
                    create_log(message)
