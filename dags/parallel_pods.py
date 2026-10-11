from datetime import datetime
from airflow.sdk import dag, task

@dag(schedule=None, start_date=datetime(2026, 1, 1), catchup=False, tags=["lab"])
def parallel_pods():
    @task
    def work(i: int):
        import socket, time
        print(f"Задача {i} выполняется на поде {socket.gethostname()}")
        time.sleep(30)

    work.expand(i=[1, 2, 3, 4, 5])

parallel_pods()