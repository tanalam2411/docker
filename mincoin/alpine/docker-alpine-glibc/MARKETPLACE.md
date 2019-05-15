
> 1. Create Ubuntu 18.04 drop on digitalocean.

> 2. [Initial Server Setup with Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04)
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

> 3. [Installing docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04 )
```sh
mnc@mnc-ubuntu:~$ sudo apt update -y
mnc@mnc-ubuntu:~$ sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
mnc@mnc-ubuntu:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
OK
mnc@mnc-ubuntu:~$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
mnc@mnc-ubuntu:~$ sudo apt update
# Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
mnc@mnc-ubuntu:~$ apt-cache policy docker-ce 
mnc@mnc-ubuntu:~$ sudo apt install docker-ce -y
mnc@mnc-ubuntu:~$ sudo systemctl status docker
mnc@mnc-ubuntu:~$ docker -v
Docker version 18.09.6, build 481bc77

```

> 4. Docker command without sudo
```sh
mnc@mnc-ubuntu:~$ sudo usermod -aG docker ${USER}
mnc@mnc-ubuntu:~$ su - ${USER}
mnc@mnc-ubuntu:~$ id -nG
mnc sudo docker

```
