from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.g2.com/products/bitly/reviews")
    page.goto("https://www.g2.com/products/bitly/reviews?__cf_chl_rt_tk=2.1zYgkOS.DrcntvpVPN0BQp5IqYGIIxwY.tDQ0nx5U-1686417771-0-gaNycGzNC7s")
    page.goto("https://www.g2.com/products/bitly/reviews")
    page.frame_locator("iframe[title=\"Widget containing a Cloudflare security challenge\"]").get_by_label("Verify you are human").check()
    page.goto("https://www.g2.com/products/bitly/reviews")
    page.get_by_text("Bitly is a leading global SaaS company offering a comprehensive platform designe").click()
    page.get_by_text("WebsiteBitly", exact=True).click()
    page.get_by_text("SellerBitly, Inc.").click()
    page.get_by_text("Company Websitebitly.com").click()
    page.get_by_text("Year Founded2008").click()
    page.get_by_text("HQ LocationNew York").click()
    page.locator("div:nth-child(3) > .link").first.click()
    page.get_by_text("Champion Diversity, Equity, and Inclusion").click()
    page.get_by_text("URL Shortener Average: 9.1").first.click()
    page.get_by_text("URL Shortener Average: 8.6").click()
    page.get_by_text("URL Shortener Average: 9.1").nth(1).click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
