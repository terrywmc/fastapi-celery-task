from worker import task_1, task_2
from celery.result import AsyncResult
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

from pydantic import BaseModel

class Task(BaseModel):
    input: int

app = FastAPI()

@app.post("/tasks", status_code=201)
def run_task(payload: Task = Body(
        example={
            "input": 1
        }
    )
):
    # to run single task
    # task = create_task.delay(payload.input)

    # to run chain tasks with perious result
    task = (task_1.s(payload.input) | task_2.s()).apply_async()

    return JSONResponse({"task_id": task.id})


@app.get("/tasks/{task_id}")
def get_status(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)
