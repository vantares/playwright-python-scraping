from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.g2.com/products/tinyurl/reviews")
    page.goto("https://www.g2.com/products/tinyurl/reviews?__cf_chl_rt_tk=TkCOc7IS0Hcwmq3K1DUO3CQBeFlUOLA8GHHQZd1Gsz0-1686371530-0-gaNycGzNC5A")
    page.goto("https://www.g2.com/products/tinyurl/reviews")
    page.frame_locator("iframe[title=\"Widget containing a Cloudflare security challenge\"]").get_by_label("Verify you are human").check()
    page.get_by_role("link", name="Cookie Policy").press("Control+c")
    page.locator(".paper > a").first.click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
