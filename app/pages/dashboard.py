import reflex as rx
from app.states.auth_state import AuthState
from app.states.sidebar_state import SidebarState
from app.components.sidebar import sidebar
from app.components.navbar import navbar


def dashboard_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            f"Welcome to PREMEDIKA Dashboard, {AuthState.current_user_email}!",
            class_name="text-2xl font-bold text-gray-800 mb-6",
        ),
        rx.el.p(
            "Silakan pilih menu dari sidebar untuk memulai.",
            class_name="text-gray-600",
        ),
        class_name="p-6",
    )


def dashboard_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                dashboard_content(),
                class_name="flex-1 overflow-y-auto p-6 bg-gray-50",
            ),
            class_name=rx.cond(
                SidebarState.is_sidebar_open,
                "flex flex-col flex-1 min-h-screen ml-64 transition-all duration-300 ease-in-out",
                "flex flex-col flex-1 min-h-screen ml-16 transition-all duration-300 ease-in-out",
            ),
        ),
        on_mount=AuthState.check_session,
        class_name="flex min-h-screen bg-gray-100",
    )