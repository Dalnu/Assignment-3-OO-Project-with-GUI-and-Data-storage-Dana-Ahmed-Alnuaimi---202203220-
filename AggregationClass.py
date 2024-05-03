from InheritanceClass import *

class Client(Person):
    """Represents a client of the company."""

    def __init__(self, clientID, name, address, contactDetails, budget):
        """Initialize a Client object with the given attributes."""
        self._clientID = clientID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails
        self._budget = budget

    # Getters
    def getClientID(self):
        """Return the client ID."""
        return self._clientID

    def getName(self):
        """Return the name of the client."""
        return self._name

    def getAddress(self):
        """Return the address of the client."""
        return self._address

    def getContactDetails(self):
        """Return the contact details of the client."""
        return self._contactDetails

    def getBudget(self):
        """Return the budget of the client."""
        return self._budget

    # Setters
    def setClientID(self, clientID):
        """Set the client ID."""
        self._clientID = clientID

    def setName(self, name):
        """Set the name of the client."""
        self._name = name

    def setAddress(self, address):
        """Set the address of the client."""
        self._address = address

    def setContactDetails(self, contactDetails):
        """Set the contact details of the client."""
        self._contactDetails = contactDetails

    def setBudget(self, budget):
        """Set the budget of the client."""
        self._budget = budget

class Event:
    """Represents an event organized by the company."""

    def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        """Initialize an Event object with the given attributes."""
        self._eventID = eventID
        self._type = type
        self._theme = theme
        self._date = date
        self._time = time
        self._duration = duration
        self._venueAddress = venueAddress
        self._clientID = clientID
        self._guestList = []
        self._cateringCompany = cateringCompany
        self._cleaningCompany = cleaningCompany
        self._decorationsCompany = decorationsCompany
        self._entertainmentCompany = entertainmentCompany
        self._furnitureSupplyCompany = furnitureSupplyCompany
        self._invoice = invoice

    # Getters
    def getEventID(self):
        """Return the ID of the event."""
        return self._eventID

    def getType(self):
        """Return the type of the event."""
        return self._type

    def getTheme(self):
        """Return the theme of the event."""
        return self._theme

    def getDate(self):
        """Return the date of the event."""
        return self._date

    def getTime(self):
        """Return the time of the event."""
        return self._time

    def getDuration(self):
        """Return the duration of the event."""
        return self._duration

    def getVenueAddress(self):
        """Return the address of the event venue."""
        return self._venueAddress

    def getClientID(self):
        """Return the ID of the client."""
        return self._clientID

    def getGuestList(self):
        """Return the guest list for the event."""
        return self._guestList

    def getCateringCompany(self):
        """Return the catering company for the event."""
        return self._cateringCompany

    def getCleaningCompany(self):
        """Return the cleaning company for the event."""
        return self._cleaningCompany

    def getDecorationsCompany(self):
        """Return the decorations company for the event."""
        return self._decorationsCompany

    def getEntertainmentCompany(self):
        """Return the entertainment company for the event."""
        return self._entertainmentCompany

    def getFurnitureSupplyCompany(self):
        """Return the furniture supply company for the event."""
        return self._furnitureSupplyCompany

    def getInvoice(self):
        """Return the invoice for the event."""
        return self._invoice

    # Setters
    def setEventID(self, eventID):
        """Set the ID of the event."""
        self._eventID = eventID

    def setType(self, type):
        """Set the type of the event."""
        self._type = type

    def setTheme(self, theme):
        """Set the theme of the event."""
        self._theme = theme

    def setDate(self, date):
        """Set the date of the event."""
        self._date = date

    def setTime(self, time):
        """Set the time of the event."""
        self._time = time

    def setDuration(self, duration):
        """Set the duration of the event."""
        self._duration = duration

    def setVenueAddress(self, venueAddress):
        """Set the address of the event venue."""
        self._venueAddress = venueAddress

    def setClientID(self, clientID):
        """Set the ID of the client."""
        self._clientID = clientID

    def setGuestList(self, guestList):
        """Set the guest list for the event."""
        self._guestList = guestList

    def setCateringCompany(self, cateringCompany):
        """Set the catering company for the event."""
        self._cateringCompany = cateringCompany

    def setCleaningCompany(self, cleaningCompany):
        """Set the cleaning company for the event."""
        self._cleaningCompany = cleaningCompany

    def setDecorationsCompany(self, decorationsCompany):
        """Set the decorations company for the event."""
        self._decorationsCompany = decorationsCompany

    def setEntertainmentCompany(self, entertainmentCompany):
        """Set the entertainment company for the event."""
        self._entertainmentCompany = entertainmentCompany

    def setFurnitureSupplyCompany(self, furnitureSupplyCompany):
        """Set the furniture supply company for the event."""
        self._furnitureSupplyCompany = furnitureSupplyCompany

    def setInvoice(self, invoice):
        """Set the invoice for the event."""
        self._invoice = invoice
