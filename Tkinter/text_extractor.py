from tkinter import Tk, Button, Label, Entry, filedialog
from PyPDF2 import PdfReader

def browse_file():
    # Open a file dialog for the user to select a file
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        filename_entry.delete(0, 'end')  # Clear any previous entry
        filename_entry.insert(0, filename)  # Update entry with selected filename

def extract_text_and_save():
    # Get the filename and page numbers from the entry widgets
    filename = filename_entry.get()
    page_numbers = page_numbers_entry.get()
    
    # Extract text from the PDF
    reader = PdfReader(filename)
    extracted_text = ""
    
    if page_numbers.lower() == "all":
        for page in reader.pages:
            extracted_text += page.extract_text()
    else:
        selected_pages = [int(num) - 1 for num in page_numbers.split(",")]
        for num in selected_pages:
            page = reader.pages[num]
            extracted_text += page.extract_text()

    # Open a file dialog for the user to choose the destination folder and filename
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        with open(save_path, "w") as file:
            file.write(extracted_text)
        status_label.config(text="Text extracted and saved to {}".format(save_path))
    else:
        status_label.config(text="Extraction canceled.")

# Create the main window
root = Tk()
root.title("PDF Text Extractor")

# Create and place widgets
Label(root, text="Select PDF file to extract text:").pack()
filename_entry = Entry(root)
filename_entry.pack()

browse_button = Button(root, text="Browse", command=browse_file)
browse_button.pack()

Label(root, text="Enter page numbers (e.g., 1, 3, 5 or 'All' for all pages):").pack()
page_numbers_entry = Entry(root)
page_numbers_entry.pack()

extract_button = Button(root, text="Extract Text and Save", command=extract_text_and_save)
extract_button.pack()

status_label = Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()
