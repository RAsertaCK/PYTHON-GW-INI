import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import json
import os

class AplikasiCatatan:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Harian")
        self.root.geometry("900x650")

        self.data_file = "catatan.json"

        self.catatan = self.load_catatan()

        self.buat_menu()

        self.buat_widget()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def load_catatan(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memuat catatan: {str(e)}")
                return []
        return []
    
    def save_catatan(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.catatan, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan catatan: {str(e)}")
    
    def on_closing(self):
        self.save_catatan()
        self.root.quit()
    
    def buat_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Keluar", command=self.on_closing)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Tentang", command=self.tampilkan_tentang)
        menubar.add_cascade(label="Bantuan", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def buat_widget(self):
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10, padx=10, fill="x")

        tk.Label(frame_input, text="Judul:").grid(row=0, column=0, sticky="w")
        self.entry_judul = tk.Entry(frame_input, width=50)
        self.entry_judul.grid(row=0, column=1, padx=5)

        frame_tombol = tk.Frame(frame_input)
        frame_tombol.grid(row=0, column=2, padx=10)

        self.btn_tambah = tk.Button(frame_tombol, text="Tambah Catatan", command=self.tambah_catatan)
        self.btn_tambah.pack(side="left", padx=5)

        self.btn_edit = tk.Button(frame_tombol, text="Edit Catatan", command=self.edit_catatan)
        self.btn_edit.pack(side="left", padx=5)

        self.btn_hapus = tk.Button(frame_tombol, text="Hapus Catatan", command=self.hapus_catatan)
        self.btn_hapus.pack(side="left", padx=5)

        frame_isi = tk.Frame(self.root)
        frame_isi.pack(pady=5, padx=10, fill="x")
        
        tk.Label(frame_isi, text="Isi Catatan:").pack(anchor="w")
        self.text_isi = scrolledtext.ScrolledText(frame_isi, width=40, height=10)
        self.text_isi.pack(fill="x", pady=5)

        frame_tampilan = tk.Frame(self.root)
        frame_tampilan.pack(pady=10, padx=10, fill="both", expand=True)

        frame_daftar = tk.Frame(frame_tampilan)
        frame_daftar.pack(side="left", fill="y", padx=(0, 10))
        
        tk.Label(frame_daftar, text="Daftar Catatan").pack(anchor="w")
        self.scrollbar = tk.Scrollbar(frame_daftar, orient="vertical")
        self.listbox_catatan = tk.Listbox(frame_daftar, width=35, height=20, 
                                         yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_catatan.yview)
        
        self.listbox_catatan.pack(side="left", fill="y")
        self.scrollbar.pack(side="right", fill="y")

        self.listbox_catatan.bind('<<ListboxSelect>>', self.tampilkan_catatan)

        self.update_listbox()

        frame_tampil_isi = tk.Frame(frame_tampilan)
        frame_tampil_isi.pack(side="right", fill="both", expand=True)
        
        tk.Label(frame_tampil_isi, text="Isi Catatan Terpilih").pack(anchor="w")
        self.text_tampil_isi = scrolledtext.ScrolledText(frame_tampil_isi, width=50, height=20, state="disabled")
        self.text_tampil_isi.pack(fill="both", expand=True)
    
    def update_listbox(self):
        self.listbox_catatan.delete(0, tk.END)
        for catatan in self.catatan:
            self.listbox_catatan.insert(tk.END, f"{catatan['judul']} ({catatan['waktu']})")
    
    def tambah_catatan(self):
        judul = self.entry_judul.get().strip()
        isi = self.text_isi.get("1.0", tk.END).strip()

        if not judul or not isi:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong!")
            return

        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")

        self.catatan.append({
            'judul': judul,
            'isi': isi,
            'waktu': waktu,
            'waktu_edit': waktu 
        })
        
        self.update_listbox()
        
        self.entry_judul.delete(0, tk.END)
        self.text_isi.delete("1.0", tk.END)
        
        messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan!")
    
    def edit_catatan(self):
        selection = self.listbox_catatan.curselection()
        
        if not selection:
            messagebox.showerror("Error", "Tidak ada catatan yang dipilih untuk diedit!")
            return
        
        index = selection[0]

        catatan = self.catatan[index]

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Catatan")
        edit_window.geometry("600x400")

        frame_edit = tk.Frame(edit_window)
        frame_edit.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(frame_edit, text="Judul:").pack(anchor="w")
        entry_judul_edit = tk.Entry(frame_edit, width=50)
        entry_judul_edit.pack(fill="x", pady=5)
        entry_judul_edit.insert(0, catatan['judul'])

        tk.Label(frame_edit, text="Isi Catatan:").pack(anchor="w")
        text_isi_edit = scrolledtext.ScrolledText(frame_edit, width=50, height=15)
        text_isi_edit.pack(fill="both", expand=True)
        text_isi_edit.insert("1.0", catatan['isi'])

        def simpan_edit():
            judul_baru = entry_judul_edit.get().strip()
            isi_baru = text_isi_edit.get("1.0", tk.END).strip()
            
            if not judul_baru or not isi_baru:
                messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong!")
                return

            self.catatan[index]['judul'] = judul_baru
            self.catatan[index]['isi'] = isi_baru
            self.catatan[index]['waktu_edit'] = datetime.now().strftime("%d/%m/%Y %H:%M")

            self.update_listbox()

            if self.listbox_catatan.curselection() == selection:
                self.tampilkan_catatan(None)
            
            edit_window.destroy()
            messagebox.showinfo("Sukses", "Catatan berhasil diperbarui!")
        
        btn_simpan = tk.Button(frame_edit, text="Simpan Perubahan", command=simpan_edit)
        btn_simpan.pack(pady=10)
    
    def tampilkan_catatan(self, event):
        selection = self.listbox_catatan.curselection()
        
        if selection:
            index = selection[0]

            self.text_tampil_isi.config(state="normal")
            self.text_tampil_isi.delete("1.0", tk.END)

            catatan = self.catatan[index]
            isi = f"Judul: {catatan['judul']}\n"
            isi += f"Dibuat: {catatan['waktu']}\n"
            isi += f"Terakhir diubah: {catatan['waktu_edit']}\n\n"
            isi += catatan['isi']
            
            self.text_tampil_isi.insert("1.0", isi)

            self.text_tampil_isi.config(state="disabled")
    
    def hapus_catatan(self):
        selection = self.listbox_catatan.curselection()
        
        if not selection:
            messagebox.showerror("Error", "Tidak ada catatan yang dipilih!")
            return
        
        index = selection[0]
        
        judul = self.catatan[index]['judul']
        if messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus catatan '{judul}'?"):
            self.listbox_catatan.delete(index)
            del self.catatan[index]
            
            self.text_tampil_isi.config(state="normal")
            self.text_tampil_isi.delete("1.0", tk.END)
            self.text_tampil_isi.config(state="disabled")
            
            messagebox.showinfo("Sukses", "Catatan berhasil dihapus!")
    
    def tampilkan_tentang(self):
        about_text = "Aplikasi Catatan Harian\nDibuat Oleh      : Rafael Abimanyu Ratmoko\nNIM                  : 123140134\n\n"
        about_text += "\n© 2025 Aplikasi Catatan Harian (Dibantu AI sedikit untuk tambahan fitur)"
        messagebox.showinfo("Tentang", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiCatatan(root)
    root.mainloop()