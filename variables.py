from datetime import datetime

# Current job, how long #
years = divmod(((datetime.now() - datetime(2021, 8, 24, 0, 0, 0)).total_seconds() / 86400), 365)
months = divmod(years[1], 30)
tempo = f"Atualmente, {int(years[0])} ano(s) e {int(months[0])} mes(es)."
