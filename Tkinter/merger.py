import PyPDF2
import tkinter as tk
from tkinter import filedialog

class PDFMergerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Merger")

        self.input_files = []

        # Input files section
        self.input_files_label = tk.Label(master, text="Input PDF Files:")
        self.input_files_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_files_listbox = tk.Listbox(master, width=50, height=10)
        self.input_files_listbox.grid(row=0, column=1, padx=5, pady=5)

        self.select_files_button = tk.Button(master, text="Select Files", command=self.select_files)
        self.select_files_button.grid(row=0, column=2, padx=5, pady=5)

        self.move_up_button = tk.Button(master, text="Move Up", command=self.move_up)
        self.move_up_button.grid(row=1, column=2, padx=5, pady=5)

        self.move_down_button = tk.Button(master, text="Move Down", command=self.move_down)
        self.move_down_button.grid(row=2, column=2, padx=5, pady=5)

        # Merge button
        self.merge_button = tk.Button(master, text="Merge PDFs", command=self.merge_files)
        self.merge_button.grid(row=5, column=1, padx=5, pady=5)

    def select_files(self):
        filenames = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])
        self.input_files = list(filenames)
        self.update_input_files_listbox()

    def update_input_files_listbox(self):
        self.input_files_listbox.delete(0, tk.END)
        for file in self.input_files:
            self.input_files_listbox.insert(tk.END, file)

    def move_up(self):
        selected_index = self.input_files_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            if selected_index > 0:
                self.input_files[selected_index], self.input_files[selected_index - 1] = \
                    self.input_files[selected_index - 1], self.input_files[selected_index]
                self.update_input_files_listbox()

    def move_down(self):
        selected_index = self.input_files_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            if selected_index < len(self.input_files) - 1:
                self.input_files[selected_index], self.input_files[selected_index + 1] = \
                    self.input_files[selected_index + 1], self.input_files[selected_index]
                self.update_input_files_listbox()

    def merge_files(self):
        if not self.input_files:
            self.show_message("No input files selected.")
            return
        
        output_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_file_path:
            merge_pdfs(output_file_path, *self.input_files)
            self.refresh_gui()
            self.show_message("Merge operation completed.")
    
    def refresh_gui(self):
        self.input_files = []
        self.update_input_files_listbox()

    def show_message(self, message):
        message_label = tk.Label(self.master, text=message)
        message_label.grid(row=6, column=1, padx=5, pady=5)
        message_label.after(3000, lambda: message_label.destroy())  # Remove message after 3 seconds

def merge_pdfs(output_filename, *input_filenames):
    pdf_merger = PyPDF2.PdfMerger()

    for filename in input_filenames:
        with open(filename, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerGUI(root)
    root.mainloop()
