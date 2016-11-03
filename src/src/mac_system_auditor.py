from subprocess import call



class MacSystemAuditor:
	"""
	Check the system configuartion of the operating system
	to see if any aspect of the setup violates the requirements of the 
	DIA Mac 10.11 STIG.
	"""
    def __init__(self, holder_filename = "holder.txt"):
        self.holder_filename = holder_filename

    def audit(self):
        result = self.session_lock_enabled()

        result = self.session_lock_time_set()

        result = self.session_login_required()



    def session_lock_enabled(self):
        """
        Check SV-81951r1_rule: The operating system must conceal, via 
        the session lock, information previously visible on the 
        display with a publicly viewable image.

        Finding ID: V-67461

        :returns: bool -- True if criteria is met, False otherwise
        """
        holder_info = open(self.holder_filename, "w")

        call(["/usr/sbin/system_profiler", "SPConfigurationProfileDataType" "|"
        			"/usr/bin/grep moduleName"], stdout=holder_info)
        holder_info.close()

        holder_info = open(self.holder_filename, "r")

        enabled = False
        for line in holder_info:
        	if "moduleName" in line:
        		enabled = True
        holder_info.close()
        return enabled


    def session_lock_time_set(self):
    	"""
        Check SV-81953r1_rule: The operating system must initiate a session 
        lock after a 15-minute period of inactivity.

        Finding ID: V-67463 CHECK TIME

        :returns: bool -- True if criteria is met, False otherwise
        """
        holder_info = open(self.holder_filename, "w")

        call(["/usr/sbin/system_profiler", "SPConfigurationProfileDataType" "|"
        			"/usr/bin/grep idleTime"], stdout=holder_info)
        holder_info.close()

        holder_info = open(self.holder_filename, "r")

        time_set = False
        for line in holder_info:
        	if "idleTime" in line:
        		time_set = True
        holder_info.close()
        return time_set


	    """
        Check RULE:

        Finding ID: ID

        :returns: bool -- True if criteria is met, False otherwise
        """	

    def session_login_required(self):
    	"""
        Check SV-81955r1_rule: The operating system must retain the 
        session lock until the user reestablishes access using established 
        identification and authentication procedures.

        Finding ID: V-67465 CHECK TIME

        :returns: bool -- True if criteria is met, False otherwise
        """    	
        holder_info = open(self.holder_filename, "w")

        call(["/usr/sbin/system_profiler", "SPConfigurationProfileDataType" "|"
        		"/usr/bin/grep askForPassword"], stdout=holder_info)
        holder_info.close()


if __name__ == "__main__":
	auditor = MacSystemAuditor()
	print("HER")
	auditor.audit()