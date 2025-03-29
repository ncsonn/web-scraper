from fastapi import FastAPI, HTTPException, Response

from modules.playwright_utils import playwright_get_html, playwright_get_screenshot

app = FastAPI()


@app.get("/health-check")
async def health_check():
    return {"status_code": 200, "message": "OK"}


@app.get(
    "/scrape/html",
    responses={200: {"content": {"text/html": {}}}},
    response_class=Response,
)
async def get_html(url: str):
    try:
        output_data = await playwright_get_html(url)
        return Response(content=output_data, media_type="text/html")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get(
    "/scrape/image",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
)
async def get_image(url: str):
    try:
        output_data = await playwright_get_screenshot(url)
        return Response(content=output_data, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
