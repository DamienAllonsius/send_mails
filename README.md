# A small script that sends you emails when your repo is updated

Tired of having __maximum 2 collaborators__  who are allowed to get github notifications on your private repositories ? Then this script does the job for you !

1. Configure the script mail_repo_example.sh by adding your local repo folder path, your __gmail__ email address, your password (__caution !__), the email address you want to send your message to, the subject of the message.

2. Use for instance cron to run the script every hour for example : 0 * * * *  . /path/to/the/script/mail_repo_example.sh

3. Configure maybe your gmail account : go to *security* and then allowed *less secured applications* to be run.

4. That's all folks !

Cron will execute every hour your script which will fetch new commits of your repository. It will send you an email with the details of the fetched data if it finds new commits !
