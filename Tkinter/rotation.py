import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfWriter, PdfReader

def rotate_pdf():
    input_file = file_path_entry.get()
    rotation_angle = int(angle_entry.get())

    page_numbers = pages_entry.get().split(',')
    if "all" in page_numbers:
        page_numbers = range(len(PdfReader(input_file).pages))
    else:
        page_numbers = [int(page.strip()) for page in page_numbers]

    writer = PdfWriter()
    reader = PdfReader(input_file)
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        if page_number in page_numbers:
            page.rotate(rotation_angle)
        writer.add_page(page)

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf")
    if output_file:
        with open(output_file, "wb") as f:
            writer.write(f)
            status_label.config(text="PDF file rotated and saved successfully!")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

# Create GUI
root = tk.Tk()
root.title("PDF Page Rotation")

file_label = tk.Label(root, text="Select PDF file:")
file_label.grid(row=0, column=0)

file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=1)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2)

pages_label = tk.Label(root, text="Pages to rotate (comma-separated, 'all' for all pages):")
pages_label.grid(row=1, column=0)

pages_entry = tk.Entry(root, width=50)
pages_entry.grid(row=1, column=1)

angle_label = tk.Label(root, text="Rotation angle (in degrees):")
angle_label.grid(row=2, column=0)

angle_entry = tk.Entry(root, width=50)
angle_entry.grid(row=2, column=1)

rotate_button = tk.Button(root, text="Rotate", command=rotate_pdf)
rotate_button.grid(row=3, column=1)

status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
