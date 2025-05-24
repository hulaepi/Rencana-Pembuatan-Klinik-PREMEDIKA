import reflex as rx
from app.states.auth_state import AuthState


def register_form_component() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Create your PREMEDIKA account",
                class_name="font-semibold tracking-tight text-2xl text-gray-800",
            ),
            rx.el.p(
                "Enter your email and password to get started.",
                class_name="text-sm text-gray-600 font-medium",
            ),
            class_name="flex flex-col items-center text-center mb-6",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Email",
                    class_name="text-sm font-medium leading-none text-gray-700",
                ),
                rx.el.input(
                    type="email",
                    placeholder="user@example.com",
                    name="email",
                    required=True,
                    class_name="flex h-10 w-full rounded-md border border-gray-300 bg-transparent px-3 py-2 text-sm shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-teal-500",
                ),
                class_name="flex flex-col gap-1.5 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Password",
                    class_name="text-sm font-medium leading-none text-gray-700",
                ),
                rx.el.input(
                    type="password",
                    name="password",
                    required=True,
                    class_name="flex h-10 w-full rounded-md border border-gray-300 bg-transparent px-3 py-2 text-sm shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-teal-500",
                ),
                class_name="flex flex-col gap-1.5 mb-6",
            ),
            rx.el.button(
                "Create Account",
                type="submit",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-semibold transition-colors text-white shadow-md bg-teal-500 hover:bg-teal-600 h-10 px-4 py-2 w-full",
            ),
            rx.el.div(
                rx.el.span(
                    "Already have an account?",
                    class_name="text-sm text-gray-600 font-medium",
                ),
                rx.el.a(
                    "Sign in",
                    href="/login",
                    class_name="text-sm text-teal-600 font-medium underline hover:text-teal-700 transition-colors",
                ),
                class_name="flex flex-row gap-2 mt-4 justify-center",
            ),
            class_name="flex flex-col gap-4",
            on_submit=AuthState.sign_up,
            reset_on_submit=True,
        ),
        class_name="p-8 rounded-xl bg-white flex flex-col gap-6 shadow-xl border border-gray-200 text-gray-800 w-full max-w-md",
    )