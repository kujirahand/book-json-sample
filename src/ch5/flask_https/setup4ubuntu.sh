#!/bin/bash
APP_DIR=/var/www/flask_https
SCRIPT_DIR=$(cd $(dirname $0); pwd)
USERNAME=$(whoami)

# setup app dir
sudo mkdir -p $APP_DIR
sudo chown $USERNAME $APP_DIR
cp -r $SCRIPT_DIR/* $APP_DIR/

# setup uWSGI service
sudo cp $SCRIPT_DIR/flask_https.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start flask_https
sudo systemctl enable flask_https
# sudo systemctl status flask_https

# setup nginx
# backup original default
# sudo cp /etc/nginx/sites-enabled/default /etc/nginx/_sites-enabled_default.bak
# sudo cp $SCRIPT_DIR/default /etc/nginx/sites-enabled/default
# sudo systemctl restart nginx

