# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import asyncio
import time

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

async def time_elasped():
    # Time elasped starts at zero seconds
    bootTime = await time.time()

    while True:
        await asyncio.sleep(15)
        passedTime = time.time()
    
        elaspedTime = passedTime - bootTime
        return elaspedTime

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
