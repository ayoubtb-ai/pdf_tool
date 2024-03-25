import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader

class PDFMetadataViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Metadata Viewer")

        self.label = tk.Label(master, text="PDF Metadata:")
        self.label.pack()

        self.text = tk.Text(master, height=10, width=50)
        self.text.pack()

        self.btn_open = tk.Button(master, text="Open PDF", command=self.open_pdf)
        self.btn_open.pack()

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.display_metadata(file_path)

    def display_metadata(self, file_path):
        try:
            reader = PdfReader(file_path)
            metadata = reader.metadata
            num_pages = len(reader.pages)

            meta_info = f"Number of Pages: {num_pages}\n"
            meta_info += f"Author: {metadata.author}\n"
            meta_info += f"Creator: {metadata.creator}\n"
            meta_info += f"Producer: {metadata.producer}\n"
            meta_info += f"Subject: {metadata.subject}\n"
            meta_info += f"Title: {metadata.title}\n"

            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, meta_info)
        except Exception as e:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = PDFMetadataViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
