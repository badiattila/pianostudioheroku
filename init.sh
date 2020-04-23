sudo snap install heroku --classic
sudo pip3 install flask-pymongo
sudo pip3 install dnspython
sudo pip3 install Flask-Mail
sudo pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
mkdir templates
touch templates/index.html
mkdir static
mkdir static/css
touch static/css/style.css
git init
git config --global user.name "Attila Badi"
git config --global user.email "attila.badi@gmail.com"
git add . 
git commit -m "initial push with Procfile for Heroku"
--- Done to this point
heroku login
heroku apps
heroku git:remote -a piano-studio
git push heroku master
heroku ps:scale web=1
