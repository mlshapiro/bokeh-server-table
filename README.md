# Boker Server: Table Example

Adapted from Bokeh Examples: https://github.com/bokeh/bokeh/tree/master/examples/app/export_csv

Developed on a new Ubuntu 16.04 on digital ocean. 

The following process should get you up and running from a fresh new server instance.

## Get OS dependencies

- `$ sudo apt-get install nginx git`

## Install anaconda
 
- `$ wget https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh`
- `$ bash Anaconda3-4.3.1-Linux-x86_64.sh`

## Set up nginx

- `$ ln -s /root/bokeh-server-table/nginx.conf /etc/nginx/sites-available/bokeh`
- `$ sudo ln -s /etc/nginx/sites-available/bokeh /etc/nginx/sites-enabled/`
- `$ sudo rm /etc/nginx/sites-enabled/default`  
- `$ sudo systemctl start nginx`

## Install systemctl service

This will run server in the background on start up

- `$ sudo cp bokeh.service /etc/systemd/system`
- `$ sudo systemctl daemon-reload`
- `$ sudo systemctl start bokeh.service`

## Visit URL

You should be able to visit the ip address of your server and see your bokeh app running.

# Other Commands

## Set up ufw

To set up up `ufw` (NOTE: THis will remove your ssh access if done wrong):
 
- `$ sudo ufw allow 'Nginx HTTP'`
- `$ sudo ufw allow ssh`
- `$ sudo ufw enable`
- `$ sudo ufw status`