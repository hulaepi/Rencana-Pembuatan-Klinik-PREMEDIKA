import reflex as rx
from app.components.register_form import (
    register_form_component,
)


def register_page() -> rx.Component:
    return rx.el.div(
        register_form_component(),
        class_name="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-teal-50 via-white to-green-50 p-4",
    )