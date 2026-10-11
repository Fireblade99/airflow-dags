from datetime import datetime
from airflow.sdk import dag, task

@dag(schedule=None, start_date=datetime(2026, 1, 1), catchup=False, tags=["lab"])
def hello_k8s():
    @task
    def extract():
        return [1, 2, 3]

    @task
    def transform(nums):
        return sum(nums)

    @task
    def load(total):
        print(f"Итого: {total}")

    load(transform(extract()))

hello_k8s()