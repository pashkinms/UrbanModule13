import asyncio

BALL_NUMBER = 5
DELAY = 5

async def start_strongman(name: str, power: int):
    print(f'Strongman {name} started to compete!')
    for i in range(1, BALL_NUMBER +1):
        await asyncio.sleep(DELAY/power)
        print(f'Strongman {name} lifted the ball {i}!')
    print(f'Strongman {name} finished the competition!')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollo', 5))
    await task1
    await task2
    await task3
    
asyncio.run(start_tournament())
    