from datetime import datetime
current_time = datetime.now()
new_time = current_time.replace(microsecond=0)

print("Текущее время:", current_time)  
print("Время без микросекунд:", new_time)
