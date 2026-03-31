import asyncio
import uuid
import datetime
from typing import Callable, Dict, Any, Optional

# In-memory store for task states
# Key: task_id, Value: dict containing status, results, and timestamps
tasks: Dict[str, Dict[str, Any]] = {}

async def _run_task(task_id: str, delay: float, func: Callable) -> None:
    """Internal helper to execute a task after a delay and update its status.

    Args:
        task_id: Unique identifier for the task.
        delay: Time in seconds to wait before execution.
        func: The asynchronous function to execute.
    """
    global tasks
    await asyncio.sleep(delay)
    try:
        await func()
        tasks[task_id]['status'] = 'DONE'
    except Exception as e:
        tasks[task_id]['status'] = 'ERROR'
        tasks[task_id]['error'] = str(e)
    
    tasks[task_id]['completed_at'] = datetime.datetime.now()

async def schedule_task(func: Callable, delay: float = 0) -> str:
    """Schedules an asynchronous function for background execution.

    Args:
        func: The async function to run.
        delay: Optional delay in seconds before starting the task.

    Returns:
        A unique string ID for tracking the task status.
    """
    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        'status': 'PENDING',
        'queued_at': datetime.datetime.now()
    }
    # Create background task
    asyncio.create_task(_run_task(task_id, delay, func))
    return task_id

def get_task_status(task_id: str) -> Optional[Dict[str, Any]]:
    """Retrieves the current state and metadata for a specific task.

    Args:
        task_id: The unique identifier returned by schedule_task.

    Returns:
        A dictionary containing status, timestamps, and errors if found.
        Returns None if the task_id does not exist.
    """
    return tasks.get(task_id)

async def wait_for_all() -> None:
    """Blocks until all currently pending tasks in the system are completed."""
    while any(task['status'] == 'PENDING' for task in tasks.values()):
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    # Example usage for verification
    async def sample_workflow():
        async def my_job(): 
            print("--- Executing Background Job ---")
            await asyncio.sleep(0.5)

        tid = await schedule_task(my_job, delay=1)
        print(f"Task scheduled with ID: {tid}")
        
        await wait_for_all()
        print(f"Final Status: {get_task_status(tid)}")

    asyncio.run(sample_workflow())
