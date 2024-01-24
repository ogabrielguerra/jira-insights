#!/bin/bash
APP_PATH=[tmp_path]
APP_SERVER=[server]
APP_REMOTE_DIR=[remote_dir]

mkdir ./tmp 
cd ./tmp

echo "\n#1 Cloning master branch.\n"
git clone [repository_path]

echo "\n#2 Preparing files for transfering.\n"
tar -czf app.tar.gz $APP_REMOTE_DIR

echo "\n#3 Uploading files.\n"
scp -r app.tar.gz $APP_SERVER:/tmp

echo "\n#4 Clean up."
rm -rf ../tmp

echo "\n#5 Unpacking files in server.\n"
ssh $APP_SERVER "
    cd /tmp && tar -xf app.tar.gz 
    rm -rf code/* 
    cp -r /tmp/$APP_REMOTE_DIR/* ~/code"

echo "\n****************"
echo "#6 IMPORTANT: The process is not completed yet. To finish the deployment, ssh into server and run **deploy-containers.sh**"
echo "******************"