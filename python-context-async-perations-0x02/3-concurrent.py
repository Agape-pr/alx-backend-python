import aiosqlite
import asyncio

# ✅ Async function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            result = await cursor.fetchall()
            print("All Users:")
            for row in result:
                print(row)
            return result

# ✅ Async function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            result = await cursor.fetchall()
            print("\nUsers older than 40:")
            for row in result:
                print(row)
            return result

# ✅ Run both queries concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# ✅ Run it
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
