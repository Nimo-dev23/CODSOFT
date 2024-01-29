import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        
        self.contacts = []
        
        self.widgets()
        
    def widgets(self):
        # Labels and Entries for Contact Information
        tk.Label(self.master, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.master, text="Phone:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_phone = tk.Entry(self.master)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.master, text="Email:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.master, text="Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_address = tk.Entry(self.master)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)
        
        # Buttons
        tk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(self.master, text="View Contact List", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(self.master, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(self.master, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=5)
        tk.Button(self.master, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=5)
        
        
        
    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        
        if name and phone:
            contact = (name, phone, email, address)
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, f"{name}: {phone}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")
            
    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact[0]}: {contact[1]}")
            
    def search_contact(self):
        search_term = self.entry_name.get() if self.entry_name.get() else self.entry_phone.get()
        if search_term:
            self.contact_listbox.delete(0, tk.END)
            for contact in self.contacts:
                if search_term.lower() in contact[0].lower() or search_term.lower() in contact[1].lower():
                    self.contact_listbox.insert(tk.END, f"{contact[0]}: {contact[1]}")
        else:
            messagebox.showerror("Error", "Please enter a search term.")
            
    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            name = self.entry_name.get()
            phone = self.entry_phone.get()
            email = self.entry_email.get()
            address = self.entry_address.get()
            
            if name and phone:
                self.contacts[selected_index[0]] = (name, phone, email, address)
                self.view_contacts()
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Name and Phone Number are required fields.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")
            
    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")
            
    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
