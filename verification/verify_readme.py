import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 2500})
        # Fix the f-string interpolation
        path = os.path.abspath('verification/readme_preview.html')
        await page.goto(f'file://{path}')
        await page.screenshot(path='verification/readme_preview.png', full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
