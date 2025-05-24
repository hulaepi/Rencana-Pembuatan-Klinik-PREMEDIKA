import reflex as rx
from app.states.auth_state import AuthState
from app.states.sidebar_state import SidebarState


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(),
            rx.el.div(
                rx.el.span(
                    f"User: {AuthState.current_user_email}",
                    class_name="text-sm text-gray-600",
                ),
                rx.el.button(
                    "Sign Out",
                    on_click=AuthState.sign_out,
                    class_name="ml-4 px-3 py-1.5 text-sm font-medium text-white bg-red-500 rounded-md hover:bg-red-600 transition-colors",
                ),
                class_name="flex items-center",
            ),
            class_name="flex h-16 items-center justify-end px-4 lg:px-6 border-b bg-white",
        ),
        class_name="sticky top-0 z-10 w-full",
    )