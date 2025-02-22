from datetime import datetime, timedelta
current_date = datetime.now() 
yesterday_date = current_date - timedelta(days=1)
tomorrow_date = current_date + timedelta(days=1)

print("Вчерашняя дата:", yesterday_date.strftime("%Y-%m-%d"))
print("Текущая дата:", current_date.strftime("%Y-%m-%d"))
print("Завташняя дата:", tomorrow_date.strftime("%Y-%m-%d"))