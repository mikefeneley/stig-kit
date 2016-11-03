from subprocess import call

from mac_network_logger import MacNetworkLogger

class MacNetworkAuditor:
    """
    Check the network system configuartion of the operating system
    to see if any aspect of the setup violates the requirements of the 
    DIA Mac 10.11 STIG.

	TODO:
		Pipe cannot be used in call funciton. Either parse entire output 
		or set up pipes.

    """
    def __init__(self, holder_filename = "holder.txt"):
        self.holder_filename = holder_filename

    def audit(self):
        logger = MacNetworkLogger()
        result = self.remote_shell_disabled()
        logger.remote_shell_disabled_errmsg(result)
        result = self.screen_sharing_disabled()
        logger.screen_sharing_disabled_errmsg(result)
        result = self.bluetooth_driver_disabled()
        logger.bluetooth_driver_disabled_errmsg(result)
        result = self.wifi_support_software_disabled()
        logger.wifi_support_software_disabled_errmsg(result)
        filename = logger.get_filename()
        del logger
        return filename

    def remote_shell_disabled(self):
        """
        Check SV-81981r1_rule: The rshd service must be disabled.

        Finding ID: V-67491

        :returns: bool -- True if criteria is met, False otherwise

        TODO
        	Set up pipe correctly or line parsing.
        """
        holder_info = open(self.holder_filename, "w")
        call(["/usr/bin/sudo", "/bin/launchctl", "print-disabled", "system", "|"
				"/usr/bin/grep", "com.apple.rshd"], stdout=holder_info)
        holder_info.close()
        holder_info = open(self.holder_filename, "r")

        disabled = False
        for line in holder_info:
            if '"com.apple.rshd" => true' in line:
                disabled = True

        holder_info.close()
        return disabled


    def screen_sharing_disabled(self):
        """
        Check SV-81983r1_rule: The operating system must enforce requirements 
        for remote connections to the information system.

        Finding ID: V-67493

        :returns: bool -- True if criteria is met, False otherwise

        TODO
        	Set up pipe correctly or line parsing.
        """
        holder_info = open(self.holder_filename, "w")
        call(["/usr/bin/sudo", "/bin/launchctl", "print-disabled", "system", 
			"|", "/usr/bin/grep", "com.apple.screensharing"], 
			stdout=holder_info)
        holder_info.close()
        holder_info = open(self.holder_filename, "r")

        disabled = False
        for line in holder_info:
		if '"com.apple.screensharing" => true' in line:
			disabled = True
        holder_info.close()
        return disabled

    def bluetooth_driver_disabled(self):
        """ 
        Check SV-81985r1_rule: The Bluetooth software driver must be disabled.

        Finding ID: V-67495

        :returns: bool -- True if criteria is met, False otherwise

        TODO
        	Set up pipe correctly or line parsing.
        """
        holder_info = open(self.holder_filename, "w")
        call(["/usr/sbin/system_profiler", "SPConfigurationProfileDataType",
			"|", "system", "|", "/usr/bin/grep", "DisableBluetooth"],
			stdout=holder_info)
        holder_info.close()
        holder_info = open(self.holder_filename, "r")

        disabled = False
        for line in holder_info:
		if "DisableBluetooth 1" in line:
			disabled = True

        return disabled

    def wifi_support_software_disabled(self):
        """
        Check SV-81987r1_rule: Wi-Fi support software must be disabled.

        Finding ID: V-67497

        :returns: bool -- True if criteria is met, False otherwise
        """	
        holder_info = open(self.holder_filename, "w")
        call(["/usr/bin/sudo", "/usr/sbin/networksetup",
		"-listallnetworkservices"], stdout=holder_info)
        holder_info.close()
        holder_info = open(self.holder_filename, "r")

        disabled = False
        for line in holder_info:
            if "*Wi-Fi" in line:
        	    disabled = True

        holder_info.close()
        return disabled


if __name__ == "__main__":
	print("START")
	auditor = MacNetworkAuditor()
	auditor.audit()
	print("End")
