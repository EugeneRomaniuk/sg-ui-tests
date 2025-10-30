GAME_NAME = "StarCraft II"


def test_find_streamer_by_category(app, screenshot_util):
    # 1. go to Twitch
    app.home_page.open()
    app.home_page.accept_cookies_button.should.be_clickable().click()

    # 2. click in the search icon
    app.home_page.browse_button.click()

    # 3. input StarCraft II
    app.browse_page.search_for(GAME_NAME)
    app.browse_page.get_category_link_by_name(GAME_NAME).should.be_clickable().click()

    # 4. scroll down 2 times
    app.category_page.wait_for_page_load()
    app.category_page.scroll_down_with_delay(1)
    app.category_page.scroll_down_with_delay(1)

    # 5. select one streamer
    app.category_page.click_on_any_stream()

    # 6. on the streamer page wait until all is load and take a screenshot
    app.streamer_page.video.should.be_present()
    app.streamer_page.close_content_gate_popup_if_appeared()
    app.streamer_page.chat_welcome_message.should.be_visible()
    app.streamer_page.wait_for_video_to_be_played()
    screenshot_util.save_screenshot()
