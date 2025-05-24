import reflex as rx
from app.states.sidebar_state import SidebarState
from app.components.sidebar import sidebar
from app.components.navbar import navbar
from app.states.auth_state import AuthState


def deployment_help_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Bantuan Penyebaran (Deployment)",
            class_name="text-2xl font-bold text-gray-800 mb-6",
        ),
        rx.el.p(
            "Berikut adalah beberapa panduan umum mengenai penyebaran aplikasi Reflex:",
            class_name="mb-4 text-gray-700 font-medium",
        ),
        rx.el.ul(
            rx.el.li(
                "Untuk menjalankan aplikasi secara lokal selama pengembangan, biasanya Anda menggunakan perintah `reflex init` (jika memulai proyek baru) diikuti oleh `reflex run` di terminal Anda.",
                class_name="mb-2",
            ),
            rx.el.li(
                "Setelah dijalankan, aplikasi lokal umumnya dapat diakses melalui peramban web di alamat `http://localhost:3000`.",
                class_name="mb-2",
            ),
            rx.el.li(
                "Untuk penyebaran ke server produksi (misalnya VPS, Vercel, Docker, dll.), Anda perlu mengikuti dokumentasi resmi Reflex dan panduan spesifik dari platform hosting yang Anda pilih. Proses ini mungkin melibatkan pembuatan versi build aplikasi (`reflex export`) dan konfigurasi server.",
                class_name="mb-2",
            ),
            rx.el.li(
                "Masalah umum saat penyebaran bisa meliputi: dependensi yang hilang (pastikan `requirements.txt` sesuai), kesalahan konfigurasi lingkungan server (misalnya variabel lingkungan, port), atau masalah selama proses build aplikasi.",
                class_name="mb-2",
            ),
            rx.el.li(
                "Sebagai AI, saya tidak dapat secara langsung mendiagnosis masalah penyebaran spesifik pada sistem Anda atau mengetahui URL aplikasi Anda setelah berhasil disebar. URL tersebut akan bergantung pada konfigurasi domain dan hosting Anda.",
                class_name="mb-2",
            ),
            rx.el.li(
                "Pastikan semua dependensi yang tercantum dalam `requirements.txt` (seperti `uvicorn`, `gunicorn`, `fastapi`, `pandas`, `openpyxl`) telah terpasang di lingkungan penyebaran Anda.",
                class_name="mb-2",
            ),
            class_name="list-disc list-inside space-y-2 text-gray-600 font-medium",
        ),
        rx.el.p(
            "Untuk informasi lebih lanjut, silakan kunjungi dokumentasi resmi Reflex.",
            class_name="mt-6 text-gray-700 font-medium",
        ),
        class_name="p-6 bg-white rounded-lg shadow-md border border-gray-200",
    )


def deployment_help_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                deployment_help_content(),
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
            lambda: SidebarState.set_active_page(
                "deployment_help"
            ),
        ],
        class_name="flex min-h-screen bg-gray-100",
    )