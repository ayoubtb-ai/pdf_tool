import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

def select_pdf():
    file_path = filedialog.askopenfilename(title="Select PDF File")
    if file_path:
        pdf_path_entry.delete(0, tk.END)
        pdf_path_entry.insert(0, file_path)

def encrypt_pdf():
    file_path = pdf_path_entry.get()
    password = password_entry.get()
    if file_path and password:
        try:
            reader = PdfReader(file_path)
            writer = PdfWriter()

            # Add all pages to the writer
            for page in reader.pages:
                writer.add_page(page)

            # Add a password to the new PDF
            writer.encrypt(password)

            # Save the new PDF to a file
            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save Encrypted PDF")
            if save_path:
                with open(save_path, "wb") as f:
                    writer.write(f)
                status_label.config(text="PDF encrypted and saved successfully.", fg="green")
                
                # Reset input fields and status label
                pdf_path_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                status_label.after(3000, clear_status)
                
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")
    else:
        status_label.config(text="Please select a PDF file and enter a password.", fg="red")

def clear_status():
    status_label.config(text="")

# Create the GUI window
root = tk.Tk()
root.title("PDF Encryptor")

# Create and place widgets
pdf_path_label = tk.Label(root, text="PDF File:")
pdf_path_label.grid(row=0, column=0, sticky="e")

pdf_path_entry = tk.Entry(root, width=50)
pdf_path_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Browse", command=select_pdf)
browse_button.grid(row=0, column=2, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt PDF", command=encrypt_pdf)
encrypt_button.grid(row=2, column=1, padx=5, pady=5)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
