import tkinter as tk
from tkinter import messagebox

medical_records = {
    "1306": {
        "name": "Ariana Grande",
        "age": 30,
        "clinical summary": [
            {
                "date" : "2021-01-10",
                "visit_summary" : "General checkup, all normal.",
                "diagnose" : "-",
                "prescription" : "Tidak ada",
                "doctor" : "Dr. Hermione Granger, Sp.PD"
            },
            {
                "date" : "2021-11-16",
                "visit_summary" : "Keluhan sakit kepala, Suhu tubuh 37,5 °C",
                "diagnose" : "Demam",
                "prescription" : "Ibuprofen",
                "doctor" : "Dr. Ron Weasley"
            },
            {
                "date" : "2022-04-05",
                "visit_summary" : "Dada terasa sakit, Napas pendek, Demam dan berkeringat di malam hari",
                "diagnose" : "TBC",
                "prescription" : "Rifampicin, Ethambutol",
                "doctor" : "Dr. Blair Waldrof, Sp.P"
            }
        ]
    },
    "0602": {
        "name": "Taylor Swift",
        "age": 25,
        "clinical summary": [
            {
                "date" : "2021-01-02",
                "visit_summary" : "Insomnia, Otot tegang, Jantung berdebar",
                "diagnose" : "Anxiety Disorder",
                "prescription" : "Escitalopram",
                "doctor" : "Dr. Regina George, Sp.KJ"
            },
            {
                "date" : "2021-04-05",
                "visit_summary" : "Diare, Kram perut, Demam",
                "diagnose" : "GERD",
                "prescription" : "Pantoprazole, Metoclopramide",
                "doctor" : "Dr. Hermione Granger, Sp.PD"
            }
        ]
    },
    "2404": {
        "name": "Olivia Rodrigo",
        "age": 28,
        "clinical summary": [
            {
                "date" : "2021-06-13",
                "visit_summary" : "General checkup for smoking cessation",
                "diagnose" : "Smoking cessation",
                "prescription" : "varenicline",
                "doctor" : "Dr. Blair Waldrof, Sp.P"
            },
            {
                "date" : "2021-06-13",
                "visit_summary" : "Kulit kemerahan, mengelupas, dan rasa terbakar",
                "diagnose" : "Sunburn",
                "prescription" : "Petroleum Jelly, Aceraminophen",
                "doctor" : "Dr. Cady Heron, Sp.KK"
            }
        ]
    }
}

jadwal_dokter = {
    "Dr. Hermione Granger, Sp.PD": [
        {"hari": "Senin", "jam": "10:00 - 14:00"},
        {"hari": "Kamis", "jam": "12:00 - 16:00"}
    ],
    "Dr. Ron Weasley": [
        {"hari": "Selasa", "jam": "09:00 - 13:00"},
        {"date": "Jum'at", "jam": "11:00 - 15:00"}
    ],
    "Dr. Blair Waldrof, Sp.P": [
        {"hari": "Rabu", "jam": "10:00 - 14:00"},
        {"hari": "Sabtu", "jam": "08:00 - 12:00"}
    ],
    "Dr. Regina George, Sp.KJ": [
        {"hari": "Senin", "jam": "11:00 - 15:00"},
        {"hari": "Kamis", "jam": "13:00 - 17:00"}
    ],
    "Dr. Cady Heron, Sp.KK": [
        {"hari": "Selasa", "jam": "09:00 - 13:00"},
        {"hari": "Jum'at", "jam": "12:00 - 16:00"}
    ]
}

class JadwalDokter:
    def __init__(self, schedules):
        self.schedules = schedules

    def get_schedule(self, doctor_name):
        if doctor_name in self.schedules:
            schedule_list = self.schedules[doctor_name]
            schedule_text = f"Schedule for {doctor_name}:\n\n"
            for entry in schedule_list:
                hari = entry["hari"]
                jam = entry["jam"]
                schedule_text += f"hari: {hari}, jam: {jam}\n"
            return schedule_text
        else:
            return "Jadwal Dokter Tidak Ditemukan."

def check_medical_history():
    patient_id = entry2.get()
    if patient_id in medical_records:
        record = medical_records[patient_id]
        name = record["name"]
        age = record["age"]
        history_entries = record["clinical summary"]

        history = " "
        for entry in history_entries:
            date = entry["date"]
            summary = entry["visit_summary"]
            diagnose = entry["diagnose"]
            prescription = entry["prescription"]
            doctor = entry["doctor"]
            history += f"Date: {date}\nSummary: {summary}\nDiagnose: {diagnose}\nPrescription: {prescription}\nDoctor: {doctor}\n\n"

        result_text = f"Name: {name}\nAge: {age}\n\nMedical History:\n{history}"
    else:
        result_text = "ID Pasien Tidak Ditemukan, Silakan Masukkan ID yang Sesuai"

    messagebox.showinfo("Medical History", result_text)

def check_doctor_schedule():
    doctor_name = entry3.get()
    schedule = jadwal_dokter.get_schedule(doctor_name)
    messagebox.showinfo("Doctor Schedule", schedule)

root = tk.Tk()
root.title("Medical Records Checker Yulje Hospital")
root.geometry("500x500")
root.configure(bg="#EED7F7")

form_frame = tk.Frame(root, bg="#D1A4E4", padx=20, pady=20, relief=tk.RIDGE, borderwidth=2)
form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

label1 = tk.Label(form_frame, text="Full Name", font=("Roboto", 12), bg="#E4E0E6")
label1.pack(pady=5)

entry1 = tk.Entry(form_frame, text="Full Name", font=("Roboto", 12), bg="#E4E0E6")
entry1.pack(pady=5)

label2 = tk.Label(form_frame, text="Medical Record Number", font=("Roboto", 12), bg="#E4E0E6")
label2.pack(pady=15)

entry2 = tk.Entry(form_frame, text="Medical Record Number", font=("Roboto", 12), bg="#E4E0E6")
entry2.pack(pady=15)

button = tk.Button(form_frame, text="Check Medical History", command=check_medical_history, font=("Roboto", 12), bg="#51375C", fg="#f0f0f0")
button.pack(pady=20)

label3 = tk.Label(form_frame, text="Doctor Name", font=("Roboto", 12), bg="#E4E0E6")
label3.pack(pady=5)

entry3 = tk.Entry(form_frame, text="Doctor Name", font=("Roboto", 12), bg="#E4E0E6")
entry3.pack(pady=5)

schedule_button = tk.Button(form_frame, text="Check Doctor Schedule", command=check_doctor_schedule, font=("Roboto", 12), bg="#51375C", fg="#f0f0f0")
schedule_button.pack(pady=20)

jadwal_dokter = JadwalDokter(jadwal_dokter)

root.mainloop()
