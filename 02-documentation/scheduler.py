import asyncio
import uuid
import datetime

t = {}

async def r(i, d, f):
    global t
    await asyncio.sleep(d)
    try:
        await f()
        t[i]['s'] = 'DONE'
    except Exception as e:
        t[i]['s'] = 'ERROR'
        t[i]['e'] = str(e)
    t[i]['c'] = datetime.datetime.now()

async def s(f, d=0):
    i = str(uuid.uuid4())
    t[i] = {'s': 'PENDING', 'q': datetime.datetime.now()}
    asyncio.create_task(r(i, d, f))
    return i

def g(i):
    return t.get(i)

async def w():
    while any(x['s'] == 'PENDING' for x in t.values()):
        await asyncio.sleep(0.1)

# Usage example (to be removed by participant)
async def main():
    async def task1(): print("TASK 1")
    i = await s(task1, 2)
    print(f"Scheduled task {i}")
    await w()
    print(f"Status: {g(i)}")

if __name__ == "__main__":
    asyncio.run(main())
