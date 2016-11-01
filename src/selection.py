import sys

sys.path.append('./stig-jre/src/')
sys.path.append("./stig-apache/src/")

from jre_auditor import JREAuditor
from apache_auditor import ApacheAuditor
from Tkinter import *

LOG_FILENAME = "Results.txt"

class Selection:
    def __init__(self):

        self.jre_audit = JREAuditor()
        self.apache_audit = ApacheAuditor()
        self.master = Tk()

        self.run_jre = IntVar()
        self.run_apache = IntVar()

        self.jre_button = Checkbutton(self.master, text="Jave Runtime Environment", variable=self.run_jre)
        self.jre_button.pack()
        
        self.apache_button = Checkbutton(self.master, text="Apache Server", variable=self.run_apache)
        self.apache_button.pack()
                
        self.run_button = Button(self.master, text="Run", command=self.run)
        self.run_button.pack()
        
        self.exit_button = Button(self.master, text="Exit", command=self.exit)
        self.exit_button.pack()
        
        while(1):
            self.master.update()

    def run(self):
        print(self.run_jre.get(), self.run_apache.get())
        if self.run_jre.get() == 1:
            self.jre_audit.audit()
        if self.run_apache.get() == 1:
            self.apache_audit.audit()

        self.build_output()
        
    def exit(self):
        del self.jre_audit
        del self.apache_audit
        del self.master
        quit()

    def build_output(self):
        out_log = open(LOG_FILENAME, 'w')
        out_log.write("AUDIT RESULTS")

        if self.run_jre.get() == 1:
            in_log = open("JRELog.txt", 'r')
            self.copy(in_log, out_log)
        if self.run_apache.get() == 1:
            in_log = open("ApacheConfigLog.txt")
            self.copy(in_log, out_log)
        out_log.close()

    def copy(self, input, output):
        for line in input:
            output.write(line)
        input.close()

if __name__ == '__main__':
    selection = Selection()
        
