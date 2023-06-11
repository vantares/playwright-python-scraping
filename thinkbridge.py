from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.g2.com/products/bitly/reviews")
    page.goto("https://www.g2.com/products/bitly/reviews?__cf_chl_rt_tk=xmQozSqMuIXJLLRobE_dJc84c1rC0UGM3O076Z2SjKw-1686456258-0-gaNycGzNC6U")
    page.goto("https://www.g2.com/products/bitly/reviews")
    page.frame_locator("iframe[title=\"Widget containing a Cloudflare security challenge\"]").get_by_label("Verify you are human").check()
    page.locator("div:nth-child(3) > .link").first.click()
    page.get_by_text("Bitly is a leading global SaaS company offering a comprehensive platform designe").click()
    page.get_by_text("Bitly is a leading global SaaS company offering a comprehensive platform designe").click()
    page.get_by_text("Bitly is a leading global SaaS company offering a comprehensive platform designe").click()
    with page.expect_popup() as page1_info:
        page.get_by_text("WebsiteBitly", exact=True).click()
    page1 = page1_info.value
    page1.frame_locator("iframe[title=\"Widget containing a Cloudflare security challenge\"]").get_by_label("Verify you are human").check()
    page1.goto("https://www.g2.com/external_clickthroughs/record?secure%5Bproduct_id%5D=1622&secure%5Btoken%5D=76904a0c3230575efeed525685308de2834a08123e22ec8d57ff3e85c1e7a9db&secure%5Burl%5D=https%3A%2F%2Fbitly.com%2Fpages%2Fpricing&secure%5Burl_type%5D=product_website")
    page1.goto("https://www.g2.com/external_clickthroughs/record?secure%5Bproduct_id%5D=1622&secure%5Btoken%5D=76904a0c3230575efeed525685308de2834a08123e22ec8d57ff3e85c1e7a9db&secure%5Burl%5D=https%3A%2F%2Fbitly.com%2Fpages%2Fpricing&secure%5Burl_type%5D=product_website&__cf_chl_rt_tk=6PDvzH_Nba6YtCNeR_oEl5VyqD0xIbF9Tp5cME4nTS0-1686456344-0-gaNycGzNEvs")
    page1.goto("https://www.g2.com/external_clickthroughs/record?secure%5Bproduct_id%5D=1622&secure%5Btoken%5D=76904a0c3230575efeed525685308de2834a08123e22ec8d57ff3e85c1e7a9db&secure%5Burl%5D=https%3A%2F%2Fbitly.com%2Fpages%2Fpricing&secure%5Burl_type%5D=product_website")
    page1.frame_locator("iframe[title=\"Widget containing a Cloudflare security challenge\"]").get_by_label("Verify you are human").check()
    page1.goto("https://www.g2.com/external_clickthroughs/record?secure%5Bproduct_id%5D=1622&secure%5Btoken%5D=76904a0c3230575efeed525685308de2834a08123e22ec8d57ff3e85c1e7a9db&secure%5Burl%5D=https%3A%2F%2Fbitly.com%2Fpages%2Fpricing&secure%5Burl_type%5D=product_website")
    page1.goto("https://www.g2.com/external_clickthroughs/record?secure%5Bproduct_id%5D=1622&secure%5Btoken%5D=76904a0c3230575efeed525685308de2834a08123e22ec8d57ff3e85c1e7a9db&secure%5Burl%5D=https%3A%2F%2Fbitly.com%2Fpages%2Fpricing&secure%5Burl_type%5D=product_website&__cf_chl_rt_tk=Fh0VkHJanyREtpzN5_N11yDFGkGKY6AVLwgkvzOD4.A-1686456361-0-gaNycGzNEvs")
    page1.goto("https://www.g2.com/external_clickthroughs/record?secure%5Bproduct_id%5D=1622&secure%5Btoken%5D=76904a0c3230575efeed525685308de2834a08123e22ec8d57ff3e85c1e7a9db&secure%5Burl%5D=https%3A%2F%2Fbitly.com%2Fpages%2Fpricing&secure%5Burl_type%5D=product_website")
    page.get_by_text(".st0{fill:#252530} WebsiteBitlyDiscussionsBitly CommunityLanguages SupportedEngl").click()
    page.get_by_text(".st0{fill:#252530} WebsiteBitlyDiscussionsBitly CommunityLanguages SupportedEngl").click()
    page1.frame_locator("iframe[title=\"Widget containing a Cloudflare security challenge\"]").get_by_label("Verify you are human").check()
    page1.close()
    page.get_by_text("Bitly Details.st0{fill:#252530} WebsiteBitlyDiscussionsBitly CommunityLanguages ").click(button="right")
    page.locator("div").filter(has_text=re.compile(r"^Languages SupportedEnglish$")).first.click(button="right")
    page.get_by_text(".st0{fill:#252530} WebsiteBitly").click(button="right")
    page.get_by_role("link", name="Bitly Community").click(button="right")
    page.get_by_text("Languages SupportedEnglish").click(button="right")
    page.get_by_text("Bitly Details.st0{fill:#252530} WebsiteBitlyDiscussionsBitly CommunityLanguages ").click(button="right")
    page.get_by_role("link", name="Bitly Reviews G2 recognized Bitly").click(button="right")
    page.get_by_role("link", name="Features").first.click()
    page.get_by_title("Error details").click()
    page.goto("https://www.g2.com/products/bitly/features")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
