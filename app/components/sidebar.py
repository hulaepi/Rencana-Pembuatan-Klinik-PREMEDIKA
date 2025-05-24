import reflex as rx
from app.states.sidebar_state import SidebarState
from app.states.auth_state import AuthState


def sidebar_link(
    icon_name: str, text: str, href: str, page_name: str
) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(tag=icon_name, class_name="h-5 w-5"),
            rx.el.span(
                text,
                class_name=rx.cond(
                    SidebarState.is_sidebar_open,
                    "opacity-100",
                    "opacity-0",
                ),
            ),
            class_name=rx.cond(
                SidebarState.active_page == page_name,
                "flex items-center gap-3 rounded-lg bg-teal-100 px-3 py-2 text-teal-700 transition-all hover:text-teal-700",
                "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-700 transition-all hover:bg-gray-100 hover:text-gray-900",
            ),
        ),
        href=href,
        on_click=lambda: SidebarState.set_active_page(
            page_name
        ),
        class_name="w-full",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        tag="activity",
                        class_name="h-8 w-8 text-teal-600",
                    ),
                    rx.el.span(
                        "PREMEDIKA",
                        class_name=rx.cond(
                            SidebarState.is_sidebar_open,
                            "text-xl font-bold text-teal-700 ml-2",
                            "hidden",
                        ),
                    ),
                    href="/dashboard",
                    class_name="flex items-center",
                    on_click=lambda: SidebarState.set_active_page(
                        "dashboard"
                    ),
                ),
                rx.el.button(
                    rx.icon(
                        tag=rx.cond(
                            SidebarState.is_sidebar_open,
                            "panel-left-close",
                            "panel-right-close",
                        ),
                        class_name="h-6 w-6",
                    ),
                    on_click=SidebarState.toggle_sidebar,
                    class_name="p-2 rounded-md hover:bg-gray-200 focus:outline-none",
                ),
                class_name="flex h-16 items-center justify-between border-b px-4 lg:px-6 sticky top-0 bg-white z-10",
            ),
            rx.el.nav(
                sidebar_link(
                    "layout-dashboard",
                    "Dashboard",
                    "/dashboard",
                    "dashboard",
                ),
                rx.el.h3(
                    "Manajemen Data Pasien",
                    class_name=rx.cond(
                        SidebarState.is_sidebar_open,
                        "text-xs font-semibold text-gray-500 uppercase tracking-wider mt-4 mb-2 px-3",
                        "hidden",
                    ),
                ),
                sidebar_link(
                    "file-text",
                    "Rekapan Hasil MCU",
                    "/mcu-recap",
                    "mcu_recap",
                ),
                sidebar_link(
                    "file-check",
                    "Rekap Hasil Follow Up",
                    "/follow-up-recap",
                    "follow_up_recap",
                ),
                sidebar_link(
                    "stethoscope",
                    "Kunjungan Berobat",
                    "/clinic-visit",
                    "clinic_visit",
                ),
                rx.el.h3(
                    "Inspeksi Medis",
                    class_name=rx.cond(
                        SidebarState.is_sidebar_open,
                        "text-xs font-semibold text-gray-500 uppercase tracking-wider mt-4 mb-2 px-3",
                        "hidden",
                    ),
                ),
                sidebar_link(
                    "fire_extinguisher",
                    "Inspeksi Alat P3K",
                    "/first-aid-inspection",
                    "first_aid_inspection",
                ),
                sidebar_link(
                    "ambulance",
                    "Inspeksi Ambulans",
                    "/ambulance-inspection",
                    "ambulance_inspection",
                ),
                rx.cond(
                    AuthState.is_admin,
                    rx.fragment(
                        rx.el.h3(
                            "Admin",
                            class_name=rx.cond(
                                SidebarState.is_sidebar_open,
                                "text-xs font-semibold text-gray-500 uppercase tracking-wider mt-4 mb-2 px-3",
                                "hidden",
                            ),
                        ),
                        sidebar_link(
                            "users",
                            "Manajemen Pengguna",
                            "/user-management",
                            "user_management",
                        ),
                    ),
                ),
                rx.el.h3(
                    "Bantuan",
                    class_name=rx.cond(
                        SidebarState.is_sidebar_open,
                        "text-xs font-semibold text-gray-500 uppercase tracking-wider mt-4 mb-2 px-3",
                        "hidden",
                    ),
                ),
                sidebar_link(
                    "circle_plus",
                    "Bantuan Deployment",
                    "/deployment-help",
                    "deployment_help",
                ),
                class_name="flex-1 overflow-auto py-4 px-2 space-y-1",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name=rx.cond(
            SidebarState.is_sidebar_open,
            "fixed inset-y-0 left-0 z-20 flex h-full w-64 flex-col border-r bg-white transition-all duration-300 ease-in-out",
            "fixed inset-y-0 left-0 z-20 flex h-full w-16 flex-col border-r bg-white transition-all duration-300 ease-in-out",
        ),
    )