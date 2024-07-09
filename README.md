# Introduction

So far, your web server communicates using the **http** protocol, which is insecure
by default.  The secure version of http is called **https** and enables encrypted
communication between the browser and the webserver.

Here's an industry article on why HTTPS is important:
https://www.cloudflare.com/en-ca/learning/ssl/why-use-https/

HTTPS is based on the idea of **certificates**.  It used to cost money to get
an HTTPS certificate for your server, but now it's free via **Let's Encrypt**.
Read up on how Let’s Encrypt works here: https://letsencrypt.org/how-it-works/

Follow these steps to enable HTTPS on your webserver.

# Steps

  1. Once HTTPS is enabled, your server will communicate with browsers using
     port 443, so make sure it is enabled on your security rules/firewall on
     AWS

  1. Make sure you have a running apache web server following the
     web-admin-basic lesson
     
  1. Install the let's encrypt software
     ```
     sudo apt install certbot python3-certbot-apache
     ```
     
  1. Execute the certbot software and answer all the questions.  You must use provide
     your domain name as HTTPS only works with domain names, not ip addresses.
     ```
     sudo certbot 
     ```
     
  1. You should now be able to access your site using https instead of http.
     ```
     curl https://${your_domain_name}
     ```

## Notes

  - https configration is housed in a completely separate configuration file.
    After successfully running certbot, a new configuration file is created
    in the `/etc/apache2/sites-available/` directory:
    
    ```
    /etc/apache2/sites-available/
    ├── 000-default-le-ssl.conf
    ├── 000-default.conf
    └── default-ssl.conf
    ```
  - The new file, `000-default-le-ssl.conf` contains the https configuration.
    From this point onwards, this is the only file that's relevant.  The original
    configuration file, `000-default.conf` only contains rules to redirect the browser
    to the https configuration.

  - Once you have enabled https on apache, all the reverse proxy applications will also
    be https enabled.

# Hand-in

Clone the assignment repo into your `${HOME}` directory, then execute pytest
in the `${HOME}/${ASSIGNMENT_REPO}/` to check if you got everything correct,
as follows:

```
cd ~
git clone ${ASSIGNMENT_REPO}
cd ${ASSIGNMENT_REPO}
pytest
```

When you are satisified, run the following commands to submit:

  - git add -A
  - git commit -a -m 'submit'
  - git push
