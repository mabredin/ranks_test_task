if [[ -v DJANGO_SUPERUSER_USERNAME ]] && [[ -v DJANGO_SUPERUSER_PASSWORD ]]; then
    python manage.py createsuperuser --email="admin@admin.com" --noinput
else
    echo "admin credentials does not set; skip admin creation"
fi