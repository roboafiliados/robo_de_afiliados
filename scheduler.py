from apscheduler.schedulers.background import BackgroundScheduler
from tasks import executar_tarefas

scheduler = BackgroundScheduler()
scheduler.add_job(executar_tarefas, 'interval', minutes=10)
scheduler.start()
