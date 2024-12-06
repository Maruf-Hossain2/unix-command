commands_by_category = {
    'most_used': [
        ('ls', 'Lists files and directories.', 'ls [options]', 'ls -l'),
        ('cd', 'Changes the current directory.', 'cd [directory]', 'cd /home'),
        ('pwd', 'Prints the current working directory.', 'pwd', 'pwd'),
        ('mkdir', 'Creates a new directory.', 'mkdir [directory]', 'mkdir mydir'),
        ('cp', 'Copies files or directories.', 'cp source destination', 'cp file1.txt file2.txt'),
        ('mv', 'Moves or renames files.', 'mv source destination', 'mv file1.txt newfile.txt'),
        ('rm', 'Removes files or directories.', 'rm [options] file', 'rm myfile.txt'),
        ('cat', 'Displays file contents.', 'cat file', 'cat myfile.txt'),
        ('grep', 'Searches for patterns in files.', 'grep pattern file', 'grep error log.txt'),
        ('ps', 'Lists running processes.', 'ps [options]', 'ps aux'),
        ('kill', 'Terminates a process.', 'kill [PID]', 'kill 1234'),  # Use cautiously!
        ('sudo', 'Executes a command with elevated privileges.', 'sudo command', 'sudo apt update'), #Use cautiously!
        ('apt update', 'Update package lists (Debian/Ubuntu)', 'apt update', 'apt update'), #Use cautiously!
    ],
    'date_time': [
        ('cal', 'Displays the current month calendar.', 'cal [options] [year]', 'cal'),
        ('cal 10 2015', 'Displays the calendar for October 2015.', 'cal month year', 'cal 10 2015'),
        ('cal 15 10 2015', 'Displays the calendar for 15-10-2015 (invalid syntax).', 'cal day month year', 'cal 15 10 2015'),
        ('cal 2015', 'Displays the calendar for 2015.', 'cal year', 'cal 2015'),
        ('date', 'Displays the current date and time.', 'date [OPTION]...', 'date'),
        ('date +%d', 'Displays the current day (01-31).', 'date +%d', 'date +%d'),
        ('date +%h', 'Displays the current month (Jan-Dec).', 'date +%h', 'date +%h'),
        ('date +%H', 'Displays the current hour (00-23).', 'date +%H', 'date +%H'),
        ('date +%M', 'Displays the current minute (00-59).', 'date +%M', 'date +%M'),
        ('date +%m', 'Displays the current month (01-12).', 'date +%m', 'date +%m'),
        ('date +%S', 'Displays the current second (00-59).', 'date +%S', 'date +%S'),
        ('date +%y', 'Displays the last two digits of the year.', 'date +%y', 'date +%y')
    ],
    'disk_management': [
        ('fdisk -l', 'List partitions', 'fdisk -l', 'fdisk -l'),
        ('mkfs.ext4 /dev/sdb1', 'Format partition as ext4', 'mkfs.ext4 device', 'mkfs.ext4 /dev/sdb1'),  # Use with extreme caution!
        ('mount /dev/sdb1 /mnt/point', 'Mount partition', 'mount device mountpoint', 'mount /dev/sdb1 /mnt/mypartition'),
        ('umount /mnt/point', 'Unmount partition', 'umount mountpoint', 'umount /mnt/mypartition')
    ],
    'file_info': [
        ('wc -c file.txt', 'Displays number of characters.', 'wc -c file', 'wc -c myfile.txt'),
        ('wc -l file.txt', 'Displays number of lines.', 'wc -l file', 'wc -l myfile.txt'),
        ('wc -w file.txt', 'Displays number of words.', 'wc -w file', 'wc -w myfile.txt'),
        ('wc file.txt', 'Displays lines, words, characters.', 'wc [option] file', 'wc myfile.txt')
    ],
    'file_manipulation': [
        ('cat file_name', 'Displays file contents.', 'cat filename', 'cat myfile.txt'),
        ('cat file1.txt file2.txt >> file3.txt', 'Appends files to file3.txt.', 'cat file1 file2 >> file3', 'cat file1.txt file2.txt >> output.txt'),
        ('cat file1.txt file2.txt > file3.txt', 'Concatenates files to file3.txt.', 'cat file1 file2 > file3', 'cat file1.txt file2.txt > output.txt'),
        ('cat >> file_name', 'Appends to a file.', 'cat >> filename', 'cat >> myfile.txt'),
        ('cat > file_name', 'Creates/overwrites a file.', 'cat > filename', 'cat > myfile.txt'),
        ('chgrp group file.txt', 'Changes file group', 'chgrp group file', 'chgrp users myfile.txt'),
        ('chown user:group file.txt', 'Changes file ownership', 'chown user:group file', 'chown john:users myfile.txt'),
        ('cp -i source destination', 'Copies with confirmation', 'cp -i source destination', 'cp -i file1.txt file2.txt'),
        ('cp -r img /path/to/destination', 'Recursively copies img.', 'cp -r source destination', 'cp -r mydir /tmp/'),
        ('cp file1.txt /path/to/destination', 'Copies file to a path.', 'cp source destination', 'cp myfile.txt /tmp/'),
        ('cp file1.txt img', 'Copies file1.txt to img.', 'cp source destination', 'cp file1.txt mydir/'),
        ('cp file1.txt newfile1.txt', 'Copies file1.txt to newfile1.txt.', 'cp source destination', 'cp myfile.txt newfile.txt'),
        ('cp file2.txt file3.txt /path/to/destination', 'Copies multiple files to a path.', 'cp file1 file2 ... destination', 'cp file1.txt file2.txt /tmp/'),
        ('dd if=input.img of=output.img bs=1M', 'Copies and converts file format', 'dd if=input of=output bs=bytes', 'dd if=/dev/zero of=empty.img bs=1M count=10'),
        ('df -h', 'Shows disk space', 'df [options]', 'df -h'),
        ('du -sh', 'Shows disk usage', 'du [options]', 'du -sh *'),
        ('find [path] [options]', 'Searches for files.', 'find [path] [options]', 'find /home -name "*.txt"'),
        ('gzip file.txt', 'Compresses file', 'gzip [options] file', 'gzip myfile.txt'),
        ('gunzip file.txt.gz', 'Uncompresses file', 'gunzip [options] file', 'gunzip myfile.txt.gz'),
        ('install -m 755 script.sh /usr/local/bin', 'Installs a script', 'install [-m MODE] source destination', 'install -m 755 myscript.sh /usr/local/bin'),
        ('ln -s source link_name', 'Creates symbolic link', 'ln -s source link_name', 'ln -s myfile.txt mylink.txt'),
        ('ln source link_name', 'Creates hard link', 'ln source link_name', 'ln myfile.txt mylink.txt'),
        ('ls', 'Lists files and directories.', 'ls [OPTIONS]', 'ls -l'),
        ('ls -f', 'Lists files without sorting.', 'ls -f', 'ls -f'),
        ('ls -h', 'Lists files with human-readable sizes.', 'ls -h', 'ls -h'),
        ('ls -l', 'Lists files with detailed info.', 'ls -l', 'ls -l'),
        ('ls -l Test', 'Lists details for "Test".', 'ls -l [directory]', 'ls -l mydir'),
        ('ls -lh', 'Combines -l and -h.', 'ls -lh', 'ls -lh'),
        ('ls -lu', 'Combines -l and -u.', 'ls -lu', 'ls -lu'),
        ('ls -r', 'Lists files in reverse order.', 'ls -r', 'ls -r'),
        ('ls -s', 'Lists files with sizes in blocks.', 'ls -s', 'ls -s'),
        ('ls -sh', 'Shows sizes in human-readable format.', 'ls -sh', 'ls -sh'),
        ('ls -t', 'Lists files sorted by modification time.', 'ls -t', 'ls -t'),
        ('ls -u', 'Lists files sorted by access time.', 'ls -u', 'ls -u'),
        ('ls [R]*', 'Lists files starting with "R".', 'ls [pattern]', 'ls R*'),
        ('ls [a-m]*', 'Lists files starting with a-m.', 'ls [pattern]', 'ls a*'),
        ('mkdir Test', 'Creates directory "Test".', 'mkdir [OPTIONS] directory', 'mkdir mydir'),
        ('mv -i file.txt /path/to/destination', 'Moves with confirmation.', 'mv -i source destination', 'mv -i myfile.txt /tmp/'),
        ('mv -i file2.txt file3.txt', 'Moves/renames with confirmation.', 'mv -i source destination', 'mv -i file1.txt file2.txt'),
        ('mv file.txt /path/to/destination', 'Moves file to a path.', 'mv source destination', 'mv myfile.txt /tmp/'),
        ('mv file1.txt file.txt', 'Renames file1.txt to file.txt.', 'mv source destination', 'mv file1.txt file2.txt'),
        ('pwd', 'Displays current working directory.', 'pwd', 'pwd'),
        ('rm -f', 'Forces deletion.', 'rm -f file', 'rm -f myfile.txt'),
        ('rm -i file', 'Removes file with confirmation', 'rm -i file', 'rm -i myfile.txt'),
        ('rm -r Test', 'Recursively deletes "Test".', 'rm -r directory', 'rm -r mydir'),
        ('rm file1.txt', 'Deletes file1.txt.', 'rm file', 'rm myfile.txt'),
        ('rm file1.txt file2.txt', 'Deletes files.', 'rm file1 file2 ...', 'rm file1.txt file2.txt'),
        ('rm -rf', 'Forces recursive deletion.', 'rm -rf directory', 'rm -rf mydir'),
        ('shred -u file.txt', 'Securely deletes a file', 'shred [-u] file', 'shred -u sensitive_data.txt'),
        ('tar -cvf archive.tar file1.txt file2.txt', 'Creates a tar archive', 'tar -cvf archive.tar file...', 'tar -cvf myarchive.tar *'),
        ('tar -xvf archive.tar', 'Extracts a tar archive', 'tar -xvf archive.tar', 'tar -xvf myarchive.tar'),
        ('touch file1.txt', 'Creates/updates file timestamp.', 'touch file', 'touch myfile.txt'),
        ('touch file2.txt file3.txt file4.txt', 'Creates/updates multiple timestamps.', 'touch file1 file2 ...', 'touch file1.txt file2.txt file3.txt'),
        ('unzip archive.zip', 'Extracts a zip archive', 'unzip archive.zip', 'unzip myarchive.zip'),
        ('zip archive.zip file1.txt file2.txt', 'Creates a zip archive', 'zip archive.zip file...', 'zip myarchive.zip *'),
        ('cd Test', 'Changes to directory "Test".', 'cd [directory]', 'cd /home'),
        ('expand file.txt.gz', 'Uncompresses a gzip file', 'expand file.txt.gz', 'expand myfile.txt.gz'),
        ('compress file.txt', 'Compresses a file using compress', 'compress file.txt', 'compress myfile.txt'),
        ('uncompress file.Z', 'Uncompresses a compress file', 'uncompress file.Z', 'uncompress myfile.Z'),
        ('split -b 100m large_file.txt part_', 'Splits a large file into smaller parts', 'split -b size large_file part_', 'split -b 100m large_file.txt part_'),
        ('cat part_* > large_file.txt', 'Combines split files', 'cat part_* > large_file.txt', 'cat part_* > large_file.txt'),
        ('head -n 100 large_file.txt > head100.txt', 'Creates a file containing the first 100 lines', 'head -n number large_file.txt > output.txt', 'head -n 100 large_file.txt > head100.txt'),
        ('tail -n 100 large_file.txt > tail100.txt', 'Creates a file containing the last 100 lines', 'tail -n number large_file.txt > output.txt', 'tail -n 100 large_file.txt > tail100.txt'),
        ('truncate -s 10k file.txt', 'Truncates a file to 10 kilobytes', 'truncate -s size file.txt', 'truncate -s 10k myfile.txt')
    ],
    'group_management': [
        ('groupadd [groupname]', 'Creates a new group.', 'groupadd [options] groupname', 'groupadd newgroup'),
        ('groupdel [groupname]', 'Deletes a group.', 'groupdel [options] groupname', 'groupdel oldgroup'),
        ('gpasswd [groupname]', 'Manages group membership.', 'gpasswd [options] groupname', 'gpasswd newgroup')
    ],
    'help': [
        ('man pwd', 'Displays the manual page for pwd.', 'man command', 'man ls')
    ],
    'networking': [
        ('curl [URL]', 'Transfers data to/from a server.', 'curl [options] URL', 'curl https://www.example.com'),
        ('dig google.com', 'DNS lookup', 'dig domain', 'dig google.com'),
        ('host google.com', 'DNS lookup', 'host domain', 'host google.com'),
        ('ifconfig', 'Displays/configures network interfaces.', 'ifconfig [options]', 'ifconfig eth0'),
        ('ip addr show', 'Displays network interface info.', 'ip [command] [options]', 'ip addr show'),
        ('ip route', 'Show routing table', 'ip route', 'ip route'),
        ('nc -lvp 8080', 'Listen on a port', 'nc -lvp port', 'nc -lvp 8080'),  # Use with caution
        ('netcat -lvp 8080', 'Listen on a port', 'netcat -lvp port', 'netcat -lvp 8080'),  # Use with caution
        ('netstat -a', 'Show all network connections', 'netstat [-a]', 'netstat -a'),
        ('netstat -tulpn', 'Displays network connections.', 'netstat [options]', 'netstat -tulpn'),
        ('nslookup google.com', 'DNS lookup', 'nslookup domain', 'nslookup google.com'),
        ('ping [hostname/IP]', 'Tests network connectivity.', 'ping [options] hostname/IP', 'ping google.com'),
        ('ss -l', 'Show listening sockets', 'ss [-l]', 'ss -l'),
        ('ss -tulpn', 'Displays network sockets.', 'ss [options]', 'ss -tulpn'),
        ('traceroute [hostname/IP]', 'Traces route to a destination.', 'traceroute [options] hostname/IP', 'traceroute google.com'),
        ('wget --limit-rate=20k https://www.example.com/file.txt', 'Download with rate limiting', 'wget --limit-rate=rate URL', 'wget --limit-rate=20k https://www.example.com/large_file.txt'),
        ('wget [URL]', 'Downloads a file from a URL.', 'wget [options] URL', 'wget https://www.example.com/file.txt'),
        ('nettop', 'Displays real-time network usage', 'nettop', 'nettop'), # Requires installation
        ('tcpdump -i eth0 port 80', 'Captures network traffic on eth0, port 80', 'tcpdump -i interface port', 'tcpdump -i eth0 port 80'),  # Requires root privileges
        ('tshark -i eth0 -f "port 80"', 'Captures and analyzes network traffic', 'tshark -i interface -f "filter"', 'tshark -i eth0 -f "port 80"'), # Requires installation and root privileges
        ('arp -a', 'Show ARP table', 'arp -a', 'arp -a'),
        ('route -n', 'Show routing table', 'route -n', 'route -n')

    ],
    'process_management': [
        ('bg', 'Put job in background', 'bg', 'bg %1'),
        ('fg', 'Bring background job to foreground', 'fg', 'fg %1'),
        ('htop', 'Interactive process viewer', 'htop', 'htop'),  # Requires installation: sudo apt-get install htop
        ('jobs', 'List background jobs', 'jobs', 'jobs'),
        ('kill [PID]', 'Sends a signal to a process.', 'kill [options] PID', 'kill 1234'),
        ('killall process_name', 'Kill all processes by name', 'killall process', 'killall firefox'),
        ('pkill [pattern]', 'Kills processes matching a pattern.', 'pkill [options] pattern', 'pkill firefox'),
        ('ps', 'Lists running processes.', 'ps [options]', 'ps aux'),
        ('ps aux | grep process_name', 'Find specific process', 'ps aux | grep process', 'ps aux | grep firefox'),
        ('renice -n 10 1234', 'Change process priority', 'renice -n priority PID', 'renice -n 10 1234'),
        ('top', 'Displays real-time process view.', 'top', 'top'),
        ('renice -n 19 1234', 'Decrease process priority', 'renice -n priority PID', 'renice -n 19 1234'),
        ('pstree', 'Shows the process tree', 'pstree', 'pstree'),
        ('pmap <PID>', 'Shows memory map of a process', 'pmap <PID>', 'pmap 1234'),
        ('limits', 'Shows current resource limits', 'limits', 'limits')

    ],
    'search': [
        ('find / -name file.txt -print', 'Find files by name (recursive)', 'find path -name file -print', 'find / -name myfile.txt -print'),
        ('locate file.txt', 'Find files by name', 'locate file', 'locate myfile.txt'),
        ('grep -r "pattern" /path/to/directory', 'Recursively searches for a pattern within a directory', 'grep -r "pattern" directory', 'grep -r "error" /var/log'),
        ('ag "pattern" /path/to/directory', 'Fast search using "ag" (The Silver Searcher)', 'ag "pattern" directory', 'ag "error" /var/log') # Requires installation: sudo apt-get install the_silver_searcher-ag

    ],
    'security': [
        ('passwd', 'Change password', 'passwd', 'passwd'),
        ('sudo addgroup users john', 'Add user to a group', 'sudo addgroup group user', 'sudo addgroup users john'),
        ('sudo apt update && sudo apt upgrade', 'Update and upgrade packages (Debian/Ubuntu)', 'sudo apt update && sudo apt upgrade', 'sudo apt update && sudo apt upgrade'),
        ('sudo delgroup users john', 'Remove user from a group', 'sudo delgroup group user', 'sudo delgroup users john'),
        ('sudo usermod -L username', 'Lock a user account', 'sudo usermod -L username', 'sudo usermod -L john'),
        ('sudo usermod -U username', 'Unlock a user account', 'sudo usermod -U username', 'sudo usermod -U john'),
        ('chkrootkit', 'Checks for rootkits', 'chkrootkit', 'chkrootkit'), #Requires installation
        ('rkhunter', 'Checks for rootkits and other security issues', 'rkhunter', 'rkhunter')

    ],
    'system_info': [
        ('cat /proc/cpuinfo', 'Shows detailed CPU info', 'cat /proc/cpuinfo', 'cat /proc/cpuinfo'),
        ('cat /proc/meminfo', 'Shows detailed memory info', 'cat /proc/meminfo', 'cat /proc/meminfo'),
        ('dmidecode', 'Shows DMI information', 'dmidecode', 'dmidecode'),
        ('echo "Hello, World!"', 'Displays the given text.', 'echo [STRING]', 'echo "Hello"'),
        ('free -h', 'Shows memory usage', 'free [options]', 'free -h'),
        ('hostname', 'Displays the hostname.', 'hostname', 'hostname'),
        ('inxi', 'Shows system information', 'inxi', 'inxi'),  # Requires installation: sudo apt-get install inxi
        ('lsblk', 'Lists block devices', 'lsblk', 'lsblk'),
        ('lscpu', 'Shows CPU information', 'lscpu', 'lscpu'),
        ('uname', 'Displays system information.', 'uname [options]', 'uname -a'),
        ('uname -a', 'Displays all system information.', 'uname -a', 'uname -a'),
        ('uptime', 'Shows uptime', 'uptime', 'uptime'),
        ('who', 'Displays logged-in users.', 'who', 'who'),
        ('whoami', 'Displays current username.', 'whoami', 'whoami'),
        ('df -h', 'Shows disk space usage in human-readable format', 'df -h', 'df -h'),
        ('du -sh', 'Shows disk usage in human-readable format for current directory', 'du -sh', 'du -sh'),
        ('hwinfo --short', 'Shows hardware information in a concise format', 'hwinfo --short', 'hwinfo --short')
    ],
    'system_administration': [
        ('systemctl status service_name', 'Shows the status of a systemd service', 'systemctl status service', 'systemctl status apache2'),
        ('systemctl start service_name', 'Starts a systemd service', 'systemctl start service', 'systemctl start apache2'),
        ('systemctl stop service_name', 'Stops a systemd service', 'systemctl stop service', 'systemctl stop apache2'),
        ('systemctl restart service_name', 'Restarts a systemd service', 'systemctl restart service', 'systemctl restart apache2'),
        ('systemctl enable service_name', 'Enables a systemd service to start at boot', 'systemctl enable service', 'systemctl enable apache2'),
        ('systemctl disable service_name', 'Disables a systemd service from starting at boot', 'systemctl disable service', 'systemctl disable apache2'),
        ('apt update && apt upgrade', 'Updates and upgrades packages (Debian/Ubuntu)', 'apt update && apt upgrade', 'apt update && apt upgrade'),
        ('yum update', 'Updates packages (Red Hat/CentOS/Fedora)', 'yum update', 'yum update'),
        ('pacman -Syu', 'Updates packages (Arch Linux)', 'pacman -Syu', 'pacman -Syu'),
        ('dpkg -i package.deb', 'Installs a Debian package', 'dpkg -i package.deb', 'dpkg -i mypackage.deb'),
        ('rpm -i package.rpm', 'Installs an RPM package', 'rpm -i package.rpm', 'rpm -i mypackage.rpm')
    ],
    'text_processing': [
        ('awk [options] program [file]', 'Pattern scanning and text processing language.', 'awk [options] program file', 'awk "{print $1}" myfile.txt'),
        ('cut -c 1-10 file.txt', 'Extracts characters 1-10.', 'cut -c start-end file', 'cut -c 1-10 myfile.txt'),
        ('cut -d"," -f 2,4 file.txt', 'Extracts 2nd and 4th fields.', 'cut -dDELIMITER -f FIELD file', 'cut -d, -f 2,4 myfile.txt'),
        ('cut -d"," -f 3-5 file.txt', 'Extracts fields 3-5.', 'cut -dDELIMITER -f FIELD file', 'cut -d, -f 3-5 myfile.txt'),
        ('cut -d"," -f 6 file.txt', 'Extracts the 6th field (comma-separated).', 'cut -dDELIMITER -f FIELD file', 'cut -d, -f 6 myfile.txt'),
        ('grep [pattern] [files]', 'Searches for a pattern in files.', 'grep [options] pattern [files]', 'grep "error" logfile.txt'),
        ('grep -n student wordSearch.txt', 'Searches and displays line numbers.', 'grep -n pattern file', 'grep -n "error" logfile.txt'),
        ('grep student wordSearch.txt', 'Searches for "student".', 'grep pattern file', 'grep "error" logfile.txt'),
        ('head -3 file.txt', 'Displays the first 3 lines.', 'head -n NUMBER file', 'head -n 3 myfile.txt'),
        ('head file.txt', 'Displays the first 10 lines.', 'head [options] file', 'head myfile.txt'),
        ('sed [options] command [file]', 'Stream editor for text transformations.', 'sed [options] command file', 'sed "s/old/new/" myfile.txt'),
        ('sort [options] [file]', 'Sorts lines of text files.', 'sort [options] file', 'sort myfile.txt'),
        ('tail -3 file.txt', 'Displays the last 3 lines.', 'tail -n NUMBER file', 'tail -n 3 myfile.txt'),
        ('tail file.txt', 'Displays the last 10 lines.', 'tail [options] file', 'tail myfile.txt'),
        ('uniq [options] [file]', 'Reports or filters out repeated lines.', 'uniq [options] file', 'uniq myfile.txt')
    ],
    'user_management': [
        ('adduser [username]', 'Adds a new user.', 'adduser [options] username', 'adduser newuser'),
        ('deluser [username]', 'Deletes a user.', 'deluser [options] username', 'deluser olduser'),
        ('su [username]', 'Switches to another user.', 'su [options] username', 'su root'),
        ('sudo [command]', 'Executes a command with elevated privileges.', 'sudo [options] command', 'sudo apt update'),
        ('sudo usermod -L username', 'Lock a user account', 'sudo usermod -L username', 'sudo usermod -L john'),
        ('sudo usermod -U username', 'Unlock a user account', 'sudo usermod -U username', 'sudo usermod -U john'),
        ('usermod [options] [username]', 'Modifies user properties.', 'usermod [options] username', 'usermod -G sudo newuser')
    ],
    'file_permissions': [
        ('chmod a=rwx file.txt', 'Sets read, write, execute for all.', 'chmod MODE file', 'chmod a=rwx myfile.txt'),
        ('chmod u+rw,g-rx file.txt', 'Sets owner permissions, removes group permissions.', 'chmod MODE file', 'chmod u+rw,g-rx myfile.txt'),
        ('chmod u-w file.txt', 'Removes write permission for the owner.', 'chmod MODE file', 'chmod u-w myfile.txt')
    ],
}
