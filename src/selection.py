import sys

sys.path.append('./stig-jre/src/')
sys.path.append("./stig-apache/src/")

from jre_auditor import JREAuditor
from apache_auditor import ApacheAuditor
from Tkinter import *



class Selection:
    def __init__(self):

        self.jre_audit = JREAuditor()
        self.apache_audit = ApacheAuditor()
        master = Tk()

        self.run_jre = IntVar()
        self.run_apache = IntVar()

        self.jre_button = Checkbutton(master, text="Jave Runtime Environment", variable=self.run_jre)
        self.jre_button.pack()
        self.apache_button = Checkbutton(master, text="Apache Server", variable=self.run_apache)
        self.apache_button.pack()
                
        self.run_button = Button(master, text="Run", command=self.run)
        self.run_button.pack()

        while(1):
            master.update()

    def run(self):
        print(self.run_jre.get(), self.run_apache.get())
        if self.run_jre:
            self.jre_audit.audit()
        if self.run_apache:
            self.apache_audit.audit()


if __name__ == '__main__':
    selection = Selection()
        
