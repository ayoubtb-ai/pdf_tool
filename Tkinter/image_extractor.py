import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader

def process_pdf():
    file_path = file_path_var.get()
    if file_path:
        reader = PdfReader(file_path)
        page = reader.pages[0]
        count = 0
        for image_file_object in page.images:
            with open(str(count) + image_file_object.name, "wb") as fp:
                fp.write(image_file_object.data)
                count += 1
        status_label.config(text="PDF processed successfully!")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_path_var.set(file_path)

# Create the main window
root = tk.Tk()
root.title("PDF Processor")

# Create a variable to store the file path
file_path_var = tk.StringVar()

# Create a label to show status
status_label = tk.Label(root, text="")

# Create a button to browse for a PDF file
browse_button = tk.Button(root, text="Browse", command=browse_file)

# Create a button to start processing the PDF
process_button = tk.Button(root, text="Process PDF", command=process_pdf)

# Layout the widgets
browse_button.pack(pady=10)
status_label.pack()
process_button.pack(pady=10)

# Start the main event loop
root.mainloop()
