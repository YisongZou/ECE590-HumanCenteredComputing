# ECE590-HumanCenteredComputing

![avatar](https://www.clipartmax.com/png/full/201-2012740_outline-hand-drawn-smiley-faces-basic-stock-vector-hand-drawn-happy-face.png)

```
For the website frontend and backend we use Django
```
Environment setup
```
sudo apt-get install python3-pip
python3 -m pip install Django
pip3 install --user django-crispy-forms
sudo apt-get install libpq-dev
pip3 install psycopg2
```
To run the website:(Remember to add the server into the allowed hosts inside mysite/settings.py)

```
cd mysite
python3 manage.py runserver 0.0.0.0:8000
```
visit the site at: http://vcm-xxxxx.vm.duke.edu:8000
