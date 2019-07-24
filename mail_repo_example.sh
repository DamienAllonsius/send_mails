#!/bin/bash
cd /path/to/your/repo; fetch_result=$(git fetch); if [ $(git rev-parse HEAD) != $(git rev-parse @{u}) ]; then python /path/to/file/mail.py YOUR_GMAIL_ADDRESS YOUR_GMAIL_PWD TARGET_E_MAIL_ADDRESS "My Subject" "$fetch_result"; fi;
