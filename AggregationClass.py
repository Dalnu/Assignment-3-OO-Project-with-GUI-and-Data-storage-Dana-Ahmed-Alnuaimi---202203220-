from InheritanceClass import *
# Importing required classes or modules. 

class Guest(Person):
    """Represents a guest attending an event."""
    def __init__(self, guestID, guestName, guestContact, guestEmail, guestAddress):
        """Initialize a Guest object with the given attributes."""
        # Initialize attributes
        self._guestID = guestID
        self._guestName = guestName
        self._guestContact = guestContact
        self._guestEmail = guestEmail
        self._guestAddress = guestAddress

    # Getter and setter methods for each attribute

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


class Event:
# Defines a class `Event`.

    """Represents an event organized by the company."""
    # Docstring describing the purpose of the `Event` class.

    def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        """Initialize an Event object with the given attributes."""
        # Constructor method to initialize an `Event` object with specific attributes.

    # Getters
    # Methods to get the values of attributes.

    def getEventID(self):
        """Return the ID of the event."""
        # Method to return the ID of the event.

    def getType(self):
        """Return the type of the event."""
        # Method to return the type of the event.

    def getTheme(self):
        """Return the theme of the event."""
        # Method to return the theme of the event.

    def getDate(self):
        """Return the date of the event."""
        # Method to return the date of the event.

    def getTime(self):
        """Return the time of the event."""
        # Method to return the time of the event.

    def getDuration(self):
        """Return the duration of the event."""
        # Method to return the duration of the event.

    def getVenueAddress(self):
        """Return the address of the event venue."""
        # Method to return the address of the event venue.

    def getClientID(self):
        """Return the ID of the client."""
        # Method to return the ID of the client.

    def getGuestList(self):
        """Return the guest list for the event."""
        # Method to return the guest list for the event.

    def getCateringCompany(self):
        """Return the catering company for the event."""
        # Method to return the catering company for the event.

    def getCleaningCompany(self):
        """Return the cleaning company for the event."""
        # Method to return the cleaning company for the event.

    def getDecorationsCompany(self):
        """Return the decorations company for the event."""
        # Method to return the decorations company for the event.

    def getEntertainmentCompany(self):
        """Return the entertainment company for the event."""
        # Method to return the entertainment company for the event.

    def getFurnitureSupplyCompany(self):
        """Return the furniture supply company for the event."""
        # Method to return the furniture supply company for the event.

    def getInvoice(self):
        """Return the invoice for the event."""
        # Method to return the invoice for the event.

    # Setters
    # Methods to set the values of attributes.

    def setEventID(self, eventID):
        """Set the ID of the event."""
        # Method to set the ID of the event.

    def setType(self, type):
        """Set the type of the event."""
        # Method to set the type of the event.

    def setTheme(self, theme):
        """Set the theme of the event."""
        # Method to set the theme of the event.

    def setDate(self, date):
        """Set the date of the event."""
        # Method to set the date of the event.

    def setTime(self, time):
        """Set the time of the event."""
        # Method to set the time of the event.

    def setDuration(self, duration):
        """Set the duration of the event."""
        # Method to set the duration of the event.

    def setVenueAddress(self, venueAddress):
        """Set the address of the event venue."""
        # Method to set the address of the event venue.

    def setClientID(self, clientID):
        """Set the ID of the client."""
        # Method to set the ID of the client.

    def setGuestList(self, guestList):
        """Set the guest list for the event."""
        # Method to set the guest list for the event.

    def setCateringCompany(self, cateringCompany):
        """Set the catering company for the event."""
        # Method to set the catering company for the event.

    def setCleaningCompany(self, cleaningCompany):
        """Set the cleaning company for the event."""
        # Method to set the cleaning company for the event.

    def setDecorationsCompany(self, decorationsCompany):
        """Set the decorations company for the event."""
        # Method to set the decorations company for the event.

    def setEntertainmentCompany(self, entertainmentCompany):
        """Set the entertainment company for the event."""
        # Method to set the entertainment company for the event.

    def setFurnitureSupplyCompany(self, furnitureSupplyCompany):
        """Set the furniture supply company for the event."""
        # Method to set the furniture supply company for the event.

    def setInvoice(self, invoice):
        """Set the invoice for the event."""
        # Method to set the invoice for the event.


class Supplier(Person):
    """Represents a supplier providing services or goods for events."""
    def __init__(self, supplierID, name, address, contactDetails):
        """Initialize a Supplier object with the given attributes."""
        # Initialize attributes
        self._supplierID = supplierID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails

    # Getter and setter methods for each attribute

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


class Venue:
    """Represents a venue where events are hosted."""
    
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        """Initialize a Venue object with the given attributes."""
        # Initialize attributes
        self._venueID = venueID
        self._name = name
        self._address = address
        self._contact = contact
        self._minGuests = minGuests
        self._maxGuests = maxGuests

    # Getters
    # Define getter methods for each attribute
    def getVenueID(self):
        """Return the venue ID."""
        return self._venueID

    def getName(self):
        """Return the name of the venue."""
        return self._name

    def getAddress(self):
        """Return the address of the venue."""
        return self._address

    def getContact(self):
        """Return the contact details of the venue."""
        return self._contact

    def getMinGuests(self):
        """Return the minimum number of guests allowed at the venue."""
        return self._minGuests

    def getMaxGuests(self):
        """Return the maximum number of guests allowed at the venue."""
        return self._maxGuests

    # Setters
    # Define setter methods for each attribute
        def setVenueID(self, venueID):
        """Set the venue ID."""
        self._venueID = venueID

    def setName(self, name):
        """Set the name of the venue."""
        self._name = name

    def setAddress(self, address):
        """Set the address of the venue."""
        self._address = address

    def setContact(self, contact):
        """Set the contact details of the venue."""
        self._contact = contact

    def setMinGuests(self, minGuests):
        """Set the minimum number of guests allowed at the venue."""
        self._minGuests = minGuests

    def setMaxGuests(self, maxGuests):
        """Set the maximum number of guests allowed at the venue."""
        self._maxGuests = maxGuests
