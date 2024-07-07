import time
import uvicorn
from fastapi import FastAPI
from routers import course, student, master

app = FastAPI()

app.include_router(course.router)
app.include_router(master.router)
app.include_router(student.router)


def long_running_process():
    """
    Simulates a long-running process, allowing interruption with cleanup.
    """
    try:
        print("Performing a long-running process. Press Ctrl+C to interrupt.")
        for i in range(5):
            time.sleep(1)
            print(f"Processing step {i + 1}")
    except KeyboardInterrupt:
        print("\nInterrupted! Cleaning up before exiting.")
    finally:
        print("Exiting the program.")
    
if __name__ == "__main__":
    try:
        uvicorn.run(app)
    except KeyboardInterrupt:
        long_running_process()