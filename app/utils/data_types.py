import reflex as rx
from typing import TypedDict, List, Literal

StatusKesehatan = Literal[
    "Fit", "Fit With Note", "Temporary Unfit", "Unfit"
]
StatusFollowUpMCU = Literal[
    "Sudah Follow Up", "Tidak Follow Up"
]
YN = Literal["Ya", "Tidak"]


class Diagnosa(TypedDict):
    id: int
    nama: str


class MCUResult(TypedDict):
    id: str
    nik: str
    nama: str
    jabatan: str
    departemen: str
    perusahaan: str
    tanggal_mcu: str
    tanggal_review_mcu: str
    temuan: str
    diagnosa_ids: List[int]
    status_kesehatan: StatusKesehatan
    status_follow_up: StatusFollowUpMCU
    file_bukti_path: str | None


class FollowUpResult(TypedDict):
    id: str
    mcu_nik: str
    mcu_tanggal: str
    nik: str
    nama: str
    jabatan: str
    departemen: str
    perusahaan: str
    tanggal_follow_up: str
    diagnosa_ids: List[int]
    status_kesehatan: StatusKesehatan
    file_bukti_path: str | None


class ObatDiberikan(TypedDict):
    nama_obat: str
    jumlah: int


class ClinicVisit(TypedDict):
    id: str
    nik: str
    nama: str
    jabatan: str
    departemen: str
    perusahaan: str
    shift: str
    mess: str
    lokasi_periksa: str
    keluhan_soap: str
    diagnosa_ids: List[int]
    obat_diberikan: List[ObatDiberikan]
    surat_sakit: YN
    keterangan: str | None
    pemeriksa: str
    tanggal_kunjungan: str
    file_bukti_path: str | None


class InspeksiItem(TypedDict):
    item_name: str
    kondisi_checklist: bool
    catatan: str | None


class InspeksiAlatP3KRecord(TypedDict):
    id: str
    tanggal_inspeksi: str
    lokasi_p3k: str
    inspektor: str
    items: List[InspeksiItem]
    catatan_umum: str | None
    file_bukti_umum_path: str | None


class InspeksiAmbulansRecord(TypedDict):
    id: str
    tanggal_inspeksi: str
    nomor_polisi_ambulans: str
    inspektor: str
    items: List[InspeksiItem]
    catatan_umum: str | None
    file_bukti_umum_path: str | None