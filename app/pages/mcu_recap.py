import reflex as rx
from app.states.auth_state import AuthState
from app.states.sidebar_state import SidebarState
from app.states.data_state import DataState
from app.components.sidebar import sidebar
from app.components.navbar import navbar
from app.utils.data_types import (
    StatusKesehatan,
    StatusFollowUpMCU,
)


def mcu_form() -> rx.Component:
    return rx.el.form(
        rx.el.h2(
            "Tambah Data MCU Baru",
            class_name="text-xl font-semibold text-gray-700 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "NIK",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="nik",
                    placeholder="Nomor Induk Karyawan",
                    required=True,
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Nama",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="nama",
                    placeholder="Nama Lengkap",
                    required=True,
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Jabatan",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="jabatan",
                    placeholder="Jabatan",
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Departemen",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.select(
                    rx.el.option(
                        "Pilih Departemen", value=""
                    ),
                    rx.foreach(
                        DataState.departments,
                        lambda dept: rx.el.option(
                            dept, value=dept
                        ),
                    ),
                    name="departemen",
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm bg-white",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Perusahaan",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.select(
                    rx.el.option(
                        "Pilih Perusahaan", value=""
                    ),
                    rx.foreach(
                        DataState.companies,
                        lambda comp: rx.el.option(
                            comp, value=comp
                        ),
                    ),
                    name="perusahaan",
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm bg-white",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Tanggal MCU",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="tanggal_mcu",
                    type="date",
                    required=True,
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Tanggal Review MCU",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="tanggal_review_mcu",
                    type="date",
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Temuan",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.textarea(
                    name="temuan",
                    placeholder="Deskripsi temuan...",
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm",
                    rows=3,
                ),
                class_name="w-full px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Diagnosa",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        DataState.diagnosa_options,
                        lambda opt: rx.el.option(
                            opt["label"], value=opt["value"]
                        ),
                    ),
                    name="diagnosa_ids",
                    multiple=True,
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm bg-white h-32",
                ),
                rx.el.form(
                    rx.el.input(
                        name="new_diagnosa_name_input",
                        placeholder="Tambah Diagnosa Baru",
                        class_name="mt-2 w-full p-2 border border-gray-300 rounded-md shadow-sm",
                    ),
                    rx.el.button(
                        "Tambah Diagnosa",
                        type="submit",
                        class_name="mt-2 px-3 py-1.5 text-sm bg-blue-500 text-white rounded-md hover:bg-blue-600",
                    ),
                    on_submit=DataState.handle_add_new_diagnosa_mcu_submit,
                    reset_on_submit=True,
                    class_name="flex gap-2 items-center",
                ),
                class_name="w-full px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Status Kesehatan",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        StatusKesehatan.__args__,
                        lambda status: rx.el.option(
                            status, value=status
                        ),
                    ),
                    name="status_kesehatan",
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm bg-white",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Status Follow Up",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        StatusFollowUpMCU.__args__,
                        lambda status: rx.el.option(
                            status, value=status
                        ),
                    ),
                    name="status_follow_up",
                    class_name="w-full p-2 border border-gray-300 rounded-md shadow-sm bg-white",
                ),
                class_name="w-full md:w-1/2 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Upload Bukti (PDF, Gambar)",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    type="file",
                    name="file_bukti",
                    class_name="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-teal-50 file:text-teal-700 hover:file:bg-teal-100",
                ),
                class_name="w-full px-2 mb-4",
            ),
            class_name="flex flex-wrap -mx-2",
        ),
        rx.el.button(
            "Simpan Data MCU",
            type="submit",
            class_name="px-6 py-2 bg-teal-500 text-white font-semibold rounded-md shadow-md hover:bg-teal-600 transition-colors",
        ),
        on_submit=DataState.add_mcu_result,
        reset_on_submit=True,
        class_name="p-6 bg-white rounded-lg shadow-md mb-8",
    )


def mcu_table() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Rekapan Hasil MCU",
            class_name="text-xl font-semibold text-gray-700 mb-4",
        ),
        rx.el.button(
            "Ekspor ke Excel",
            on_click=DataState.export_mcu_data,
            class_name="mb-4 px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.foreach(
                            [
                                "NIK",
                                "Nama",
                                "Perusahaan",
                                "Tgl MCU",
                                "Status Kesehatan",
                                "Follow Up",
                                "Aksi",
                            ],
                            lambda header: rx.el.th(
                                header,
                                class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600 bg-gray-100 border-b",
                            ),
                        )
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        DataState.mcu_results,
                        lambda mcu_item: rx.el.tr(
                            rx.el.td(
                                mcu_item["nik"],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                mcu_item["nama"],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                mcu_item["perusahaan"],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                mcu_item["tanggal_mcu"],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                mcu_item[
                                    "status_kesehatan"
                                ],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                mcu_item[
                                    "status_follow_up"
                                ],
                                class_name="px-4 py-2 border-b text-sm text-gray-700",
                            ),
                            rx.el.td(
                                rx.el.button(
                                    rx.icon(tag="eye"),
                                    class_name="text-blue-500 hover:text-blue-700 mr-2",
                                ),
                                rx.el.button(
                                    rx.icon(tag="copy"),
                                    class_name="text-yellow-500 hover:text-yellow-700",
                                ),
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                        ),
                    ),
                    rx.cond(
                        DataState.mcu_results.length() == 0,
                        rx.el.tr(
                            rx.el.td(
                                "Tidak ada data MCU.",
                                col_span=7,
                                class_name="text-center py-4 text-gray-500",
                            )
                        ),
                    ),
                ),
                class_name="min-w-full bg-white shadow rounded-lg",
            ),
            class_name="overflow-x-auto",
        ),
    )


def mcu_recap_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                rx.el.h1(
                    "Manajemen Rekapan Hasil MCU",
                    class_name="text-2xl font-bold text-gray-800 mb-6",
                ),
                mcu_form(),
                mcu_table(),
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
                "mcu_recap"
            ),
        ],
        class_name="flex min-h-screen bg-gray-100",
    )