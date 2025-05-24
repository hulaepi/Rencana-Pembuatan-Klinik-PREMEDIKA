import reflex as rx
from app.components.login_form import login_form_component


def login_page() -> rx.Component:
    return rx.el.div(
        login_form_component(),
        class_name="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-teal-50 via-white to-green-50 p-4",
    )