import reflex as rx
from typing import Dict, List


class AuthState(rx.State):
    users: Dict[str, Dict[str, str]] = {
        "admin@premedika.com": {
            "password": "password123",
            "role": "admin",
        },
        "user@premedika.com": {
            "password": "user123",
            "role": "user",
        },
    }
    in_session: bool = False
    current_user_email: str = ""
    current_user_role: str = ""

    @rx.event
    def sign_up(self, form_data: dict):
        email = form_data["email"]
        password = form_data["password"]
        if email in self.users:
            yield rx.toast("Email already in use")
        else:
            self.users[email] = {
                "password": password,
                "role": "user",
            }
            self.in_session = True
            self.current_user_email = email
            self.current_user_role = "user"
            yield rx.toast("Account created successfully!")
            return rx.redirect("/dashboard")

    @rx.event
    def sign_in(self, form_data: dict):
        email = form_data["email"]
        password = form_data["password"]
        user_data = self.users.get(email)
        if user_data and user_data["password"] == password:
            self.in_session = True
            self.current_user_email = email
            self.current_user_role = user_data["role"]
            if user_data["role"] == "admin":
                yield rx.toast(
                    f"Admin login successful: {email}"
                )
            else:
                yield rx.toast(f"Welcome back, {email}!")
            return rx.redirect("/dashboard")
        else:
            self.in_session = False
            self.current_user_email = ""
            self.current_user_role = ""
            yield rx.toast("Invalid email or password")

    @rx.event
    def sign_out(self):
        self.in_session = False
        self.current_user_email = ""
        self.current_user_role = ""
        yield rx.toast("Signed out successfully.")
        return rx.redirect("/login")

    @rx.event
    def check_session(self):
        if not self.in_session:
            return rx.redirect("/login")

    @rx.event
    def check_admin_access(self):
        if not self.is_admin:
            yield rx.toast(
                "Akses ditolak. Hanya admin yang dapat mengakses halaman ini."
            )
            return rx.redirect("/dashboard")

    @rx.var
    def is_admin(self) -> bool:
        return self.current_user_role == "admin"

    @rx.var
    def user_list_for_display(self) -> List[Dict[str, str]]:
        return [
            {"email": email, "role": data["role"]}
            for email, data in self.users.items()
        ]