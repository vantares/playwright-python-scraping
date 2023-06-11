import json
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.g2.com/products/bitly/reviews")
    page.wait_for_url("https://www.g2.com/products/bitly/reviews")
    # page.get_by_text("Show More").nth(2).click()
    # page.locator(".hide-for-custom-profile").locator(".link .x-toggle-visible-initialized").locator("a").click()
    base_company_locator = page.locator(".hide-for-custom-profile .paper--nestable").nth(2)

    # name = base_company_locator.get_by_text("Seller").locator(".ml-1").inner_text()
    name = page.locator(".product-head__title").locator("a").first.inner_text()
    website = base_company_locator.get_by_text("Website").inner_text()
    # year_fundation = base_company_locator.get_by_text("Year Founded").inner_text()
    # location = base_company_locator.get_by_text("HQ Location").inner_text()
    #  page.locator(".product-head__logo").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
    # company ={
    #     "name": name,
    #     "website": website,
    #     "year_fundation": year_fundation,
    #     "location": location
    # }
    # print(json.dumps(company))
    print(name)
    print(website)


with sync_playwright() as playwright:
    run(playwright)
