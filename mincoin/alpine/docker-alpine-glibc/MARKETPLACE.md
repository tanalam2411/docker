
> 1. Create Ubuntu 18.04 drop on digitalocean.

> 2. 
```sh
root@mnc-ubuntu:~# adduser mnc
# password - mnc1234
root@mnc-ubuntu:~# usermod -aG sudo mnc
root@mnc-ubuntu:~# su mnc

mnc@mnc-ubuntu:~$ sudo ufw allow OpenSSH
Rules updated
Rules updated (v6)

mnc@mnc-ubuntu:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
mnc@mnc-ubuntu:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere                  
OpenSSH (v6)               ALLOW       Anywhere (v6)  

mnc@mnc-ubuntu:~$ sudo su
root@mnc-ubuntu:/home/mnc# cd
root@mnc-ubuntu:~# rsync --archive --chown=mnc:mnc ~/.ssh /home/mnc
```

Now you can login using `mnc` user also using ssh.
