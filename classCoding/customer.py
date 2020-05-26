class customer();
    def __init__(self,CustomerID,Phone,LastName,FirstName);
        self.CustomerID=CustomerID
        self.Phone=Phone
        self.LastName=LastName
        self.FirstName=FirstName

    def getCustomerID(self);
        return self.CustomerID
    
    def setCustomerID(self);
        self.CustomerID=CustomerID

    def getPhone(self);
        return self.Phone

    def setPhone(self);
        self.Phone=Phone

    def getLastName(self);
        return self.LastName
    
    def setLastName(self);
        self.LastName=LastName

    def getFirstName(self);
        return self.FirstName

    def setFirstName(self);
        self.FirstName=FirstName

    def __str__(self);
        return self.CustomerID + ' ' + self.LastName + ' ' + self.FirstName + ' ' + self.Phone
