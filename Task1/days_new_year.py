from datetime import date
print(f"До Нового года: {(date(date.today().year + 1, 1, 1) - date.today()).days} дней")
