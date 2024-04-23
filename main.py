import tkinter as tk
from tkinter import ttk

class TableGUI(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Tabel dengan Input")
        self.geometry("500x500")

        #Membuat objek gaya dan mengatur tampilan tabel
        style = ttk.Style()
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25)

        self.tree = ttk.Treeview(self, columns=('Nama', 'Usia', 'Kota'), show='headings', style="Treeview")
        self.tree.heading('Nama', text='Nama')
        self.tree.heading('Usia', text='Usia')
        self.tree.heading('Kota', text='Kota')
        self.tree.pack(expand=True, fill='both')

        self.label_nama = tk.Label(self, text='Nama:', bg="#D3D3D3")
        self.label_nama.pack()
        self.entry_nama = tk.Entry(self)
        self.entry_nama.pack()

        self.label_usia = tk.Label(self, text='Usia:', bg="#D3D3D3")
        self.label_usia.pack()
        self.entry_usia = tk.Entry(self)
        self.entry_usia.pack()

        self.label_kota = tk.Label(self, text='Kota:', bg="#D3D3D3")
        self.label_kota.pack()
        self.entry_kota = tk.Entry(self)
        self.entry_kota.pack()

        self.btn_add = tk.Button(self, text='Tambah', command=self.add_row)
        self.btn_add.pack(side='left', pady=5)

        self.btn_edit = tk.Button(self, text='Edit', command=self.edit_row())
        self.btn_edit.pack(side='left', pady=5)

        self.btn_delete = tk.Button(self, text='Delete', command=self.delete_row())
        self.btn_delete.pack(side='left', pady=5)

    def add_row(self):
        nama = self.entry_nama.get()
        usia = self.entry_usia.get()
        kota = self.entry_kota.get()

        self.tree.insert('', 'end', values=(nama, usia, kota))

        self.entry_nama.delete(0, 'end')
        self.entry_usia.delete(0, 'end')
        self.entry_kota.delete(0, 'end')

    def edit_row(self):
        # Mendapatkan baris yang dipilih
        selected_item = self.tree.selection()
        if selected_item:
            # Mendapatkan nilai kolom dari baris yang dipilih
            nama = self.entry_nama.get()
            usia = self.entry_usia.get()
            kota = self.entry_kota.get()

            # Memperbarui nilai kolom dengan nilai baru
            self.tree.item(selected_item, values=(nama, usia, kota))

    def delete_row(self):
        # Mendapatkan baris yang dipilih
        selected_item = self.tree.selection()
        if selected_item:
            # Menghapus baris yang dipilih
            self.tree.delete(selected_item)

if __name__ == "__main__":
    app = TableGUI()
    app.mainloop()