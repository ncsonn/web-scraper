# Web Scraper
Dynamic Web Scraping API with Python and Playwright

## Prerequisites
- Python 3.8 or higher.
- Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL).
- macOS 13 Ventura, or later.
- Debian 12, Ubuntu 22.04, Ubuntu 24.04, on x86-64 and arm64 architecture.

## Deployment
1. **Clone the repository:**
    ```bash
    git clone https://github.com/ncsonn/web-scraper.git
    cd web-scraper
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

3. **Start the API server:**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

    - Check if the server is running:
    ```bash
    curl -X GET http://localhost:8000/health-check
    ```

4. **Access the endpoints:**
    - Get website HTML:
    ```bash
    curl -X GET http://localhost:8000/scrape/html?url=https://example.com/
    ```

    - Get website screenshot:
    ```bash
    curl -X GET http://localhost:8000/scrape/image?url=https://playwright.dev/
    ```

## Stop the Server
To stop the API server, press `Ctrl+C` in the terminal where the server is running.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.