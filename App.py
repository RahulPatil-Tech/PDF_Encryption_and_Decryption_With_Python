import PyPDF2
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, ttk

def encrypt_pdf():
    # Get the selected PDF file
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    if not file_path:
        return
    
    # Get the password from the entry field
    password = password_entry.get()
    
    # Create a PDF writer object
    writer = PyPDF2.PdfWriter()
    
    try:
        # Read the PDF file
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Iterate through each page and add it to the writer object
            for page_num in range(len(reader.pages)):
                writer.add_page(reader.pages[page_num])
            
            # Encrypt the PDF with the provided password
            writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
            
            # Write the encrypted PDF to a new file
            output_filename = f"encrypted_{file_path.split('/')[-1]}"
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)
            
            messagebox.showinfo("Success", f"The PDF has been encrypted and saved as {output_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def decrypt_pdf():
    # Get the selected PDF file
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if not file_path:
        return

    # Get the password from the entry field
    password = password_entry.get()

    try:
        # Read the PDF file
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            # Check if the PDF is encrypted
            if reader.is_encrypted:
                # Verify the provided password
                if reader.decrypt(password):
                    # Create a new PDF writer object
                    writer = PyPDF2.PdfWriter()

                    # Add all the pages to the writer object
                    for page_num in range(len(reader.pages)):
                        writer.add_page(reader.pages[page_num])

                    # Write the decrypted PDF to a new file
                    output_filename = f"decrypted_{file_path.split('/')[-1]}"
                    with open(output_filename, 'wb') as output_file:
                        writer.write(output_file)

                    messagebox.showinfo("Success", f"The PDF has been decrypted and saved as {output_filename}")
                else:
                    messagebox.showerror("Error", "Incorrect password for decryption")
            else:
                messagebox.showinfo("Info", "The PDF is already decrypted")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the Tkinter window
window = Tk()
window.title("PDF Encryption/Decryption")
window.geometry("400x250")

# Create labels and entry fields
password_label = Label(window, text="Enter Password:", font=("Arial", 14))
password_label.pack(pady=10)

password_entry = Entry(window, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

# Create the encryption button
encrypt_button = Button(window, text="Encrypt PDF",bg ='LimeGreen', command=encrypt_pdf, font=("Arial", 12), width=15)
encrypt_button.pack(pady=10)

# Create the decryption button
decrypt_button = Button(window, text="Decrypt PDF",bg ='OrangeRed', command=decrypt_pdf, font=("Arial", 12), width=15)
decrypt_button.pack(pady=5)

# Style the buttons using ttk
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), foreground="white", background="#4CAF50", width=15)

# Start the Tkinter event loop
window.mainloop()
