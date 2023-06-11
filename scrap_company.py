import json
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.g2.com/products/bitly/reviews")
    page.wait_for_url("https://www.g2.com/products/bitly/reviews")
    
    website = page.locator('//*[@id="leads-sticky-top"]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/a').inner_text()
    description = page.locator('//*[@id="leads-sticky-top"]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div/p').inner_text()
    rating = page.locator('//*[@id="products-dropdown"]/div[1]/div[1]/span[1]').inner_text()
    # Click 'show more' to see details
    page.locator('//*[@id="leads-sticky-top"]/div/div[1]/div[3]/div/div[1]/div[2]/a').first.click()
    detail = page.locator('//*[@id="leads-sticky-top"]/div/div[1]/div[3]/div[1]/div/div[2]/div[2]').inner_text()

    page.close()

    # ---------------------
    context.close()
    browser.close()
    print(website)
    print(description)
    print(rating)
    print(detail)


with sync_playwright() as playwright:
    run(playwright)
