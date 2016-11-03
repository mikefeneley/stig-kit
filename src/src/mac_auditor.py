
from mac_network_auditor import MacNetworkAuditor

class MacAuditor:
    def __init__(self):
        pass

    def audit(self):
        """
        Entry function for Mac audit. Calls functions that check
		for rule violates of the Mac STIG and combines the outputs
		into a single log file.

		
		:returns: string -- filename of the master log file
		"""
        files = []
        network_auditor = MacNetworkAuditor()

        log_filename = network_auditor.audit()
        files.append(log_filename)
        master_log = self.build_output(files)
    

    def build_output(self, files, filename = "MacLog.txt"):
    	"""
        Combine all the log files in argument files into a single
        log file called filename
    
        :param files: list of log file names
        :type files: list
        :param filename: filename of master log
        :type filename: string
        :return: filename of master log
        """
        out_log = open(filename, 'w')

        for file in files:
            in_log = open(file, 'r')
            for line in in_log:
                out_log.write(line)
            in_log.close()

        out_log.close()
        return filename


if __name__ == "__main__":
	auditor = MacAuditor()
	auditor.audit()