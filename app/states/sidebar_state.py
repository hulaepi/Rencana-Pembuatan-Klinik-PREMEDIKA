import reflex as rx


class SidebarState(rx.State):
    is_sidebar_open: bool = True
    active_page: str = "dashboard"

    @rx.event
    def toggle_sidebar(self):
        self.is_sidebar_open = not self.is_sidebar_open

    @rx.event
    def set_active_page(self, page_name: str):
        self.active_page = page_name