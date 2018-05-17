# Email Tracker
Email Tracker allows you to send emails and track those emails to see if they were opened or not.
If they were opened, you can see their IP address (and hence rough location), user agent, device etc.

## How does it work?
When the `send_mail.py` sends an email, it embeds a 1x1 gif into the mail which is hosted on my webserver (using nginx).
The name of the gif is the same as the target's email address, so, we can get the relevant information from nginx's logs, which is what `check_activity.py` does.

## Dependencies and Setup
Both the scripts require no external dependencies and will run out of the box with python3.

Apart from the scripts, you need to have `nginx` installed and running.

For `check_activity.py` to parse information from nginx logs, you'll have to change the `log_format` option in `/etc/nginx/nginx.conf`.

    log_format myformat '$remote_addr,$time_local,"$request","$http_referer","$http_user_agent"';
    accesslog /var/log/nginx/access.log myformat;

## Installation and Usage
After setting up `nginx` as mentioned above, clone this repo:

    git clone https://github.com/mananapr/email-tracker
Then copy the files to the webroot:

    cp -r email-tracker/* /var/www/html
To manipulate files within the webroot, change the permissions:

    sudo chown -R "$USER":www-data /var/www/html
    sudo chmod -R 0755 /var/www/html
Now you can use `send_mail.py` to send mails and `check_activity.py` to track the sent mails.
Make sure that you change the variables in both the scripts according to your setup.

## Demo
[This](https://u.teknik.io/1owqz.mp4) video shows me using the scripts.
I checked the mail on my phone, so it shows my Phone OS version and IP Address.
