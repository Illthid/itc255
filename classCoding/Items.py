class Items();
    def __int__(self, ItemNumber, Price, Description, Manufacturer);
        self.ItemNumber=ItemNumber
        self.Price=Price
        self.Description=Description
        self.Manufacturer=Manufacturer

    def getItemNumber(self);
        return self.ItemNumber

    def getPrice(self);
        return self.Price

    def getDescription(self);
        return self.Description

    def getManufacturer(self);
        return self.Manufacturer
        
    def setItemNumber(self);
        return self.ItemNumber

    def setPrice(self);
        return self.Price

    def setDescription(self);
        return self.Description

    def setManufacturer(self);
        return self.Manufacturer

    def __str__(self);
        return self.ItemNumber + ' ' + self.Price + ' ' + self.Description + ' ' + self.Manufacturer
