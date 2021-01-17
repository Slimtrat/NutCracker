import select

import bluetooth


class MyDiscoverer(bluetooth.DeviceDiscoverer):

    def pre_inquiry(self):
        self.done = False

    def device_discovered(self, address, device_class, rssi, name):
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

        for bitpos, classname in service_classes:
            if device_class & (1 << (bitpos-1)):
                print("   ", classname)
        print("  RSSI:", rssi)

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
