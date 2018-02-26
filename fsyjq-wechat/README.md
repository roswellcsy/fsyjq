#checklist

更新部署时
backend
git pull
pip install -r requirements.txt
修改setting：
databases
allowed_hosts
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

frontend
检查config/prod.env.js
npm i
