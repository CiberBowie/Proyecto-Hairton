# gui_module.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import sv_ttk

class DarkGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KMZ to AutoCAD Converter")
        self.root.geometry("800x600")
        
        # Configurar tema oscuro
        sv_ttk.set_theme("dark")
        
        self.create_widgets()
        self.setup_layout()
        
    def create_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(expand=True, fill='both')
        
        # Controles de entrada
        self.create_input_controls()
        
        # Consola de salida
        self.output_console = ScrolledText(self.main_frame, height=15, bg='#333333', fg='white')
        self.output_console.tag_config('success', foreground='#00ff00')
        self.output_console.tag_config('error', foreground='#ff0000')
        
        # Barra de progreso
        self.progress = ttk.Progressbar(self.main_frame, mode='determinate')
        
        # Botones
        self.process_btn = ttk.Button(self.main_frame, text="Procesar", command=self.process)
        self.exit_btn = ttk.Button(self.main_frame, text="Salir", command=self.root.destroy)
        
    def create_input_controls(self):
        style = ttk.Style()
        style.configure('Dark.TLabel', foreground='white', background='#333333')
        
        # Frame de controles
        input_frame = ttk.Frame(self.main_frame)
        
        # KMZ File
        ttk.Label(input_frame, text="Archivo KMZ:", style='Dark.TLabel').grid(row=0, column=0, sticky='w')
        self.kmz_entry = ttk.Entry(input_frame, width=50)
        ttk.Button(input_frame, text="Buscar...", command=self.select_kmz).grid(row=0, column=2)
        
        # CSV de referencia
        ttk.Label(input_frame, text="CSV Referencia:", style='Dark.TLabel').grid(row=1, column=0, sticky='w')
        self.csv_entry = ttk.Entry(input_frame, width=50)
        ttk.Button(input_frame, text="Buscar...", command=self.select_csv).grid(row=1, column=2)
        
        # Parámetros
        ttk.Label(input_frame, text="Offset:", style='Dark.TLabel').grid(row=2, column=0, sticky='w')
        self.offset_entry = ttk.Entry(input_frame)
        self.offset_entry.insert(0, "10")
        
        ttk.Label(input_frame, text="Altura texto:", style='Dark.TLabel').grid(row=3, column=0, sticky='w')
        self.text_height_entry = ttk.Entry(input_frame)
        self.text_height_entry.insert(0, "2.5")
        
        # Posicionamiento
        self.kmz_entry.grid(row=0, column=1, padx=5, pady=5)
        self.csv_entry.grid(row=1, column=1, padx=5, pady=5)
        self.offset_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.text_height_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        
        input_frame.pack(fill='x', pady=10)
        
    def setup_layout(self):
        # Organización de elementos
        self.output_console.pack(expand=True, fill='both', pady=10)
        self.progress.pack(fill='x', pady=5)
        self.process_btn.pack(side='right', padx=5, pady=10)
        self.exit_btn.pack(side='right', padx=5, pady=10)
        
    def select_kmz(self):
        file_path = filedialog.askopenfilename(filetypes=[("KMZ files", "*.kmz")])
        if file_path:
            self.kmz_entry.delete(0, tk.END)
            self.kmz_entry.insert(0, file_path)
            
    def select_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.csv_entry.delete(0, tk.END)
            self.csv_entry.insert(0, file_path)
            
    def log_message(self, message, tag=None):
        self.output_console.configure(state='normal')
        self.output_console.insert(tk.END, message + "\n", tag)
        self.output_console.configure(state='disabled')
        self.output_console.see(tk.END)
        self.root.update_idletasks()
        
    def process(self):
        try:
            self.progress['value'] = 0
            params = {
                'kmz_path': self.kmz_entry.get(),
                'reference_csv': self.csv_entry.get(),
                'offset': float(self.offset_entry.get()),
                'text_height': float(self.text_height_entry.get())
            }
            
            self.progress['value'] = 30
            self.process_callback(params, self.update_progress, self.log_message)
            
            self.progress['value'] = 100
            messagebox.showinfo("Éxito", "Proceso completado correctamente")
            
        except Exception as e:
            self.log_message(f"Error: {str(e)}", 'error')
            messagebox.showerror("Error", str(e))
            
    def update_progress(self, value):
        self.progress['value'] = value
        self.root.update_idletasks()
        
    def run(self):
        self.root.mainloop()