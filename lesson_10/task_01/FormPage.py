from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class FormPage:
    """
    Класс PageObject для страницы формы по заполнению пользовательских данных.
    Содержит методы для открытия страницы, заполнения полей, отправки формы
    и проверки результатов валидации.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы.

        :param driver: WebDriver — экземпляр браузера, используемый для работы со страницей.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Значения полей для автозаполнения формы.
        self.fields: dict[str, str] = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self) -> None:
        """
        Открывает страницу формы.

        :return: None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_form(self) -> None:
        """
        Заполняет форму значениями из словаря self.fields.

        :return: None
        """
        for field, value in self.fields.items():
            element = self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            )
            element.send_keys(value)

    def submit_form(self) -> None:
        """
        Нажимает кнопку отправки формы.

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))
        )
        button.click()

    def get_field_class(self, field_id: str) -> str:
        """
        Возвращает значение атрибута class для указанного поля.

        :param field_id: str — ID HTML-элемента поля.
        :return: str — значение атрибута class.
        """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return element.get_attribute("class")

    def check_zip_code_error(self) -> bool:
        """
        Проверяет, отображается ли ошибка валидации для поля zip-code.

        :return: bool — True, если поле содержит класс alert-danger.
        """
        return "alert-danger" in self.get_field_class("zip-code")

    def check_fields_success(self) -> bool:
        """
        Проверяет, что остальные поля заполнены корректно (status success).

        :return: bool — True, если все поля содержат success. Иначе False.
        """
        fields_to_check = [
            'first-name', 'last-name', 'address', 'e-mail', 'phone',
            'city', 'country', 'job-position', 'company'
        ]

        for field in fields_to_check:
            if "success" not in self.get_field_class(field):
                return False

        return True

    def check_form_submission(self) -> None:
        """
        Выполняет проверку корректной отправки формы:
        - zip-code должен быть с ошибкой;
        - остальные поля должны пройти валидацию.

        :return: None
        :raises AssertionError: если хотя бы одно условие не выполнено.
        """
        assert self.check_zip_code_error(), "Поле zip-code должно быть с ошибкой"
        assert self.check_fields_success(), "Корректные поля должны иметь статус success"
