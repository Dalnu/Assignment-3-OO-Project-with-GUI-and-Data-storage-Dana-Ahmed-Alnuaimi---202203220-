class Person:
    """Represents a person."""
    def __init__(self, name, address, contactDetails):
        """Initialize a Person object with the given attributes."""
        self._name = name
        self._address = address
        self._contactDetails = contactDetails

    def setName(self, name):
        """Set the name of the person."""
        self._name = name
    def getName(self):
        """Return the name of the person."""
        return self._name

    def setAddress(self, address):
        """Set the address of the person."""
        self._address = address
    def getAddress(self):
        """Return the address of the person."""
        return self._address

    def setContactDetails(self, contactDetails):
        """Set the contact details of the person."""
        self._contactDetails = contactDetails
    def getContactDetails(self):
        """Return the contact details of the person."""
        return self._contactDetails



class Employee(Person):
    """Represents an employee of the company."""
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth):
        """Initialize an Employee object with the given attributes."""
        self._name = name
        self._employeeID = employeeID
        self._department = department
        self._jobTitle = jobTitle
        self._basicSalary = basicSalary
        self._age = age
        self._dateOfBirth = dateOfBirth
        self.__passportDetails = None

    def setName(self, name):
        """Set the name of the employee."""
        self._name = name
    def getName(self):
        """Return the name of the employee."""
        return self._name

    def setEmployeeID(self, employeeID):
        """Set the employee ID."""
        self._employeeID = employeeID
    def getEmployeeID(self):
        """Return the employee ID."""
        return self._employeeID

    def setDepartment(self, department):
        """Set the department of the employee."""
        self._department = department
    def getDepartment(self):
        """Return the department of the employee."""
        return self._department

    def setJobTitle(self, jobTitle):
        """Set the job title of the employee."""
        self._jobTitle = jobTitle
    def getJobTitle(self):
        """Return the job title of the employee."""
        return self._jobTitle

    def setBasicSalary(self, basicSalary):
        """Set the basic salary of the employee."""
        self._basicSalary = basicSalary
    def getBasicSalary(self):
        """Return the basic salary of the employee."""
        return self._basicSalary

    def setAge(self, age):
        """Set the age of the employee."""
        self._age = age
    def getAge(self):
        """Return the age of the employee."""
        return self._age

    def setDateOfBirth(self, dateOfBirth):
        """Set the date of birth of the employee."""
        self._dateOfBirth = dateOfBirth
    def getDateOfBirth(self):
        """Return the date of birth of the employee."""
        return self._dateOfBirth

    def setPassportDetails(self, passportDetails):
        """Set the passport details of the employee."""
        self.__passportDetails = passportDetails
    def getPassportDetails(self):
        """Return the passport details of the employee."""
        return self.__passportDetails


class Client(Person):
    """Represents a client of the company."""
    def __init__(self, clientID, name, address, contactDetails, budget):
        """Initialize a Client object with the given attributes."""
        self._clientID = clientID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails
        self._budget = budget

    def setClientID(self, clientID):
        """Set the client ID."""
        self._clientID = clientID
    def getClientID(self):
        """Return the client ID."""
        return self._clientID

    def setName(self, name):
        """Set the name of the client."""
        self._name = name
    def getName(self):
        """Return the name of the client."""
        return self._name

    def setAddress(self, address):
        """Set the address of the client."""
        self._address = address
    def getAddress(self):
        """Return the address of the client."""
        return self._address

    def setContactDetails(self, contactDetails):
        """Set the contact details of the client."""
        self._contactDetails = contactDetails
    def getContactDetails(self):
        """Return the contact details of the client."""
        return self._contactDetails

    def setBudget(self, budget):
        """Set the budget of the client."""
        self._budget = budget
    def getBudget(self):
        """Return the budget of the client."""
        return self._budget


class Guest(Person):
    """Represents a guest attending an event."""
    def __init__(self, guestID, guestName, guestContact, guestEmail, guestAddress):
        """Initialize a Guest object with the given attributes."""
        self._guestID = guestID
        self._guestName = guestName
        self._guestContact = guestContact
        self._guestEmail = guestEmail
        self._guestAddress = guestAddress

    def setGuestID(self, guestID):
        """Set the guest ID."""
        self._guestID = guestID
    def getGuestID(self):
        """Return the guest ID."""
        return self._guestID

    def setGuestName(self, guestName):
        """Set the name of the guest."""
        self._name = guestName
    def getGuestName(self):
        """Return the name of the guest name."""
        return self._guestName

    def setGuestContact(self, guestContact):
        """Set the name of the guest contact number."""
        self._guestContact = guestContact
    def getGuestContact(self):
        """Return the name of the guest contact number."""
        return self._guestContact

    def setGuestEmail(self, guestEmail):
        """Set the address of the guest email."""
        self._guestEmail = guestEmail
    def getGuestEmail(self):
        """Return the address of the guest email."""
        return self._guestEmail

    def setGuestAddress(self, guestAddress):
        """Set the contact details of the guest address."""
        self._guestAddress = guestAddress
    def getGuestAddress(self):
        """Return the contact details of the guest address."""
        return self._guestAddress


class Supplier(Person):
    """Represents a supplier providing services or goods for events."""

    def __init__(self, supplierID, name, address, contactDetails):
        """Initialize a Supplier object with the given attributes."""
        self._supplierID = supplierID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails

    def setSupplierID(self, supplierID):
        """Set the supplier ID."""
        self._supplierID = supplierID
    def getSupplierID(self):
        """Return the supplier ID."""
        return self._supplierID

    def setName(self, name):
        """Set the name of the supplier."""
        self._name = name
    def getName(self):
        """Return the name of the supplier."""
        return self._name

    def setAddress(self, address):
        """Set the address of the supplier."""
        self._address = address
    def getAddress(self):
        """Return the address of the supplier."""
        return self._address

    def setContactDetails(self, contactDetails):
        """Set the contact details of the supplier."""
        self._contactDetails = contactDetails
    def getContactDetails(self):
        """Return the contact details of the supplier."""
        return self._contactDetails




