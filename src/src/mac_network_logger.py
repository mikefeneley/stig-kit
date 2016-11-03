class MacNetworkLogger:
    """
    MacNetworkLogger writes error messages to the mac network log file
    for mac network rule in the Apache STIG that is violated
    """
    def __init__(self, filename="MacNetworkLog.txt"):
        self.filename = filename
        self.log = open(filename, 'w')
        self.log.write("#########################\n\n")
        self.log.write("Mac Network Audit Findings\n\n")
    
    def __del__(self):
        self.log.write("#########################\n\n")
        self.log.close()

    def get_filename(self):
        return self.filename

    def remote_shell_disabled_errmsg(self, result):
        if result == 0:
            self.log.write("Check SV-81981r1_rule: ")
            self.log.write("The rshd service must be disabled.\n\n")
            self.log.write("To fix: ")
            self.log.write("To disable the rshd service, run the following command: /usr/bin/sudo /bin/launchctl disable system/com.apple.rshd.\n\n\n")
    
    def screen_sharing_disabled_errmsg(self, result):
        if result == 0:
            self.log.write("Check SV-81983r1_rule: ")
            self.log.write(" The operating system must enforce requirements for remote connections to the information system.\n\n")
            self.log.write("To fix: ")
            self.log.write("Screen Sharing service, run the following command: /usr/bin/sudo /bin/launchctl disable system/com.apple.screensharing\n\n\n")
    
    def bluetooth_driver_disabled_errmsg(self, result):
        if result == 0:
            self.log.write("Check SV-81985r1_rule: ")
            self.log.write("The Bluetooth software driver must be disabled.\n\n")
            self.log.write("To fix: ")
            self.log.write(" This setting is enforced using the Bluetooth Policy configuration profile. \n\n\n")
    
    def wifi_support_software_disabled_errmsg(self, result):
        if result == 0:
            self.log.write("Check SV-81987r1_rule: ")
            self.log.write("Wi-Fi support software must be disabled.\n\n")
            self.log.write("To fix: ")
            self.log.write('To disable the Wi-Fi network device, run the following command: /usr/bin/sudo /usr/sbin/networksetup -setnetworkserviceenabled "Wi-Fi" off \n\n\n')