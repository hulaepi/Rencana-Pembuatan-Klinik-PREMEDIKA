import reflex as rx
from app.states.auth_state import AuthState
from app.states.sidebar_state import SidebarState
from app.states.data_state import DataState
from app.components.sidebar import sidebar
from app.components.navbar import navbar


def first_aid_inspection_form() -> rx.Component:
    return rx.el.form(
        rx.el.h2(
            "Tambah Inspeksi Alat P3K",
            class_name="text-xl font-semibold text-gray-700 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Tanggal Inspeksi",
                    class_name="block text-sm font-medium",
                ),
                rx.el.input(
                    name="tanggal_inspeksi",
                    type="date",
                    required=True,
                    class_name="w-full p-2 border rounded",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Lokasi P3K",
                    class_name="block text-sm font-medium",
                ),
                rx.el.input(
                    name="lokasi_p3k",
                    placeholder="Contoh: Office Lt.1",
                    required=True,
                    class_name="w-full p-2 border rounded",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Inspektor",
                    class_name="block text-sm font-medium",
                ),
                rx.el.select(
                    rx.el.option(
                        "Pilih Inspektor", value=""
                    ),
                    rx.foreach(
                        DataState.pemeriksa_list,
                        lambda p: rx.el.option(p, value=p),
                    ),
                    name="inspektor",
                    required=True,
                    class_name="w-full p-2 border rounded bg-white",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            class_name="flex flex-wrap -mx-2",
        ),
        rx.el.div(
            rx.el.h3(
                "Item Checklist P3K",
                class_name="text-md font-semibold text-gray-700 mb-2",
            ),
            rx.el.form(
                rx.el.input(
                    name="current_p3k_item_name_input",
                    placeholder="Nama Item (cth: Kasa Steril)",
                    class_name="flex-1 p-2 border rounded-l",
                ),
                rx.el.button(
                    "Tambah Item",
                    type="submit",
                    class_name="px-3 py-2 bg-blue-500 text-white rounded-r hover:bg-blue-600",
                ),
                on_submit=DataState.handle_add_p3k_item_submit,
                reset_on_submit=True,
                class_name="flex mb-3",
            ),
            rx.foreach(
                DataState.p3k_inspection_items,
                lambda item, index: rx.el.div(
                    rx.el.span(
                        item["item_name"],
                        class_name="flex-1",
                    ),
                    rx.el.label(
                        rx.el.input(
                            type="checkbox",
                            checked=item[
                                "kondisi_checklist"
                            ],
                            on_change=lambda checked: DataState.update_p3k_item_in_form(
                                index,
                                "kondisi_checklist",
                                checked,
                            ),
                            class_name="form-checkbox h-5 w-5 text-teal-600 mr-2",
                        ),
                        "OK",
                        class_name="mr-4",
                    ),
                    rx.el.input(
                        placeholder="Catatan item",
                        default_value=item["catatan"],
                        on_change=lambda val: DataState.update_p3k_item_in_form(
                            index, "catatan", val
                        ),
                        class_name="flex-1 p-1 border rounded text-sm",
                    ),
                    rx.el.button(
                        rx.icon(tag="trash-2", size=16),
                        type="button",
                        on_click=lambda: DataState.remove_p3k_item_from_form(
                            index
                        ),
                        class_name="ml-2 text-red-500 hover:text-red-700",
                    ),
                    class_name="flex items-center justify-between p-2 border-b mb-1",
                ),
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Catatan Umum Inspeksi",
                class_name="block text-sm font-medium",
            ),
            rx.el.textarea(
                name="catatan_umum",
                rows=3,
                class_name="w-full p-2 border rounded",
            ),
            class_name="w-full px-2 mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Upload Bukti Umum (Foto, PDF)",
                class_name="block text-sm font-medium",
            ),
            rx.el.input(
                type="file",
                name="file_bukti_umum",
                class_name="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-teal-50 file:text-teal-700 hover:file:bg-teal-100",
            ),
            class_name="w-full px-2 mb-4",
        ),
        rx.el.button(
            "Simpan Inspeksi P3K",
            type="submit",
            class_name="px-6 py-2 bg-teal-500 text-white font-semibold rounded-md shadow-md hover:bg-teal-600",
        ),
        on_submit=DataState.add_first_aid_inspection,
        reset_on_submit=True,
        class_name="p-6 bg-white rounded-lg shadow-md mb-8",
    )


def first_aid_table() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Rekapan Inspeksi Alat P3K",
            class_name="text-xl font-semibold text-gray-700 mb-4",
        ),
        rx.el.button(
            "Ekspor ke Excel",
            on_click=DataState.export_first_aid_inspections,
            class_name="mb-4 px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.foreach(
                            [
                                "Tgl Inspeksi",
                                "Lokasi",
                                "Inspektor",
                                "Jml Item",
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
                        DataState.first_aid_inspections,
                        lambda insp: rx.el.tr(
                            rx.el.td(
                                insp["tanggal_inspeksi"],
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                insp["lokasi_p3k"],
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                insp["inspektor"],
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                insp["items"].length(),
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                rx.el.button(
                                    rx.icon(tag="eye"),
                                    class_name="text-blue-500",
                                ),
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                        ),
                    ),
                    rx.cond(
                        DataState.first_aid_inspections.length()
                        == 0,
                        rx.el.tr(
                            rx.el.td(
                                "Tidak ada data inspeksi P3K.",
                                col_span=5,
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


def first_aid_inspection_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                rx.el.h1(
                    "Manajemen Inspeksi Alat P3K",
                    class_name="text-2xl font-bold text-gray-800 mb-6",
                ),
                first_aid_inspection_form(),
                first_aid_table(),
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
                "first_aid_inspection"
            ),
        ],
        class_name="flex min-h-screen bg-gray-100",
    )