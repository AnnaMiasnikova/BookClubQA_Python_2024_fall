import pytest
from faker import Faker

fake = Faker()


def test_register_as_tutor(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake.user_name())
    register.fill_password("sdjflsfdjlksdjflksdjf")
    register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
    register.click_on_become_a_teacher_button()
    register.click_on_registration_button()
    header.create_listing_button_should_be_visible()


@pytest.mark.slow
def test_register_as_student(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")
    register.fill_nick(fake.user_name())
    register.fill_password("sdjflsfdjlksdjflksdjf")
    register.fill_confirm_password("sdjflsfdjlksdjflksdjf")
    register.click_on_registration_button()


#TC_35.001.001.001 | Student >Become a teacher > Navigate to the "Стать репетитором" page
def test_become_a_teacher_from_student_page(header, login, homepage, register):
    """Проверка перехода на страницу регистрации как репетитор из профиля студента."""
    header.visit()
    header.click_on_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.visit()
    homepage.check_2_find_tutor_btns()
    homepage.click_become_tutor_btn()
    register.verify_registration_page_opened()