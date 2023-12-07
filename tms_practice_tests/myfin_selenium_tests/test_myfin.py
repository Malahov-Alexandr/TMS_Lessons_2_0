


def test_myfin_red_button(setup):
    base, main = setup
    base.open(base.URL)
    main.hover_card_button()
    main.click_red_card_button()
    base.go_to_another_page()
    main.fill_in_the_number_field()
    main.click(main.CONFIRM_BUTTON)
    main.verify_identification_text()
    main.verify_msi_button()
