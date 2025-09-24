# update_dates.py
import os
import django
from django.utils import timezone

# === configure Django ===
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # <- change if your project folder name is different
django.setup()

from myapp.models import Post  # <- your app name (you showed it's "myapp")

TARGET_YEAR = 2025
updated = 0

for p in Post.objects.all():
    try:
        if p.time:
            # try to replace year while keeping month/day/time
            try:
                p.time = p.time.replace(year=TARGET_YEAR)
            except ValueError:
                # e.g., Feb 29 -> non-leap year: fallback to Mar 1 same year
                p.time = p.time.replace(month=3, day=1, year=TARGET_YEAR)
        else:
            # If time is None, set it to the current datetime but with TARGET_YEAR
            now = timezone.now()
            try:
                p.time = now.replace(year=TARGET_YEAR)
            except ValueError:
                p.time = timezone.datetime(TARGET_YEAR, 1, 1, tzinfo=now.tzinfo)
        p.save()
        updated += 1
    except Exception as exc:
        print(f"Skipped post id={p.id} due to error: {exc}")

print(f"Updated {updated} posts to year {TARGET_YEAR}")
