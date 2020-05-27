import unittest
from Customer import Customer
from Items import Items

class CustomerTest(unittest,TestCase):
    def setUp(self):
        self.Customer=Customer('001','123,4567','James','John')

    def test_CustomerString(self):
        self.assertEqual(str(self.Customer),self.Customer.LastName)

    def test_getPhone(self):
        self.assertEqual(str(self.Customer.getPhone()),'123,4567')
    
    def test_getFirstName(self):
        self.assertEqual(str(self.Customer.getFirstName()),'John')
    
    def test_getCustomerID(self):
        self.assertEqual(str(self.Customer.getCustomerID()),'001')

class ItemsTest(unittest,TestCase):
    def setUp(self):
        self.item=Items(1,'12.95','Beer','Coors','Molson')

    def test_ItemsString(self):
        self.assertEqual(str(self.Items.Description))

    def test_getPrice(self):
        self.assertEqual(str(self.Items.getPrice()), '12.95')

    def test_getItemNumber(self):
        self.assertEqual(str(self.Items.getItemNumber()),'1')

    def test_getDescription(self):
        self.assertEqual(str(self.Items.Description()),'Coors')
    
    def test_getManufacturer(self):
        self.assertEqual(str(self.Items.Manufacturer()),'Molson')

    
