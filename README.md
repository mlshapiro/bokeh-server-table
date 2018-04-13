# Boker Server: Table Example

Adapted from Bokeh Examples: https://github.com/bokeh/bokeh/tree/master/examples/app/export_csv

Developed on a new Ubuntu 16.04 on digital ocean. 

The following process should get you up and running from a fresh new server instance.

## Get OS dependencies

```bash
$ sudo apt-get install nginx git
```
## Install anaconda
 
 - use the latest version of [anaconda](https://www.anaconda.com/download/#linux) or [miniconda](https://conda.io/miniconda.html)
 
 ```bash
$ wget https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh
$ bash Anaconda3-4.3.1-Linux-x86_64.sh
$ # add anaconda to your PATH (.bashrc/.bash_profile) so that you can use pip/conda from anaconda
```
- make sure anaconda is your default systems python

```bash
$ sudo rm /usr/bin/python  # remove old python symlink
$ sudo ln -s /home/ubuntu/anaconda3/bin/python /usr/bin/python   # link anaconda python as system default
```

- Log out, then log back in
- Make sure you are using anaconda by typing `$ python` and making sure it lists your version of anaconda

## Clone this repository

```bash
$ git clone https://github.com/mlshapiro/bokeh-server-table.git
$ cd bokeh-server-table
```

## Set up nginx

```bash
$ sudo rm /etc/nginx/sites-available/default  # remove the default site
$ ln -s /root/bokeh-server-table/conf/nginx.conf /etc/nginx/sites-available/default   # make the bokeh nginx conf the default
$ sudo systemctl start nginx   # start the nginx service
$ sudo systemctl status nginx  # check the nginx status
```

## Install systemctl service

- This will run server in the background on start up

```bash
$ sudo systemctl enable /home/ubuntu/bokeh-server-table/conf/bokeh.service  # this creates a symlink in /etc/systemd/system/
$ sudo systemctl daemon-reload         # reload conf files
$ sudo systemctl start bokeh.service   # start the service
$ sudo systemctl status bokeh.service  # check the status
```

## Visit URL

You should be able to visit the ip address of your server and see your bokeh app running.

# Notes

## Set up universal firewall

To set up up `ufw` (NOTE: THis will remove your ssh access if done wrong):

```bash
$ sudo ufw allow 'Nginx HTTP'
$ sudo ufw allow ssh
$ sudo ufw enable
$ sudo ufw status    # check status to make sure you have ssh access
```
