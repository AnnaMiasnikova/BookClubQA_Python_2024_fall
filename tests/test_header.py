import pytest


def test_login_button_opens_login_page(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_url_login_page("/login")


def test_verify_registration_options_on_registration_page(header, register):
    header.visit()
    header.click_on_registration_button()
    register.header_should_contain_text("Регистрация")


def test_verify_registration_options_on_login_page(header, login):
    header.visit()
    header.click_on_login_button()
    login.check_title_of_registration()


def test_verify_registration_options_on_find_tutor_page(header, find_tutor):
    header.visit()
    header.click_on_find_tutor_button()
    find_tutor.check_title_of_registration()


def test_support_visibility_as_teacher(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    header.support_button_should_be_visible()


def test_support_clickability_as_teacher(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("teacher_test", "a.9QA{!@HDB;en2")
    header.click_on_support_button()


def test_support_visibility_as_student(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.support_button_should_be_visible()


def test_support_clickability_as_student(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.click_on_support_button()


def test_hover_support_button_as_student(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("student_test", "]<c%ZTHH8EZ3L–+")
    header.hover_support_button_color_check()


@pytest.mark.skip("Need fix this test")
def test_verify_redirection_on_profile_page(login, header):
    header.visit()
    header.click_on_login_button()
    login.full_login("Garry", "Potter1$")
    header.click_on_profile_button()
    header.profile_button_should_be_visible()


def test_login_button_is_visible(header):
    header.visit()
    header.login_button_should_be_visible()


def test_become_a_tutor_button_is_visible(header):
    header.visit()


def test_login_button_is_enabled(header):
    header.visit()
    header.login_button_is_enabled()
