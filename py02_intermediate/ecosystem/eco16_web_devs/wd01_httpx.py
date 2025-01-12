# 비동기 코드
import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response.status_code)
        print(response.text)

asyncio.run(main())