import asyncio
from pyppeteer import launch
import os

async def download_file():
    browser = await launch(headless=False)
    page = await browser.newPage()
    
    # Set download path
    download_path = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(download_path, exist_ok=True)

    await page._client.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': download_path
    })
    
    # Navigate to the page
    await page.goto('https://discord.com/download')
    

    # Find the download button or link
    download_button = await page.querySelector('a.button-bl.download-button') 

    if download_button:
        await download_button.click()
        print("Downloaded successfully")
    else:
        print("Not found")
    
    # Click the download button
    # await page.click('a.button-bl.download-button')

    await asyncio.sleep(5)

    print(f"File should be downloaded to: {download_path}")

    await browser.close()

asyncio.get_event_loop().run_until_complete(download_file())