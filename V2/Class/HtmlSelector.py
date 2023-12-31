class HtmlSelector:
    LOGIN_INPUT_EMAIL = '//input[@id="session_key"]'
    LOGIN_INPUT_PASS = '//input[@id="session_password"]'
    LOGIN_BUTTON = '//button[@data-id="sign-in-form__submit-btn"]'
    LINKEDIN_CONTACT_BUTTONS = '//section[@class="artdeco-card ember-view pv-top-card"]//button'
    CONNECT_MODAL = '//div[@role="dialog"]'
    CONNECT_MODAL_ADD_NOTE_BUTTON = '//button[@aria-label="Añadir una nota"]'
    CONNECT_MODAL_TEXT_AREA = '//textarea'
    SEND_MESSAGE_BUTTON_CONTAINER = '//div[@class="artdeco-modal__actionbar ember-view text-align-right"]'
    SEND_MESSAGE_BUTTON = '//button[@aria-label="Enviar ahora"]'
    MENU_OPTIONS_MORE_BUTTON = '//div[@class="artdeco-dropdown__content-inner"]//ul//li'
    CONNECT_MORE_MENU = 'div.pvs-profile-actions div[aria-label="Invita a {name} a conectar"]'

    def connect_more_menu_selector(self, full_name: str = "") -> str:
        """Funcion que retorna el selector con nombre del contacto"""

        return self.CONNECT_MORE_MENU.format(name=full_name)