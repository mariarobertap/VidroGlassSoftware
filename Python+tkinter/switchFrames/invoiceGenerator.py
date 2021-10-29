import os

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

from InvoiceGenerator.pdf import SimpleInvoice
# choosing English as the document language

os.environ["INVOICE_LANG"] = "en"

client = Client('Client company')

provider = Provider('STechies', bank_account='6454-6361-217273', bank_code='2021')

creator = Creator('Karl Iris')

invoice = Invoice(client, provider, creator)

invoice.add_item(Item(26, 780, description="Milk"))

invoice.add_item(Item(14, 460, description="Fruits"))

invoice.add_item(Item(10, 290, description="Nuts"))

invoice.add_item(Item(3, 165, description="Biscuits"))

invoice.currency = "Rs."

invoice.number = "10393069"

docu = SimpleInvoice(invoice)

#docu.gen("invoice2.pdf", generate_qr_code=False) #you can put QR code by setting the #qr_code parameter to ‘True’