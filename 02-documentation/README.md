# Async Task Scheduler

A lightweight, memory-efficient asynchronous task runner for Python. This library allows you to schedule background functions with optional delays and track their execution status in real-time.

## Key Features

- **Asynchronous Execution**: Leverages `asyncio` to run tasks without blocking the main event loop.
- **Delayed Scheduling**: Specify a delay in seconds before a task starts.
- **Task Tracking**: Unique UUIDs are generated for every task, allowing status polling.
- **Google-Style Documentation**: Fully documented with clear type hints and docstrings.

## Quick Start

```python
import asyncio
from scheduler import schedule_task, wait_for_all, get_task_status

async def my_long_running_job():
    print("Working...")
    await asyncio.sleep(2)
    print("Done!")

async def main():
    # 1. Schedule a task with a 1-second delay
    task_id = await schedule_task(my_long_running_job, delay=1.0)
    print(f"Task ID: {task_id}")

    # 2. Check initial status
    status = get_task_status(task_id)
    print(f"Current Status: {status['status']}") # -> PENDING

    # 3. Wait for completion
    await wait_for_all()

    # 4. Check final status
    final_status = get_task_status(task_id)
    print(f"Final Status: {final_status['status']}") # -> DONE

if __name__ == "__main__":
    asyncio.run(main())
```

## API Reference

### `schedule_task(func, delay=0)`
Schedules `func` to run in the background. Returns a `str` (UUID).

### `get_task_status(task_id)`
Returns a dictionary with `status`, `queued_at`, `completed_at`, and `error` (if applicable).

### `wait_for_all()`
A blocking async call that returns only when the internal task queue is empty.
