import reflex as rx
from app.pages.login import login_page
from app.pages.register import register_page
from app.pages.dashboard import dashboard_page
from app.pages.mcu_recap import mcu_recap_page
from app.pages.follow_up_recap import follow_up_recap_page
from app.pages.clinic_visit import clinic_visit_page
from app.pages.first_aid_inspection import (
    first_aid_inspection_page,
)
from app.pages.ambulance_inspection import (
    ambulance_inspection_page,
)
from app.pages.user_management import user_management_page
from app.pages.deployment_help import deployment_help_page
from app.states.auth_state import AuthState
from app.states.sidebar_state import SidebarState
from app.states.data_state import DataState

app = rx.App(
    theme=rx.theme(appearance="light", accent_color="teal"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
    stylesheets=["custom_styles.css"],
)
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")
app.add_page(
    dashboard_page,
    route="/",
    on_load=AuthState.check_session,
)
app.add_page(
    dashboard_page,
    route="/dashboard",
    on_load=AuthState.check_session,
)
app.add_page(
    mcu_recap_page,
    route="/mcu-recap",
    on_load=AuthState.check_session,
)
app.add_page(
    follow_up_recap_page,
    route="/follow-up-recap",
    on_load=AuthState.check_session,
)
app.add_page(
    clinic_visit_page,
    route="/clinic-visit",
    on_load=AuthState.check_session,
)
app.add_page(
    first_aid_inspection_page,
    route="/first-aid-inspection",
    on_load=AuthState.check_session,
)
app.add_page(
    ambulance_inspection_page,
    route="/ambulance-inspection",
    on_load=AuthState.check_session,
)
app.add_page(
    user_management_page,
    route="/user-management",
    on_load=[
        AuthState.check_session,
        AuthState.check_admin_access,
    ],
)
app.add_page(
    deployment_help_page,
    route="/deployment-help",
    on_load=AuthState.check_session,
)