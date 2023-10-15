export TG_KEY=''
export WE_KEY=''
export GEO_KEY=''
(trap 'kill 0' SIGINT; python3 test_site/manage.py runserver & python3 telegramm/bot.py)