# -*- coding: utf-8 -*-
"""
In this file we define common functions that may be useful
in all feature steps.
"""
from acceptance_tests.features.definitions.core.form_interactors import login_form
from acceptance_tests.features.definitions.core.navigators import admin_navigator


def login(username, password):
    login_form.enter_username(username)
    login_form.enter_password(password)
    login_form.submit()


def admin_logs_in():
    admin_navigator.go_to_login_page()
    login('admin', '123')
