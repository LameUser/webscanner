# webscanner

An automated tool for searching network and domain information. This tool is integrated with many reconnaissance tools in it, such as nmap, whois, ipaddress, domain check, etc. 


## Installation

1. Go to the terminal and type "pwd"
   ```sh
   pwd
   ```

2. Using "cd" command navigate and get to the directory where you want to install this tool.
   ```sh
   cd ~ 
   ```

3. Then type "git clone https://github.com/LameUser/webscanner.git" and the tool will be clonned.
   ```sh
   git clone https://github.com/LameUser/webscanner.git
   ```

4. Then navigate to the webscanner folder using "cd webscanner"
   ```sh
   cd webscanner
   ```
   
6. Once entered the folder, check the permissions of each file by using "ls -l" command.
   ```sh
   ls -l
   ```

7. Give executable permission to the main.py using the "chmod +x `main.py`" command, which will allow the file to be executed.
   ```sh
   chnod +x main.py
   ```
   
8. Now run the file using "python3 main.py" and enter the urls and ip address respectively.
   ```sh
   python3 main.py
   ```
   
9. You many need to install some dependencies if not already present.




## About the Sub-tools

### `domain_name.py`

It confirms and outputs the main domain present in the url.
"For this enter the URL"

### ip_address.py

This will do a nslookup and will prompt you the URL details.
"For this enter the URL, e.g: https://github.com "

### Main.py

The main python file which will be used to run the tool.

### nmap.py

This python tool will help you perform a nmap search for a given ip address.
"For this enter an IP address, e.g: 192.148.1.2"

### Robots_txt.py

This tool tells search engine crawlers which URLs the crawler can access on given site.
"For this enter the URL, e.g: https://github.com"

### Whois.py

This tool will let you know whom the domain belongs to and related information.
"For this enter the URL, e.g: https://github.com"
