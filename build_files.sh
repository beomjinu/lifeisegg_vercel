python3 -m pip install --upgrade pip
python3 -m pip install --no-cache-dir -r requirements.txt

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput