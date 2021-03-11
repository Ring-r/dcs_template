from celery import Celery

app = Celery('workers.worker0')

@app.task(bind=True)
def hello_world(self):
	return 'hello world'

if __name__ == '__main__':
	app.start()
