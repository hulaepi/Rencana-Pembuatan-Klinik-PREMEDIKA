import reflex as rx
from app.states.auth_state import AuthState
from app.states.sidebar_state import SidebarState
from app.components.sidebar import sidebar
from app.components.navbar import navbar


def user_management_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Manajemen Pengguna",
            class_name="text-2xl font-bold text-gray-800 mb-6",
        ),
        rx.el.p(
            "Halaman ini ditujukan untuk admin mengelola akun pengguna.",
            class_name="text-gray-600 mb-4",
        ),
        rx.el.div(
            rx.el.h2(
                "Daftar Pengguna",
                class_name="text-xl font-semibold text-gray-700 mb-4",
            ),
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Email",
                            class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600 bg-gray-100 border-b",
                        ),
                        rx.el.th(
                            "Role",
                            class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600 bg-gray-100 border-b",
                        ),
                        rx.el.th(
                            "Aksi",
                            class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600 bg-gray-100 border-b",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        AuthState.user_list_for_display,
                        lambda user_data: rx.el.tr(
                            rx.el.td(
                                user_data["email"],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                user_data["role"],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                rx.el.button(
                                    "Edit",
                                    class_name="text-xs px-2 py-1 bg-yellow-400 text-white rounded mr-1 hover:bg-yellow-500",
                                ),
                                rx.el.button(
                                    "Delete",
                                    class_name="text-xs px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600",
                                ),
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                        ),
                    ),
                    rx.cond(
                        AuthState.user_list_for_display.length()
                        == 0,
                        rx.el.tr(
                            rx.el.td(
                                "Tidak ada pengguna terdaftar.",
                                col_span=3,
                                class_name="text-center py-4 text-gray-500",
                            )
                        ),
                    ),
                ),
                class_name="min-w-full bg-white shadow rounded-lg",
            ),
            class_name="bg-white p-6 rounded-lg shadow-md",
        ),
        class_name="p-6",
    )


def user_management_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                user_management_content(),
                class_name="flex-1 overflow-y-auto p-6 bg-gray-50",
            ),
            class_name=rx.cond(
                SidebarState.is_sidebar_open,
                "flex flex-col flex-1 min-h-screen ml-64 transition-all duration-300 ease-in-out",
                "flex flex-col flex-1 min-h-screen ml-16 transition-all duration-300 ease-in-out",
            ),
        ),
        on_mount=[
            AuthState.check_session,
            AuthState.check_admin_access,
            lambda: SidebarState.set_active_page(
                "user_management"
            ),
        ],
        class_name="flex min-h-screen bg-gray-100",
    )