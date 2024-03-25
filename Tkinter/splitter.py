import PyPDF2
import tkinter as tk
from tkinter import filedialog

def extract_specific_pages(input_pdf, output_pdf, *page_numbers):
    """
    Extract specific pages from input_pdf and save them to output_pdf.
    
    Parameters:
        input_pdf (str): Name of the input PDF file.
        output_pdf (str): Name of the output PDF file.
        *page_numbers (int): Page numbers to extract.
    """
    with open(input_pdf, 'rb') as objFile:
        pdfReader = PyPDF2.PdfReader(objFile)
        
        pdfWriter = PyPDF2.PdfWriter()
        for page_num in page_numbers:
            pageObj = pdfReader.pages[page_num - 1]  # Adjust to zero-based indexing
            pdfWriter.add_page(pageObj)
        
        with open(output_pdf, 'wb') as pdfOutputFile:
            pdfWriter.write(pdfOutputFile)

def browse_pdf():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(tk.END, filename)

def extract_pages():
    input_pdf = entry_pdf.get()
    page_numbers_str = entry_pages.get()
    page_numbers = [int(num.strip()) for num in page_numbers_str.split(',')]
    
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF files", "*.pdf")])
    
    if output_pdf:
        extract_specific_pages(input_pdf, output_pdf, *page_numbers)
        status_label.config(text="Extraction complete.")
    else:
        status_label.config(text="Extraction canceled.")
    
    # Refresh GUI
    entry_pdf.delete(0, tk.END)
    entry_pages.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("PDF Page Extractor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_pdf = tk.Label(frame, text="Input PDF:")
label_pdf.grid(row=0, column=0, sticky="w")

entry_pdf = tk.Entry(frame, width=50)
entry_pdf.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(frame, text="Browse", command=browse_pdf)
browse_button.grid(row=0, column=2, padx=5, pady=5)

label_pages = tk.Label(frame, text="Page Numbers:")
label_pages.grid(row=1, column=0, sticky="w")

entry_pages = tk.Entry(frame, width=50)
entry_pages.grid(row=1, column=1, padx=5, pady=5)

extract_button = tk.Button(frame, text="Extract Pages", command=extract_pages)
extract_button.grid(row=2, column=1, padx=5, pady=5)

status_label = tk.Label(frame, text="")
status_label.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
