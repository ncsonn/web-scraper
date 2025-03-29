from playwright.async_api import async_playwright


async def playwright_get_html(input_url: str) -> dict:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(input_url)

        html = await page.content()

        await page.close()
        await browser.close()

        return html


async def playwright_get_screenshot(input_url: str) -> dict:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(input_url)

        screenshot = await page.screenshot()

        await page.close()
        await browser.close()
        return screenshot
