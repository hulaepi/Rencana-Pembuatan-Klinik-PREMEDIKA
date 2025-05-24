import reflex as rx
from typing import List, Dict
from app.utils.data_types import (
    MCUResult,
    FollowUpResult,
    ClinicVisit,
    Diagnosa,
    ObatDiberikan,
    InspeksiAlatP3KRecord,
    InspeksiAmbulansRecord,
    InspeksiItem,
    StatusKesehatan,
    StatusFollowUpMCU,
    YN,
)
import datetime
import pandas as pd
import io


class DataState(rx.State):
    all_diagnosa: List[Diagnosa] = [
        {"id": 1, "nama": "Hipertensi"},
        {"id": 2, "nama": "Diabetes Mellitus"},
        {"id": 3, "nama": "Common Cold"},
    ]
    next_diagnosa_id: int = 4
    companies: List[str] = [
        "PT. Sejahtera Abadi",
        "CV. Maju Jaya",
    ]
    departments: List[str] = [
        "Produksi",
        "HRD",
        "Marketing",
        "IT",
    ]
    pemeriksa_list: List[str] = [
        "Dr. Budi Santoso",
        "Ns. Siti Aminah",
    ]
    mcu_results: List[MCUResult] = []
    follow_up_results: List[FollowUpResult] = []
    clinic_visits: List[ClinicVisit] = []
    first_aid_inspections: List[InspeksiAlatP3KRecord] = []
    ambulance_inspections: List[InspeksiAmbulansRecord] = []
    new_mcu_diagnosa_ids: List[int] = []
    new_follow_up_diagnosa_ids: List[int] = []
    new_clinic_visit_diagnosa_ids: List[int] = []
    new_clinic_visit_obat: List[ObatDiberikan] = []
    p3k_inspection_items: List[InspeksiItem] = []
    ambulance_inspection_items: List[InspeksiItem] = []

    @rx.event
    def add_new_diagnosa(self, nama_diagnosa: str):
        if nama_diagnosa and (
            not any(
                (
                    d["nama"].lower()
                    == nama_diagnosa.lower()
                    for d in self.all_diagnosa
                )
            )
        ):
            self.all_diagnosa.append(
                {
                    "id": self.next_diagnosa_id,
                    "nama": nama_diagnosa,
                }
            )
            self.next_diagnosa_id += 1
            yield rx.toast(
                f"Diagnosa '{nama_diagnosa}' ditambahkan."
            )
        else:
            yield rx.toast(
                "Nama diagnosa tidak boleh kosong atau sudah ada."
            )

    @rx.event
    def handle_add_new_diagnosa_mcu_submit(
        self, form_data: dict
    ):
        nama_diagnosa = form_data.get(
            "new_diagnosa_name_input", ""
        )
        if nama_diagnosa:
            yield DataState.add_new_diagnosa(nama_diagnosa)

    @rx.var
    def diagnosa_options(
        self,
    ) -> List[Dict[str, str | int]]:
        return [
            {"label": d["nama"], "value": d["id"]}
            for d in self.all_diagnosa
        ]

    def _get_diagnosa_names_by_ids(
        self, ids: List[int] | None
    ) -> List[str]:
        if ids is None:
            return []
        return [
            d["nama"]
            for d in self.all_diagnosa
            if d["id"] in ids
        ]

    @rx.event
    def add_mcu_result(self, form_data: dict):
        if not all(
            (
                form_data.get(key)
                for key in ["nik", "nama", "tanggal_mcu"]
            )
        ):
            yield rx.toast(
                "NIK, Nama, dan Tanggal MCU wajib diisi."
            )
            return
        new_id = (
            form_data["nik"]
            + "_"
            + form_data["tanggal_mcu"]
        )
        diagnosa_ids_str = form_data.get("diagnosa_ids", [])
        if not isinstance(diagnosa_ids_str, list):
            diagnosa_ids_str = (
                [diagnosa_ids_str]
                if diagnosa_ids_str
                else []
            )
        try:
            processed_diagnosa_ids = [
                int(id_str)
                for id_str in diagnosa_ids_str
                if id_str
            ]
        except ValueError:
            yield rx.toast(
                "Format ID Diagnosa tidak valid."
            )
            return
        mcu = MCUResult(
            id=new_id,
            nik=form_data["nik"],
            nama=form_data["nama"],
            jabatan=form_data.get("jabatan", ""),
            departemen=form_data.get("departemen", ""),
            perusahaan=form_data.get("perusahaan", ""),
            tanggal_mcu=form_data["tanggal_mcu"],
            tanggal_review_mcu=form_data.get(
                "tanggal_review_mcu", ""
            ),
            temuan=form_data.get("temuan", ""),
            diagnosa_ids=processed_diagnosa_ids,
            status_kesehatan=form_data.get(
                "status_kesehatan", "Fit"
            ),
            status_follow_up=form_data.get(
                "status_follow_up", "Tidak Follow Up"
            ),
            file_bukti_path=None,
        )
        self.mcu_results.append(mcu)
        self.new_mcu_diagnosa_ids = []
        yield rx.toast("Data MCU berhasil ditambahkan.")

    @rx.event
    def add_follow_up_result(self, form_data: dict):
        if not all(
            (
                form_data.get(key)
                for key in [
                    "nik",
                    "nama",
                    "tanggal_follow_up",
                    "mcu_reference_nik",
                    "mcu_reference_tanggal",
                ]
            )
        ):
            yield rx.toast(
                "NIK, Nama, Tanggal Follow Up, dan Referensi MCU wajib diisi."
            )
            return
        diagnosa_ids_str = form_data.get("diagnosa_ids", [])
        if not isinstance(diagnosa_ids_str, list):
            diagnosa_ids_str = (
                [diagnosa_ids_str]
                if diagnosa_ids_str
                else []
            )
        try:
            processed_diagnosa_ids = [
                int(id_str)
                for id_str in diagnosa_ids_str
                if id_str
            ]
        except ValueError:
            yield rx.toast(
                "Format ID Diagnosa tidak valid."
            )
            return
        follow_up = FollowUpResult(
            id=form_data["nik"]
            + "_"
            + form_data["tanggal_follow_up"],
            mcu_nik=form_data["mcu_reference_nik"],
            mcu_tanggal=form_data["mcu_reference_tanggal"],
            nik=form_data["nik"],
            nama=form_data["nama"],
            jabatan=form_data.get("jabatan", ""),
            departemen=form_data.get("departemen", ""),
            perusahaan=form_data.get("perusahaan", ""),
            tanggal_follow_up=form_data[
                "tanggal_follow_up"
            ],
            diagnosa_ids=processed_diagnosa_ids,
            status_kesehatan=form_data.get(
                "status_kesehatan", "Fit"
            ),
            file_bukti_path=None,
        )
        self.follow_up_results.append(follow_up)
        mcu_id_to_update = f"{form_data['mcu_reference_nik']}_{form_data['mcu_reference_tanggal']}"
        for i, mcu in enumerate(self.mcu_results):
            if mcu["id"] == mcu_id_to_update:
                mcu_copy = self.mcu_results[i].copy()
                mcu_copy["status_follow_up"] = (
                    "Sudah Follow Up"
                )
                self.mcu_results[i] = mcu_copy
                break
        self.new_follow_up_diagnosa_ids = []
        yield rx.toast(
            "Data Follow Up berhasil ditambahkan dan MCU terupdate."
        )

    @rx.event
    def handle_add_obat_clinic_submit(
        self, form_data: dict
    ):
        obat_nama = form_data.get(
            "current_obat_nama_input", ""
        )
        obat_jumlah_str = form_data.get(
            "current_obat_jumlah_input", "1"
        )
        try:
            obat_jumlah = int(obat_jumlah_str)
            if obat_jumlah <= 0:
                obat_jumlah = 1
        except ValueError:
            obat_jumlah = 1
        if obat_nama:
            self.new_clinic_visit_obat.append(
                {
                    "nama_obat": obat_nama,
                    "jumlah": obat_jumlah,
                }
            )
        else:
            yield rx.toast(
                "Nama obat dan jumlah harus valid."
            )

    @rx.event
    def remove_obat_from_clinic_visit_form(
        self, index: int
    ):
        if 0 <= index < len(self.new_clinic_visit_obat):
            del self.new_clinic_visit_obat[index]

    @rx.event
    def add_clinic_visit(self, form_data: dict):
        if not all(
            (
                form_data.get(key)
                for key in [
                    "nik",
                    "nama",
                    "tanggal_kunjungan",
                    "keluhan_soap",
                ]
            )
        ):
            yield rx.toast(
                "NIK, Nama, Tanggal Kunjungan, dan Keluhan (SOAP) wajib diisi."
            )
            return
        diagnosa_ids_str = form_data.get("diagnosa_ids", [])
        if not isinstance(diagnosa_ids_str, list):
            diagnosa_ids_str = (
                [diagnosa_ids_str]
                if diagnosa_ids_str
                else []
            )
        try:
            processed_diagnosa_ids = [
                int(id_str)
                for id_str in diagnosa_ids_str
                if id_str
            ]
        except ValueError:
            yield rx.toast(
                "Format ID Diagnosa tidak valid."
            )
            return
        visit = ClinicVisit(
            id=form_data["nik"]
            + "_"
            + form_data["tanggal_kunjungan"]
            + "_"
            + str(datetime.datetime.now().timestamp()),
            nik=form_data["nik"],
            nama=form_data["nama"],
            jabatan=form_data.get("jabatan", ""),
            departemen=form_data.get("departemen", ""),
            perusahaan=form_data.get("perusahaan", ""),
            shift=form_data.get("shift", ""),
            mess=form_data.get("mess", ""),
            lokasi_periksa=form_data.get(
                "lokasi_periksa", ""
            ),
            keluhan_soap=form_data["keluhan_soap"],
            diagnosa_ids=processed_diagnosa_ids,
            obat_diberikan=list(self.new_clinic_visit_obat),
            surat_sakit=form_data.get(
                "surat_sakit", "Tidak"
            ),
            keterangan=form_data.get("keterangan", ""),
            pemeriksa=form_data.get("pemeriksa", ""),
            tanggal_kunjungan=form_data[
                "tanggal_kunjungan"
            ],
            file_bukti_path=None,
        )
        self.clinic_visits.append(visit)
        self.new_clinic_visit_diagnosa_ids = []
        self.new_clinic_visit_obat = []
        yield rx.toast(
            "Data Kunjungan Berobat berhasil ditambahkan."
        )

    @rx.event
    def handle_add_p3k_item_submit(self, form_data: dict):
        item_name = form_data.get(
            "current_p3k_item_name_input", ""
        )
        if item_name:
            self.p3k_inspection_items.append(
                {
                    "item_name": item_name,
                    "kondisi_checklist": True,
                    "catatan": "",
                }
            )
        else:
            yield rx.toast(
                "Nama item P3K tidak boleh kosong."
            )

    @rx.event
    def update_p3k_item_in_form(
        self, index: int, field: str, value: str | bool
    ):
        if 0 <= index < len(self.p3k_inspection_items):
            item_copy = self.p3k_inspection_items[
                index
            ].copy()
            if field == "kondisi_checklist":
                item_copy["kondisi_checklist"] = bool(value)
            elif field == "catatan":
                item_copy["catatan"] = str(value)
            self.p3k_inspection_items[index] = item_copy

    @rx.event
    def remove_p3k_item_from_form(self, index: int):
        if 0 <= index < len(self.p3k_inspection_items):
            del self.p3k_inspection_items[index]

    @rx.event
    def add_first_aid_inspection(self, form_data: dict):
        if not all(
            (
                form_data.get(key)
                for key in [
                    "tanggal_inspeksi",
                    "lokasi_p3k",
                    "inspektor",
                ]
            )
        ):
            yield rx.toast(
                "Tanggal, Lokasi P3K, dan Inspektor wajib diisi."
            )
            return
        inspection = InspeksiAlatP3KRecord(
            id=form_data["lokasi_p3k"]
            + "_"
            + form_data["tanggal_inspeksi"],
            tanggal_inspeksi=form_data["tanggal_inspeksi"],
            lokasi_p3k=form_data["lokasi_p3k"],
            inspektor=form_data["inspektor"],
            items=list(self.p3k_inspection_items),
            catatan_umum=form_data.get("catatan_umum", ""),
            file_bukti_umum_path=None,
        )
        self.first_aid_inspections.append(inspection)
        self.p3k_inspection_items = []
        yield rx.toast(
            "Data Inspeksi Alat P3K berhasil ditambahkan."
        )

    @rx.event
    def handle_add_ambulance_item_submit(
        self, form_data: dict
    ):
        item_name = form_data.get(
            "current_ambulance_item_name_input", ""
        )
        if item_name:
            self.ambulance_inspection_items.append(
                {
                    "item_name": item_name,
                    "kondisi_checklist": True,
                    "catatan": "",
                }
            )
        else:
            yield rx.toast(
                "Nama item inspeksi ambulans tidak boleh kosong."
            )

    @rx.event
    def update_ambulance_item_in_form(
        self, index: int, field: str, value: str | bool
    ):
        if (
            0
            <= index
            < len(self.ambulance_inspection_items)
        ):
            item_copy = self.ambulance_inspection_items[
                index
            ].copy()
            if field == "kondisi_checklist":
                item_copy["kondisi_checklist"] = bool(value)
            elif field == "catatan":
                item_copy["catatan"] = str(value)
            self.ambulance_inspection_items[index] = (
                item_copy
            )

    @rx.event
    def remove_ambulance_item_from_form(self, index: int):
        if (
            0
            <= index
            < len(self.ambulance_inspection_items)
        ):
            del self.ambulance_inspection_items[index]

    @rx.event
    def add_ambulance_inspection(self, form_data: dict):
        if not all(
            (
                form_data.get(key)
                for key in [
                    "tanggal_inspeksi",
                    "nomor_polisi_ambulans",
                    "inspektor",
                ]
            )
        ):
            yield rx.toast(
                "Tanggal, No. Polisi Ambulans, dan Inspektor wajib diisi."
            )
            return
        inspection = InspeksiAmbulansRecord(
            id=form_data["nomor_polisi_ambulans"]
            + "_"
            + form_data["tanggal_inspeksi"],
            tanggal_inspeksi=form_data["tanggal_inspeksi"],
            nomor_polisi_ambulans=form_data[
                "nomor_polisi_ambulans"
            ],
            inspektor=form_data["inspektor"],
            items=list(self.ambulance_inspection_items),
            catatan_umum=form_data.get("catatan_umum", ""),
            file_bukti_umum_path=None,
        )
        self.ambulance_inspections.append(inspection)
        self.ambulance_inspection_items = []
        yield rx.toast(
            "Data Inspeksi Ambulans berhasil ditambahkan."
        )

    def _export_to_excel_helper(
        self, data_list: List[Dict], filename: str
    ):
        if not data_list:
            yield rx.toast("Tidak ada data untuk diekspor.")
            return
        df_data = []
        for item_dict in data_list:
            processed_item = {}
            for key, value in item_dict.items():
                if isinstance(value, list):
                    if all(
                        (isinstance(i, dict) for i in value)
                    ):
                        processed_item[key] = "; ".join(
                            [
                                str(sub_item)
                                for sub_item in value
                            ]
                        )
                    else:
                        processed_item[key] = ", ".join(
                            map(str, value)
                        )
                elif isinstance(value, dict):
                    processed_item[key] = str(value)
                else:
                    processed_item[key] = value
            df_data.append(processed_item)
        df = pd.DataFrame(df_data)
        output = io.BytesIO()
        with pd.ExcelWriter(
            output, engine="openpyxl"
        ) as writer:
            df.to_excel(
                writer, index=False, sheet_name="Sheet1"
            )
        output.seek(0)
        yield rx.download(
            data=output.getvalue(), filename=filename
        )
        yield rx.toast(f"Memulai unduhan {filename}...")

    @rx.event
    def export_mcu_data(self):
        export_data = []
        for mcu_item_typed_dict in self.mcu_results:
            mcu_item = dict(mcu_item_typed_dict)
            mcu_item["diagnosa_str"] = ", ".join(
                self._get_diagnosa_names_by_ids(
                    mcu_item.get("diagnosa_ids")
                )
            )
            if "diagnosa_ids" in mcu_item:
                del mcu_item["diagnosa_ids"]
            export_data.append(mcu_item)
        yield from self._export_to_excel_helper(
            export_data, "rekapan_mcu.xlsx"
        )

    @rx.event
    def export_follow_up_data(self):
        export_data = []
        for fu_item_typed_dict in self.follow_up_results:
            fu_item = dict(fu_item_typed_dict)
            fu_item["diagnosa_str"] = ", ".join(
                self._get_diagnosa_names_by_ids(
                    fu_item.get("diagnosa_ids")
                )
            )
            if "diagnosa_ids" in fu_item:
                del fu_item["diagnosa_ids"]
            export_data.append(fu_item)
        yield from self._export_to_excel_helper(
            export_data, "rekapan_follow_up.xlsx"
        )

    @rx.event
    def export_clinic_visit_data(self):
        export_data = []
        for visit_item_typed_dict in self.clinic_visits:
            visit_item = dict(visit_item_typed_dict)
            visit_item["diagnosa_str"] = ", ".join(
                self._get_diagnosa_names_by_ids(
                    visit_item.get("diagnosa_ids")
                )
            )
            if "diagnosa_ids" in visit_item:
                del visit_item["diagnosa_ids"]
            obat_list = visit_item.get("obat_diberikan", [])
            visit_item["obat_diberikan_str"] = "; ".join(
                [
                    f"{o['nama_obat']} ({o['jumlah']})"
                    for o in obat_list
                ]
            )
            if "obat_diberikan" in visit_item:
                del visit_item["obat_diberikan"]
            export_data.append(visit_item)
        yield from self._export_to_excel_helper(
            export_data, "kunjungan_berobat.xlsx"
        )

    @rx.event
    def export_first_aid_inspections(self):
        export_data = []
        for (
            insp_item_typed_dict
        ) in self.first_aid_inspections:
            insp_item = dict(insp_item_typed_dict)
            items_list = insp_item.get("items", [])
            insp_item["items_str"] = "; ".join(
                [
                    f"{i['item_name']} (Kondisi: {('OK' if i['kondisi_checklist'] else 'Not OK')}, Catatan: {i.get('catatan', '')})"
                    for i in items_list
                ]
            )
            if "items" in insp_item:
                del insp_item["items"]
            export_data.append(insp_item)
        yield from self._export_to_excel_helper(
            export_data, "inspeksi_p3k.xlsx"
        )

    @rx.event
    def export_ambulance_inspections(self):
        export_data = []
        for (
            insp_item_typed_dict
        ) in self.ambulance_inspections:
            insp_item = dict(insp_item_typed_dict)
            items_list = insp_item.get("items", [])
            insp_item["items_str"] = "; ".join(
                [
                    f"{i['item_name']} (Kondisi: {('OK' if i['kondisi_checklist'] else 'Not OK')}, Catatan: {i.get('catatan', '')})"
                    for i in items_list
                ]
            )
            if "items" in insp_item:
                del insp_item["items"]
            export_data.append(insp_item)
        yield from self._export_to_excel_helper(
            export_data, "inspeksi_ambulans.xlsx"
        )