import sys

sys.path.append('./stig-jre/src/')
sys.path.append("./stig-apache/src/")
sys.path.append("./stig-windows10/src/")
from jre_auditor import JREAuditor
from apache_auditor import ApacheAuditor
from windows10_auditor import Windows10Auditor
from Tkinter import *

LOG_FILENAME = "Results.txt"


class Selection:

    def __init__(self):

        self.jre_audit = JREAuditor()
        self.apache_audit = ApacheAuditor()
        self.windows10_audit = Windows10Auditor()
        self.master = Tk()

        self.run_jre = IntVar()
        self.run_apache = IntVar()
        self.run_windows10 = IntVar()

        self.windows_button = Checkbutton(
            self.master, text="Windows 10", variable=self.run_windows10)
        self.windows_button.pack()

        self.jre_button = Checkbutton(
            self.master, text="Jave Runtime Environment", variable=self.run_jre)
        self.jre_button.pack()

        self.apache_button = Checkbutton(
            self.master, text="Apache Server", variable=self.run_apache)
        self.apache_button.pack()

        self.run_button = Button(self.master, text="Run", command=self.run)
        self.run_button.pack()

        self.exit_button = Button(self.master, text="Exit", command=self.exit)
        self.exit_button.pack()

        while(1):
            self.master.update()

    def run(self):

        logs = []

        if self.run_jre.get() == 1:
            log = self.jre_audit.audit()
            logs.append(log)
        if self.run_apache.get() == 1:
            log = self.apache_audit.audit()
            logs.append(log)
        if self.run_windows10.get() == 1:
            log = self.windows10_audit.audit()
            logs.append(log)
        self.build_output(logs)

    def exit(self):
        del self.jre_audit
        del self.apache_audit
        del self.master
        quit()

    def build_output(self, logs, out_log=LOG_FILENAME):
        """
        Concatenates all the log files in files list into single file
        with name filename.

        :returns: string -- filename of the log file
        """
        out_log = open(out_log, 'w')
        out_log.write("AUDIT RESULTS\n\n")

        for log in logs:
            self.copy(log, out_log)
        out_log.close()

    def copy(self, input, output):
        """
        Copy the data from file input into file output
        """
        in_log = open(input, 'r')
        for line in in_log:
            output.write(line)
        in_log.close()

if __name__ == '__main__':
    selection = Selection()
