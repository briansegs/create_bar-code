"Bar Code Creator Class"
import json
from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter

class BarcodeCreator:
    "Creates barcodes and saves them to a local folder"
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        file.close()
    folder = data["folder_path"]

    def __init__(self, prefix="101"):
        self.prefix = prefix
        self.numStr = ""

    def setPrefix(self, prefixNum):
        "sets the prefix variable with parameter"
        self.prefix = prefixNum

    def setRandomNumStr(self):
        "sets the numStr variable with a random 13 digit number"
        self.numStr = str(randint(1000000000000, 9999999999999))

    def setPrefixNumStr(self):
        "sets the numStr variable with a 3 digit prefix plus a random 10 digit number"
        self.numStr = self.prefix + str(randint(1000000000, 9999999999))

    def setCustomNumStr(self, customNum):
        "sets the numStr variable with a parameter"
        self.numStr = customNum

    def saveBarcode(self):
        "saves the barcode to a local folder"
        barCode = EAN13(self.numStr, writer=ImageWriter())
        barCode.save(self.folder + "/" + str(barCode))
        print(f'Created bar-code: {barCode} in {self.folder}')
