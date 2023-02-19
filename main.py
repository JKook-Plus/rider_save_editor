from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import qdarkstyle
import xml.etree.ElementTree as ET
import json
import sys
from ppadb.client import Client as AdbClient
from html import escape



class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.setWindowTitle("Rider Save editor")
        self.resize(720, 480)
        self.setupADB()
        self.initUI()
        self.json_to_be = None
    
        self.editing_json_filename = "current_save.json"
        
        
    def setupADB(self):
        # 127.0.0.1:5037 is the default for ADB
        self.client = AdbClient(host="127.0.0.1", port=5037)
        devices = self.client.devices()
        self.device = devices[0]
        print("Connected to: {0}".format(self.device.serial))
        print("ADB Version of device: {0}".format(self.client.version()))

    def initUI(self): 
        full_pull_button = QPushButton('Full Pull', self)
        full_pull_button.setToolTip('Force closes Rider\nPulls file from data folder to PC using ADB')
        full_pull_button.move(10,10)
        full_pull_button.clicked.connect(self.full_pull_data)

        full_push_button = QPushButton('Full Push', self)
        full_push_button.setToolTip('Force closes Rider\nPushes file from PC to data folder using ADB')
        full_push_button.move(10,50)
        full_push_button.clicked.connect(self.full_push_data)

        pull_without_kill_button = QPushButton('Full Pull (without kill)', self)
        pull_without_kill_button.setToolTip('Full pull without killing')
        pull_without_kill_button.move(120,10)
        pull_without_kill_button.clicked.connect(self.pull_without_kill)

        

        pull_button = QPushButton('Pull', self)
        pull_button.setToolTip('Pulls file from android device using ADB')
        pull_button.move(610,10)
        pull_button.clicked.connect(self.pull_data)

        push_button = QPushButton('Push', self)
        push_button.setToolTip('Pushes file from android device using ADB')
        push_button.move(610,50)
        push_button.clicked.connect(self.push_data)

        understand = QPushButton('Extract', self)
        understand.setToolTip('Gets all the data from the com.ketchapp.rider_preferences.xml file')
        understand.move(610,90)
        understand.clicked.connect(self.understand)

        save = QPushButton('Save', self)
        save.setToolTip('Save the info as editing_1.json')
        save.move(610,130)
        save.clicked.connect(self.save)

        compress = QPushButton('Compress', self)
        compress.setToolTip('Remakes the com.ketchapp.rider_preferences.xml file')
        compress.move(610,170)
        compress.clicked.connect(self.compress)

    @pyqtSlot()
    def kill_rider(self):
        # cat data/data/com.ketchapp.rider/shared_prefs/com.ketchapp.rider_preferences.xml > /storage/self/primary/Documents/com.ketchapp.rider_preferences.xml &&
    
        print(self.device.shell("su -c 'am force-stop com.ketchapp.rider'"))
        print("Force stoped Rider")

        print(self.device.shell("su -c 'rm -rf /data/data/com.ketchapp.rider/cache*'"))
        print("Removed all files from cache folder")

        # print("ls")
        # print(self.device.shell("su -c 'ls /data/data/com.ketchapp.rider/cache*'"))


    def start_rider(self):
        self.device.shell("monkey -p com.ketchapp.rider 1")
    

    def pull_data(self):
        # It moves it to docuements because adb cannot pull directly from data/* directories
        self.device.shell("su -c 'cat data/data/com.ketchapp.rider/shared_prefs/com.ketchapp.rider_preferences.xml > /storage/self/primary/Documents/com.ketchapp.rider_preferences.xml'")
        self.device.pull("/storage/emulated/0/Documents/com.ketchapp.rider_preferences.xml", "com.ketchapp.rider_preferences.xml")
        print("Pulled: com.ketchapp.rider_preferences.xml")

    def pull_without_kill(self):
        self.pull_data()
        self.understand()
        self.save()
    
    def full_pull_data(self):
        self.kill_rider()
        self.pull_data()
        self.understand()
        self.save()
    
    def full_push_data(self):
        self.kill_rider()
        self.compress()
        self.push_data()
        self.start_rider()
        
        
    
    def push_data(self):
        self.device.push("com.ketchapp.rider_preferences.xml", "/storage/emulated/0/Documents/com.ketchapp.rider_preferences.xml")
        self.device.shell("su -c 'cat /storage/self/primary/Documents/com.ketchapp.rider_preferences.xml > data/data/com.ketchapp.rider/shared_prefs/com.ketchapp.rider_preferences.xml'")
        print("Pushed com.ketchapp.rider_preferences.xml")
        self.device.shell("su -c 'rm data/data/com.ketchapp.rider/shared_prefs/com.ketchapp.rider.v2.playerprefs.xml'")
        print("Deleted: com.ketchapp.rider.v2.playerprefs.xml")
        self.device.shell("su -c 'rm data/data/com.ketchapp.rider/shared_prefs/com.ketchapp.rider.promotion.xml'")
        print("Deleted: com.ketchapp.rider.promotion.xml")
        print("Pushed: com.ketchapp.rider_preferences.xml")
    
    def understand(self):
        tree = ET.parse('com.ketchapp.rider_preferences.xml')
        root = tree.getroot()
        for child in root:
            if child.tag == "string":
                if child.attrib["name"] == "systemOptions":
                    self.json_to_be = child.text
                    # print(json_to_be)
                    
        print("understand")
    
    def save(self):
        if (self.json_to_be != None):
            with open(self.editing_json_filename, 'w') as file:
                file.write(self.json_to_be)
                # parsed = json.loads(str(json_to_be))
                # file.write(json.dumps(parsed, indent=4))

            with open(self.editing_json_filename, 'r') as file:
                parsed = json.load(file)
                out = json.dumps(parsed, indent=4)
            
            with open(self.editing_json_filename, 'w') as file:
                file.write(out)
            
            print("saved")

        else:
            print("Did not save as Json has not been loaded")
    


    def compress(self):
        with open(self.editing_json_filename, 'r') as file:
            data_from_json_file = file.read()

        if data_from_json_file != "":
            tree = ET.parse('com.ketchapp.rider_preferences.xml')
            root = tree.getroot()
            
            for elem in root:
                if elem.get("name") == "systemOptions":
                    elem.text = data_from_json_file
                    print("Found")

            tree.write('com.ketchapp.rider_preferences.xml')
            print("compressed")
        else:
            print("did not save as {0} is empty".format(self.editing_json_filename))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())