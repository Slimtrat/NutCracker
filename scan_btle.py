import select

import bluetooth


class MyDiscoverer(bluetooth.DeviceDiscoverer):

    def pre_inquiry(self):
        self.done = False
        self.devices=[]

    def device_discovered(self, address, device_class, rssi, name):
        sortie=[]
        sortie.append(address)
        sortie.append(name)
        print("{} - {}".format(address, name))
        major_classes = ("Miscellaneous",
                         "Computer",
                         "Phone",
                         "LAN/Network Access Point",
                         "Audio/Video",
                         "Peripheral",
                         "Imaging")
        major_class = (device_class >> 8) & 0xf
        if major_class < 7:
            print(" " + major_classes[major_class])
        else:
            print("  Uncategorized")
        print("  Services:")
        service_classes = ((16, "positioning"),
                           (17, "networking"),
                           (18, "rendering"),
                           (19, "capturing"),
                           (20, "object transfer"),
                           (21, "audio"),
                           (22, "telephony"),
                           (23, "information"))
        temp=[]
        for bitpos, classname in service_classes:
            if device_class & (1 << (bitpos-1)):
                print("   ", classname)
                temp.append(classname)
        sortie.append(temp)

        print("  RSSI:", rssi)
        sortie.append(rssi)
	if not sortie==[]:
            devices.append(sortie)

    def inquiry_complete(self):
        self.done = True


d = MyDiscoverer()
d.find_devices(lookup_names=True)

readfiles = [d, ]

while True:
    rfds = select.select(readfiles, [], [])[0]

    if d in rfds:
        d.process_event()

    if d.done:
        break
