import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

    info_label.config(text="Compression complete.")
    selected_file_label.config(text="Selected File: None")
    compress_button.config(state=tk.DISABLED)

# Function to handle button click for selecting PDF file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        selected_file_label.config(text="Selected File: " + file_path)
        compress_button.config(state=tk.NORMAL)
        global input_path
        input_path = file_path

# Function to handle button click for compression and saving
def compress_and_save():
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                filetypes=[("PDF files", "*.pdf")])
    if not output_path:
        return  # No save path provided
    compress_pdf(input_path, output_path)

# Create a Tkinter window
window = tk.Tk()
window.title("PDF Compressor")

# Create a label
info_label = tk.Label(window, text="Select a PDF file to compress.")
info_label.pack()

# Create a button to select a PDF file
select_button = tk.Button(window, text="Select PDF File", command=select_file)
select_button.pack()

# Label to display selected file
selected_file_label = tk.Label(window, text="Selected File: None")
selected_file_label.pack()

# Create a button to execute compression and save
compress_button = tk.Button(window, text="Compress and Save", command=compress_and_save, state=tk.DISABLED)
compress_button.pack()

# Run the Tkinter event loop
window.mainloop()
