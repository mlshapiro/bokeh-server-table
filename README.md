# Boker Server: Table Example

Adapted from Bokeh Examples: https://github.com/bokeh/bokeh/tree/master/examples/app/export_csv

Developed on a new Ubuntu 16.04 on digital ocean

## Get OS dependencies

`$ sudo apt-get install nginx git`

## Install anaconda
 
`$ wget https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh`
`$ bash Anaconda3-4.3.1-Linux-x86_64.sh`

## Set up nginx

`$ cd /etc/nginx/sites-available`
`$ ln -s /root/bokeh-server-table/nginx.conf bokeh`
`$ sudo ln -s /etc/nginx/sites-available/bokeh /etc/nginx/sites-enabled/`
`$ sudo rm /etc/nginx/sites-enabled/default`
`$ sudo systemctl start nginx`

## Install service

`$ chmod ugo+x bokeh.service`
`$ sudo cp bokeh.service /etc/systemd/system`
`$ sudo systemctl daemon-reload`

## Control nginx
 
`$ sudo systemctl stop nginx`
`$ sudo systemctl start nginx`

## Set up ufw

To set up up `ufw` (NOTE: THis will remove your ssh access if done wrong):
 
`$ sudo ufw allow 'Nginx HTTP'`
`$ sudo ufw allow ssh`
`$ sudo ufw enable`
`$ sudo ufw status`