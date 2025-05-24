import reflex as rx
from app.states.auth_state import AuthState
from app.states.sidebar_state import SidebarState
from app.states.data_state import DataState
from app.components.sidebar import sidebar
from app.components.navbar import navbar
from app.utils.data_types import YN


def clinic_visit_form() -> rx.Component:
    return rx.el.form(
        rx.el.h2(
            "Tambah Data Kunjungan Berobat",
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
                    required=True,
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Nama",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="nama",
                    required=True,
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Tanggal Kunjungan",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="tanggal_kunjungan",
                    type="date",
                    required=True,
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Jabatan",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="jabatan",
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
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
                    class_name="w-full p-2 border rounded-md bg-white",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
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
                    class_name="w-full p-2 border rounded-md bg-white",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Shift",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="shift",
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Mess",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="mess",
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Lokasi Periksa",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.input(
                    name="lokasi_periksa",
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Keluhan (SOAP)",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.textarea(
                    name="keluhan_soap",
                    rows=4,
                    required=True,
                    class_name="w-full p-2 border rounded-md",
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
                class_name="w-full px-2 mb-4",
            ),
            rx.el.div(
                rx.el.h3(
                    "Obat yang Diberikan",
                    class_name="text-md font-semibold text-gray-700 mb-2",
                ),
                rx.el.form(
                    rx.el.input(
                        name="current_obat_nama_input",
                        placeholder="Nama Obat",
                        class_name="flex-1 p-2 border rounded-l-md",
                    ),
                    rx.el.input(
                        name="current_obat_jumlah_input",
                        type="number",
                        placeholder="Jumlah",
                        min=1,
                        default_value="1",
                        class_name="w-24 p-2 border-t border-b",
                    ),
                    rx.el.button(
                        "Tambah Obat",
                        type="submit",
                        class_name="px-3 py-2 bg-blue-500 text-white rounded-r-md hover:bg-blue-600",
                    ),
                    on_submit=DataState.handle_add_obat_clinic_submit,
                    reset_on_submit=True,
                    class_name="flex mb-2",
                ),
                rx.el.ul(
                    rx.foreach(
                        DataState.new_clinic_visit_obat,
                        lambda obat, index: rx.el.li(
                            f"{obat['nama_obat']} ({obat['jumlah']})",
                            rx.el.button(
                                rx.icon(tag="x", size=16),
                                type="button",
                                on_click=lambda: DataState.remove_obat_from_clinic_visit_form(
                                    index
                                ),
                                class_name="ml-2 text-red-500 hover:text-red-700",
                            ),
                            class_name="flex justify-between items-center p-1 border-b",
                        ),
                    ),
                    class_name="list-disc pl-5 mb-4",
                ),
                class_name="w-full px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Surat Sakit",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        YN.__args__,
                        lambda opt: rx.el.option(
                            opt, value=opt
                        ),
                    ),
                    name="surat_sakit",
                    class_name="w-full p-2 border rounded-md bg-white",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Pemeriksa",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.select(
                    rx.el.option(
                        "Pilih Pemeriksa", value=""
                    ),
                    rx.foreach(
                        DataState.pemeriksa_list,
                        lambda p: rx.el.option(p, value=p),
                    ),
                    name="pemeriksa",
                    class_name="w-full p-2 border rounded-md bg-white",
                ),
                class_name="w-full md:w-1/3 px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Keterangan (Opsional)",
                    class_name="block text-sm font-medium text-gray-700 mb-1",
                ),
                rx.el.textarea(
                    name="keterangan",
                    rows=2,
                    class_name="w-full p-2 border rounded-md",
                ),
                class_name="w-full px-2 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Upload Bukti",
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
            "Simpan Kunjungan",
            type="submit",
            class_name="px-6 py-2 bg-teal-500 text-white font-semibold rounded-md shadow-md hover:bg-teal-600",
        ),
        on_submit=DataState.add_clinic_visit,
        reset_on_submit=True,
        class_name="p-6 bg-white rounded-lg shadow-md mb-8",
    )


def clinic_visit_table() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Rekapan Kunjungan Berobat",
            class_name="text-xl font-semibold text-gray-700 mb-4",
        ),
        rx.el.button(
            "Ekspor ke Excel",
            on_click=DataState.export_clinic_visit_data,
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
                                "Tgl Kunjungan",
                                "Keluhan",
                                "Pemeriksa",
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
                        DataState.clinic_visits,
                        lambda visit: rx.el.tr(
                            rx.el.td(
                                visit["nik"],
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                visit["nama"],
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                visit["tanggal_kunjungan"],
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                visit[
                                    "keluhan_soap"
                                ].to_string()[0:50]
                                + "...",
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                visit["pemeriksa"],
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                            rx.el.td(
                                rx.el.button(
                                    rx.icon(tag="eye"),
                                    class_name="text-blue-500 mr-2",
                                ),
                                rx.el.button(
                                    rx.icon(tag="copy"),
                                    class_name="text-yellow-500",
                                ),
                                class_name="px-4 py-2 border-b text-sm",
                            ),
                        ),
                    ),
                    rx.cond(
                        DataState.clinic_visits.length()
                        == 0,
                        rx.el.tr(
                            rx.el.td(
                                "Tidak ada data kunjungan.",
                                col_span=6,
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


def clinic_visit_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                rx.el.h1(
                    "Manajemen Kunjungan Berobat",
                    class_name="text-2xl font-bold text-gray-800 mb-6",
                ),
                clinic_visit_form(),
                clinic_visit_table(),
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
                "clinic_visit"
            ),
        ],
        class_name="flex min-h-screen bg-gray-100",
    )