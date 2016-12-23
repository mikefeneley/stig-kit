# stig-kit

<b>Update 11/13/2016:</b>

STIG-KIT was originally intended to be a vulnerability checker that checked application configuration against the recommendations of the STIG guides provided by the DISA. The STIG-KIT used Python implementations of each individual STIG guide to check against the STIG requirements.


According to the NISA, the best way to implement a SCAP, (Security Content Automation Protocol),  like the STIG-KIT is to use OVAL, (Open Vulnerability and Assessment Language) repository to check the vulnerabilities provided by an XCCDF, (Extensible Configuration Checklist Description Format) and report the misconfigurations back the user.


Because the approach used to start this project is outdated and the correct approach is already implemented here: https://github.com/OpenSCAP, I am no longer going to continue regular work on this project. I may continue to write new methods in my free time in order to learn about STIG requirements, but it is no longer a personal priority.


If you are interested in working on this project with me, I may be interested if you can provide a good reason to do. If so, please contact me here: mfeneley@vt.edu.


<b>Update 11/26/2016:</b>

Initially this tool was originally intended to just check and report misconfiguations back to the user. However, adding the option to change or add configurations to make the system STIG compliant might help this tool stand out from many of the other STIG tools avaliable. 

I am still going to work on extending the number of findings that are supported by the STIG Kit, but I also intend to add configuration change functitonality to the program.


<b>Overview</b>

The README files of the sub stig-checkers which describe the rules supported can be found here:


https://github.com/mikefeneley/stig-apache

https://github.com/mikefeneley/stig-windows10

https://github.com/mikefeneley/stig-jre

<b>Using the Program</b>

The program can be run using the command line. Navigate to the src folder after downloading and execute program with the following command:

<i>python selection.py</i>


<br>
<br>
<b>Contact:</b>

Michael Feneley: mfeneley(at)vt.edu
