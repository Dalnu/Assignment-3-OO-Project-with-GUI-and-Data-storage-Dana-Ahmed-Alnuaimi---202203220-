import tkinter as tk
from tkinter import messagebox
from AggregationClass import *
from AssociationClass import *
from InheritanceClass import *
from CompositionClass import *
import pickle


employeeList = []
eventList = []
clientList = []
guestList = []
venueList = []
supplierList = []


class CategoryWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Category Window")
        self.geometry("400x200")

        # Create a label to inform the user
        info_label = tk.Label(self, text="Select a category to perform actions:")
        info_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create category buttons
        self.category_buttons = []
        categories = ["Employee", "Event", "Client", "Guest", "Venue", "Supplier"]
        for i in range(2):
            for j in range(3):
                index = i * 3 + j
                if index < len(categories):
                    button = tk.Button(self, text=categories[index], command=lambda c=categories[index]: self.open_category_window(c), width=15)
                    button.grid(row=i+1, column=j, padx=10, pady=10)
                    self.category_buttons.append(button)

        # Add exit button
        exit_button = tk.Button(self, text="Exit", command=self.quit, width=15)
        exit_button.grid(row=3, column=1, padx=10, pady=10)

    def open_category_window(self, category):
        self.withdraw()  # Hide the category window
        category_window = CategoryFunctionsWindow(self, category)
        category_window.mainloop()
        self.deiconify()  # Show the category window when the functions window is closed


class CategoryFunctionsWindow(tk.Tk):
    def __init__(self, master, category):
        super().__init__()
        self.master = master
        self.category = category
        self.title(f"{category} Functions")
        self.geometry("300x250")  # Increased height to accommodate the sentence

        # Add a sentence at the top
        sentence_label = tk.Label(self, text="Select an action to perform:")
        sentence_label.pack(pady=10)

        # Create a frame to hold the buttons
        frame = tk.Frame(self)
        frame.pack(expand=True)

        # Define width and height for buttons
        button_width = 15
        button_height = 2

        # Create function buttons
        functions = ["Add", "Delete", "Modify", "Display"]
        row_index = 0
        col_index = 0
        for function in functions:
            button = tk.Button(frame, text=function, command=lambda f=function: self.open_data_entry_window(f), width=button_width, height=button_height)
            button.grid(row=row_index, column=col_index, padx=10, pady=10)
            col_index += 1
            if col_index > 1:
                col_index = 0
                row_index += 1

        # Add back button
        back_button = tk.Button(frame, text="Back", command=self.go_back, width=button_width, height=button_height)
        back_button.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10)

    def open_data_entry_window(self, function):
        if function == "Display":
            if self.category == "Employee":
                title = "Display Employee Information"
            elif self.category == "Event":
                title = "Display Event Information"
            elif self.category == "Client":
                title = "Display Client Information"
            elif self.category == "Guest":
                title = "Display Guest Information"
            elif self.category == "Venue":
                title = "Display Venue Information"
            elif self.category == "Supplier":
                title = "Display Supplier Information"
            self.display_data_window = DisplayDataWindow(self, self.category, title)

        elif function == "Delete":
            self.delete_data_window = DeleteDataWindow(self, self.category)
        elif function == "Modify":
            self.modify_data_window = ModifyDataWindow(self, self.category)
        else:
            self.withdraw()  # Hide the functions window
            data_entry_window = DataEntryWindow(self, self.category, function)
            data_entry_window.mainloop()
            self.deiconify()  # Show the functions window when the data entry window is closed

    def go_back(self):
        self.destroy()  # Close the current window
        self.master.deiconify()  # Show the main window


class DataEntryWindow(tk.Tk):
    def __init__(self, master, category, function):
        super().__init__()
        self.master = master
        self.category = category
        self.function = function
        self.title(f"{function} {category}")
        self.geometry("300x800")

        # Create data entry widgets based on category and function
        # Entry widgets for employee data entry
        if category == "Employee":
            self.employee_name_label = tk.Label(self, text="Name:")
            self.employee_name_entry = tk.Entry(self)
            self.employee_name_label.pack()
            self.employee_name_entry.pack()

            self.employee_id_label = tk.Label(self, text="ID:")
            self.employee_id_entry = tk.Entry(self)
            self.employee_id_label.pack()
            self.employee_id_entry.pack()

            # Additional fields for Employee
            self.employee_department_label = tk.Label(self, text="Department:")
            self.employee_department_entry = tk.Entry(self)
            self.employee_department_label.pack()
            self.employee_department_entry.pack()


            self.employee_job_title_label = tk.Label(self, text="Job Title:")
            self.employee_job_title_entry = tk.Entry(self)
            self.employee_job_title_label.pack()
            self.employee_job_title_entry.pack()

            self.employee_basic_salary_label = tk.Label(self, text="Basic Salary:")
            self.employee_basic_salary_entry = tk.Entry(self)
            self.employee_basic_salary_label.pack()
            self.employee_basic_salary_entry.pack()

            self.employee_age_label = tk.Label(self, text="Age:")
            self.employee_age_entry = tk.Entry(self)
            self.employee_age_label.pack()
            self.employee_age_entry.pack()

            self.employee_date_of_birth_label = tk.Label(self, text="Date of Birth:")
            self.employee_date_of_birth_entry = tk.Entry(self)
            self.employee_date_of_birth_label.pack()
            self.employee_date_of_birth_entry.pack()

        elif category == "Event":
            self.event_id_label = tk.Label(self, text="Event ID:")
            self.event_id_entry = tk.Entry(self)
            self.event_id_label.pack()
            self.event_id_entry.pack()

            self.event_type_label = tk.Label(self, text="Type:")
            self.event_type_entry = tk.Entry(self)
            self.event_type_label.pack()
            self.event_type_entry.pack()

            self.event_theme_label = tk.Label(self, text="Theme:")
            self.event_theme_entry = tk.Entry(self)
            self.event_theme_label.pack()
            self.event_theme_entry.pack()

            self.event_date_label = tk.Label(self, text="Date (YYYY-MM-DD):")
            self.event_date_entry = tk.Entry(self)
            self.event_date_label.pack()
            self.event_date_entry.pack()

            self.event_time_label = tk.Label(self, text="Time (HH:MM):")
            self.event_time_entry = tk.Entry(self)
            self.event_time_label.pack()
            self.event_time_entry.pack()

            self.event_duration_label = tk.Label(self, text="Duration:")
            self.event_duration_entry = tk.Entry(self)
            self.event_duration_label.pack()
            self.event_duration_entry.pack()

            self.event_venue_label = tk.Label(self, text="Venue Address:")
            self.event_venue_entry = tk.Entry(self)
            self.event_venue_label.pack()
            self.event_venue_entry.pack()

            self.event_client_label = tk.Label(self, text="Client ID:")
            self.event_client_entry = tk.Entry(self)
            self.event_client_label.pack()
            self.event_client_entry.pack()

            self.catering_company_label = tk.Label(self, text="Catering Company:")
            self.catering_company_entry = tk.Entry(self)
            self.catering_company_label.pack()
            self.catering_company_entry.pack()

            self.cleaning_company_label = tk.Label(self, text="Cleaning Company:")
            self.cleaning_company_entry = tk.Entry(self)
            self.cleaning_company_label.pack()
            self.cleaning_company_entry.pack()

            self.decorations_company_label = tk.Label(self, text="Decorations Company:")
            self.decorations_company_entry = tk.Entry(self)
            self.decorations_company_label.pack()
            self.decorations_company_entry.pack()

            self.entertainment_company_label = tk.Label(self, text="Entertainment Company:")
            self.entertainment_company_entry = tk.Entry(self)
            self.entertainment_company_label.pack()
            self.entertainment_company_entry.pack()

            self.furniture_company_label = tk.Label(self, text="Furniture Supply Company:")
            self.furniture_company_entry = tk.Entry(self)
            self.furniture_company_label.pack()
            self.furniture_company_entry.pack()

            self.event_invoice_label = tk.Label(self, text="Invoice:")
            self.event_invoice_entry = tk.Entry(self)
            self.event_invoice_label.pack()
            self.event_invoice_entry.pack()

        elif category == "Client":
            self.client_id_label = tk.Label(self, text="Client ID:")
            self.client_id_entry = tk.Entry(self)
            self.client_id_label.pack()
            self.client_id_entry.pack()

            self.client_name_label = tk.Label(self, text="Client Name:")
            self.client_name_entry = tk.Entry(self)
            self.client_name_label.pack()
            self.client_name_entry.pack()

            self.client_contact_label = tk.Label(self, text="Contact Number:")
            self.client_contact_entry = tk.Entry(self)
            self.client_contact_label.pack()
            self.client_contact_entry.pack()

            self.client_email_label = tk.Label(self, text="Email Address:")
            self.client_email_entry = tk.Entry(self)
            self.client_email_label.pack()
            self.client_email_entry.pack()

            self.client_address_label = tk.Label(self, text="Address:")
            self.client_address_entry = tk.Entry(self)
            self.client_address_label.pack()
            self.client_address_entry.pack()

        elif category == "Guest":
            self.guest_id_label = tk.Label(self, text="Guest ID:")
            self.guest_id_entry = tk.Entry(self)
            self.guest_id_label.pack()
            self.guest_id_entry.pack()

            self.guest_name_label = tk.Label(self, text="Guest Name:")
            self.guest_name_entry = tk.Entry(self)
            self.guest_name_label.pack()
            self.guest_name_entry.pack()

            self.guest_contact_label = tk.Label(self, text="Contact Number:")
            self.guest_contact_entry = tk.Entry(self)
            self.guest_contact_label.pack()
            self.guest_contact_entry.pack()

            self.guest_email_label = tk.Label(self, text="Email Address:")
            self.guest_email_entry = tk.Entry(self)
            self.guest_email_label.pack()
            self.guest_email_entry.pack()

            self.guest_address_label = tk.Label(self, text="Address:")
            self.guest_address_entry = tk.Entry(self)
            self.guest_address_label.pack()
            self.guest_address_entry.pack()

        elif category == "Venue":
            self.venue_id_label = tk.Label(self, text="Venue ID:")
            self.venue_id_entry = tk.Entry(self)
            self.venue_id_label.pack()
            self.venue_id_entry.pack()

            self.venue_name_label = tk.Label(self, text="Name:")
            self.venue_name_entry = tk.Entry(self)
            self.venue_name_label.pack()
            self.venue_name_entry.pack()

            self.venue_address_label = tk.Label(self, text="Address:")
            self.venue_address_entry = tk.Entry(self)
            self.venue_address_label.pack()
            self.venue_address_entry.pack()

            self.venue_contact_label = tk.Label(self, text="Contact Number:")
            self.venue_contact_entry = tk.Entry(self)
            self.venue_contact_label.pack()
            self.venue_contact_entry.pack()

            self.venue_min_guests_label = tk.Label(self, text="Min Guests:")
            self.venue_min_guests_entry = tk.Entry(self)
            self.venue_min_guests_label.pack()
            self.venue_min_guests_entry.pack()

            self.venue_max_guests_label = tk.Label(self, text="Max Guests:")
            self.venue_max_guests_entry = tk.Entry(self)
            self.venue_max_guests_label.pack()
            self.venue_max_guests_entry.pack()

        elif category == "Supplier":
            self.supplier_id_label = tk.Label(self, text="Supplier ID:")
            self.supplier_id_entry = tk.Entry(self)
            self.supplier_id_label.pack()
            self.supplier_id_entry.pack()

            self.supplier_name_label = tk.Label(self, text="Name:")
            self.supplier_name_entry = tk.Entry(self)
            self.supplier_name_label.pack()
            self.supplier_name_entry.pack()

            self.supplier_address_label = tk.Label(self, text="Address:")
            self.supplier_address_entry = tk.Entry(self)
            self.supplier_address_label.pack()
            self.supplier_address_entry.pack()

            self.supplier_contact_label = tk.Label(self, text="Contact Details:")
            self.supplier_contact_entry = tk.Entry(self)
            self.supplier_contact_label.pack()
            self.supplier_contact_entry.pack()

        # Save data to pickle file or perform appropriate action based on function
        save_button = tk.Button(self, text="Save", command=self.save_data)
        save_button.pack()

        # Add back button
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack()

    def save_data(self):
        if self.category == "Employee":
            name = self.employee_name_entry.get()
            employeeID = self.employee_id_entry.get()
            department = self.employee_department_entry.get()
            jobTitle = self.employee_job_title_entry.get()
            basicSalary = self.employee_basic_salary_entry.get()
            age = self.employee_age_entry.get()
            dateOfBirth = self.employee_date_of_birth_entry.get()
            # Create Employee instance
            employee = Employee(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth)
            # Save employee data to pickle file or perform other action based on function
            employeeList.append(employee)

            with open('emp.dat', 'wb') as outputfile:
                # Create a dictionary with employee IDs as keys and employee objects as values
                employee_dict = {employeeID: employee for employee in employeeList}
                # Pickle the dictionary to the file
                pickle.dump(employee_dict, outputfile)
            print("Employee data saved:", employee)


        elif self.category == "Event":
            eventID = self.event_id_entry.get()
            eventType = self.event_type_entry.get()
            eventTheme = self.event_theme_entry.get()
            eventDate = self.event_date_entry.get()
            eventTime = self.event_time_entry.get()
            eventDuration = self.event_duration_entry.get()
            eventVenue = self.event_venue_entry.get()
            eventClient = self.event_client_entry.get()
            eventInvoice = self.event_invoice_entry.get()
            # Create Event instance
            event = Event(eventID, eventType, eventTheme, eventDate, eventTime, eventDuration, eventVenue, eventClient,
                          None, None, None, None, None, eventInvoice)
            # Save event data to pickle file or perform other action based on function
            print("Event data saved:", event)
            eventList.append(event)

            with open('eve.dat', 'wb') as outputfile:
                # Create a dictionary with employee IDs as keys and employee objects as values
                event_dict = {eventID: event for event in eventList}
                # Pickle the dictionary to the file
                pickle.dump(event_dict, outputfile)


        elif self.category == "Client":
            clientID = self.client_id_entry.get()
            clientName = self.client_name_entry.get()
            clientContact = self.client_contact_entry.get()
            clientEmail = self.client_email_entry.get()
            clientAddress = self.client_address_entry.get()
            # Create Client instance
            client = Client(clientID, clientName, clientContact, clientEmail, clientAddress)
            # Save client data to pickle file or perform other action based on function
            print("Client data saved:", client)
            clientList.append(client)

            with open('cli.dat', 'wb') as outputfile:
                # Create a dictionary with employee IDs as keys and employee objects as values
                client_dict = {clientID: client for client in clientList}
                # Pickle the dictionary to the file
                pickle.dump(client_dict, outputfile)

        elif self.category == "Guest":
            guestID = self.guest_id_entry.get()
            guestName = self.guest_name_entry.get()
            guestContact = self.guest_contact_entry.get()
            guestEmail = self.guest_email_entry.get()
            guestAddress = self.guest_address_entry.get()
            # Create Guest instance
            guest = Guest(guestID, guestName, guestContact, guestEmail, guestAddress)
            # Save guest data to pickle file or perform other action based on function
            print("Guest data saved:", guest)
            guestList.append(guest)

            with open('gus.dat', 'wb') as outputfile:
                # Create a dictionary with employee IDs as keys and employee objects as values
                guest_dict = {guestID: guest for guest in guestList}
                # Pickle the dictionary to the file
                pickle.dump(guest_dict, outputfile)

        elif self.category == "Venue":
            venue_id = self.venue_id_entry.get()
            name = self.venue_name_entry.get()
            address = self.venue_address_entry.get()
            contact = self.venue_contact_entry.get()
            min_guests = self.venue_min_guests_entry.get()
            max_guests = self.venue_max_guests_entry.get()
            # Create Venue instance
            venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
            # Save venue data to pickle file or perform other action based on function
            print("Venue data saved:", venue)
            venueList.append(venue)

            with open('ven.dat', 'wb') as outputfile:
                # Create a dictionary with employee IDs as keys and employee objects as values
                venue_dict = {venue_id: venue for venue in venueList}
                # Pickle the dictionary to the file
                pickle.dump(venue_dict, outputfile)

            # Reset entry fields
            self.reset_fields()

        elif self.category == "Supplier":
            supplierID = self.supplier_id_entry.get()
            name = self.supplier_name_entry.get()
            address = self.supplier_address_entry.get()
            contactDetails = self.supplier_contact_entry.get()
            # Create Supplier instance
            supplier = Supplier(supplierID, name, address, contactDetails)
            # Save supplier data to pickle file or perform other action based on function
            print("Supplier data saved:", supplier)
            supplierList.append(supplier)

            with open('sup.dat', 'wb') as outputfile:
                # Create a dictionary with employee IDs as keys and employee objects as values
                supplier_dict = {supplierID: supplier for supplier in supplierList}
                # Pickle the dictionary to the file
                pickle.dump(supplier_dict, outputfile)

    def reset_fields(self):
        # Clear entry fields after saving data
        self.venue_id_entry.delete(0, tk.END)
        self.venue_name_entry.delete(0, tk.END)
        self.venue_address_entry.delete(0, tk.END)
        self.venue_contact_entry.delete(0, tk.END)
        self.venue_min_guests_entry.delete(0, tk.END)
        self.venue_max_guests_entry.delete(0, tk.END)

    def go_back(self):
        self.destroy()  # Close the current window
        self.master.deiconify()  # Show the category functions window


class DisplayDataWindow(tk.Tk):
    def __init__(self, master, category, title):
        super().__init__()
        self.master = master
        self.category = category
        self.title(title)  # Set the window title based on the parameter
        self.geometry("300x100")

        self.id_label = tk.Label(self, text=f"Enter {category} ID:")
        self.id_entry = tk.Entry(self)
        self.id_label.pack()
        self.id_entry.pack()

        display_button = tk.Button(self, text="Display", command=self.display_data)
        display_button.pack()

        # Add back button
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack()

    def display_data(self):
        data_id = self.id_entry.get()

        if self.category == "Employee":
            try:
                with open('emp.dat', 'rb') as inputfile:
                    # Unpickle the dictionary from the file
                    employee_dict = pickle.load(inputfile)
                    # Check if the data_id exists in the dictionary
                    if data_id in employee_dict:
                        # If employee exists, retrieve the employee data
                        employee = employee_dict[data_id]
                        # Display employee information
                        info = f"Name: {employee.getName()}\nID: {employee.getEmployeeID()}\nDepartment: {employee.getDepartment()}\nJob Title: {employee.getJobTitle()}\nBasic Salary: {employee.getBasicSalary()}\nAge: {employee.getAge()}\nDate of Birth: {employee.getDateOfBirth()}"
                        messagebox.showinfo("Employee Information", info)
                    else:
                        messagebox.showerror("Error", "Employee not found")
            except FileNotFoundError:
                # Show error message if the file is not found
                messagebox.showerror("Error", "Employee data file not found")


        elif self.category == "Event":
            try:
                with open('eve.dat', 'rb') as inputfile:
                    # Unpickle the dictionary from the file
                    event_dict = pickle.load(inputfile)
                    # Check if the data_id exists in the dictionary
                    if data_id in event_dict:
                        # If event exists, retrieve the event data
                        event = event_dict[data_id]
                        # Display event information
                        info = f"Event ID: {event.getEventID()}\nType: {event.getType()}\nTheme: {event.getTheme()}" \
                               f"\nDate: {event.getDate()}\nTime: {event.getTime()}\nDuration: {event.getDuration()}" \
                               f"\nVenue: {event.getVenueAddress()}\nClient ID: {event.getClientID()}\n" \
                               f"Invoice: {event.getInvoice()} "
                        messagebox.showinfo("Event Information", info)
                    else:
                        messagebox.showerror("Error", "Event not found")
            except FileNotFoundError:
                # Show error message if the file is not found
                messagebox.showerror("Error", "Event data file not found")



        elif self.category == "Client":
            try:
                with open('cli.dat', 'rb') as inputfile:
                    # Unpickle the dictionary from the file
                    client_dict = pickle.load(inputfile)                        # Check if the data_id exists in the dictionary
                    if data_id in client_dict:
                        # If client exists, retrieve the client data
                        client = client_dict[data_id]
                        # Display client information
                        info = f"Client ID: {client.getClientID()}\nName: {client.getName()}\nContact Number: " \
                               f"{client.getContactDetails()}\nBudget: {client.getBudget()}\nAddress: " \
                               f"{client.getAddress()}"
                        messagebox.showinfo("Client Information", info)
                    else:
                        messagebox.showerror("Error", "Client not found")
            except FileNotFoundError:
                # Show error message if the file is not found
                messagebox.showerror("Error", "Client data file not found")


        elif self.category == "Guest":
            try:
                with open('gus.dat', 'rb') as inputfile:
                    # Unpickle the dictionary from the file
                    guest_dict = pickle.load(inputfile)
                    # Check if the data_id exists in the dictionary
                    if data_id in guest_dict:
                        # If guest exists, retrieve the guest data
                        guest = guest_dict[data_id]
                        # Display guest information
                        info = f"Guest ID: {guest.getGuestID()}\nName: {guest.getGuestName()}\nContact Number: " \
                               f"{guest.getGuestContact()}\nEmail Address: {guest.getGuestEmail()}\nAddress: " \
                               f"{guest.getGuestAddress()}"
                        messagebox.showinfo("Guest Information", info)
                    else:
                        messagebox.showerror("Error", "Guest not found")
            except FileNotFoundError:
                # Show error message if the file is not found
                messagebox.showerror("Error", "Guest data file not found")


        elif self.category == "Venue":
            try:
                with open('ven.dat', 'rb') as inputfile:
                    # Unpickle the dictionary from the file
                    venue_dict = pickle.load(inputfile)
                    # Check if the data_id exists in the dictionary
                    if data_id in venue_dict:
                        # If venue exists, retrieve the venue data
                        venue = venue_dict[data_id]
                        # Display venue information
                        info = f"Venue ID: {venue.getVenueID()}\nName: {venue.getName()}\nAddress: {venue.getAddress()}" \
                               f"\nContact Number: {venue.getContact()}\nMin Guests: {venue.getMinGuests()}\nMax Guests:" \
                               f" {venue.getMaxGuests()}"
                        messagebox.showinfo("Venue Information", info)
                    else:
                        messagebox.showerror("Error", "Venue not found")
            except FileNotFoundError:
                # Show error message if the file is not found
                messagebox.showerror("Error", "Venue data file not found")


        elif self.category == "Supplier":
            try:
                with open('sup.dat', 'rb') as inputfile:
                    # Unpickle the dictionary from the file
                    supplier_dict = pickle.load(inputfile)
                    # Check if the data_id exists in the dictionary
                    if data_id in supplier_dict:
                        # If supplier exists, retrieve the supplier data
                        supplier = supplier_dict[data_id]
                        # Display supplier information
                        info = f"Supplier ID: {supplier.getSupplierID()}\nName: {supplier.getName()}\nAddress:" \
                               f" {supplier.getAddress()}\nContact Details: {supplier.getContactDetails()}"
                        messagebox.showinfo("Supplier Information", info)
                    else:
                        messagebox.showerror("Error", "Supplier not found")
            except FileNotFoundError:
                # Show error message if the file is not found
                messagebox.showerror("Error", "Supplier data file not found")

    def go_back(self):
        self.destroy()  # Close the current window
        self.master.deiconify()  # Show the category functions window


class DeleteDataWindow(tk.Tk):
    def __init__(self, master, category):
        super().__init__()
        self.master = master
        self.category = category
        self.title(f"Delete {category} by ID")
        self.geometry("300x100")

        self.id_label = tk.Label(self, text=f"Enter {category} ID:")
        self.id_entry = tk.Entry(self)
        self.id_label.pack()
        self.id_entry.pack()

        delete_button = tk.Button(self, text="Delete", command=self.delete_data)
        delete_button.pack()

        # Add back button
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack()

    def delete_data(self):
        data_id = self.id_entry.get()

        if self.category == "Employee":
            try:
                with open('emp.dat', 'rb') as inputfile:
                    employee_dict = pickle.load(inputfile)
                    if data_id in employee_dict:
                        del employee_dict[data_id]  # Delete the employee data
                        with open('emp.dat', 'wb') as outputfile:
                            pickle.dump(employee_dict, outputfile)
                        messagebox.showinfo("Success", "Employee data deleted successfully")
                    else:
                        messagebox.showerror("Error", "Employee not found")
            except FileNotFoundError:
                messagebox.showerror("Error", "Employee data file not found")

        elif self.category == "Event":
            try:
                with open('eve.dat', 'rb') as inputfile:
                    event_dict = pickle.load(inputfile)
                    if data_id in event_dict:
                        del event_dict[data_id]  # Delete the event data
                        with open('eve.dat', 'wb') as outputfile:
                            pickle.dump(event_dict, outputfile)
                        messagebox.showinfo("Success", "Event data deleted successfully")
                    else:
                        messagebox.showerror("Error", "Event not found")
            except FileNotFoundError:
                messagebox.showerror("Error", "Event data file not found")

        elif self.category == "Client":
            try:
                with open('cli.dat', 'rb') as inputfile:
                    client_dict = pickle.load(inputfile)
                    if data_id in client_dict:
                        del client_dict[data_id]  # Delete the client data
                        with open('cli.dat', 'wb') as outputfile:
                            pickle.dump(client_dict, outputfile)
                        messagebox.showinfo("Success", "Client data deleted successfully")
                    else:
                        messagebox.showerror("Error", "Client not found")
            except FileNotFoundError:
                messagebox.showerror("Error", "Client data file not found")

        elif self.category == "Guest":
            try:
                with open('gus.dat', 'rb') as inputfile:
                    guest_dict = pickle.load(inputfile)
                    if data_id in guest_dict:
                        del guest_dict[data_id]  # Delete the guest data
                        with open('gus.dat', 'wb') as outputfile:
                            pickle.dump(guest_dict, outputfile)
                        messagebox.showinfo("Success", "Guest data deleted successfully")
                    else:
                        messagebox.showerror("Error", "Guest not found")
            except FileNotFoundError:
                messagebox.showerror("Error", "Guest data file not found")

        elif self.category == "Venue":
            try:
                with open('ven.dat', 'rb') as inputfile:
                    venue_dict = pickle.load(inputfile)
                    if data_id in venue_dict:
                        del venue_dict[data_id]  # Delete the venue data
                        with open('ven.dat', 'wb') as outputfile:
                            pickle.dump(venue_dict, outputfile)
                        messagebox.showinfo("Success", "Venue data deleted successfully")
                    else:
                        messagebox.showerror("Error", "Venue not found")
            except FileNotFoundError:
                messagebox.showerror("Error", "Venue data file not found")

        elif self.category == "Supplier":
            try:
                with open('sup.dat', 'rb') as inputfile:
                    supplier_dict = pickle.load(inputfile)
                    if data_id in supplier_dict:
                        del supplier_dict[data_id]  # Delete the supplier data
                        with open('sup.dat', 'wb') as outputfile:
                            pickle.dump(supplier_dict, outputfile)
                        messagebox.showinfo("Success", "Supplier data deleted successfully")
                    else:
                        messagebox.showerror("Error", "Supplier not found")
            except FileNotFoundError:
                messagebox.showerror("Error", "Supplier data file not found")

    def go_back(self):
        self.destroy()  # Close the current window
        self.master.deiconify()  # Show the category functions window



class ModifyDataWindow(tk.Tk):
    def __init__(self, master, category):
        super().__init__()
        self.master = master
        self.category = category
        self.title(f"Modify {category} by ID")
        self.geometry("300x100")

        self.id_label = tk.Label(self, text=f"Enter {category} ID:")
        self.id_entry = tk.Entry(self)
        self.id_label.pack()
        self.id_entry.pack()

        modify_button = tk.Button(self, text="Modify", command=self.modify_data)
        modify_button.pack()

        # Add back button
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack()

    def modify_data(self):
        data_id = self.id_entry.get()

        if self.category == "Employee":
            try:
                with open('emp.dat', 'rb') as inputfile:
                    employee_dict = pickle.load(inputfile)
                    if data_id in employee_dict:
                        # Retrieve the employee object
                        employee = employee_dict[data_id]
                        # Destroy current window
                        self.destroy()
                        # Create a new window for modifying employee data
                        ModifyDataWindow(self.master, employee)
                    else:
                        messagebox.showerror("Error", "Employee not found")
            except FileNotFoundError:
                messagebox.showerror("Error", "Employee data file not found")

    def go_back(self):
        self.destroy()
        self.master.deiconify()



# Main
if __name__ == "__main__":
    app = CategoryWindow()
    app.mainloop()
