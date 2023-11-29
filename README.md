# Тестовое задание для Python разработчика
# [Задание](https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit)

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель Item с полями (name, description, price)
- API с двумя методами:
    - __GET__ _/buy/{id}_, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос __stripe.checkout.Session.create(...)__ и полученный session.id выдаваться в результате запроса
    - __GET__ _/item/{id}_, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки __Stripe__ происходить редирект на Checkout форму __stripe.redirectToCheckout(sessionId=session_id)__
- Залить решение на Github, описать запуск в Readme.md
- Опубликовать свое решение чтобы его можно было быстро и легко протестировать.

# Бонусные задачи
1. Запуск используя Docker
2. Использование environment variables
3. Просмотр Django Моделей в Django Admin панели
4. Запуск приложения на удаленном сервере, доступном для тестирования
5. Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
6. Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
7. Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
8. Реализовать не Stripe Session, а Stripe Payment Intent.

# Описание
Сервис, общающийся со __Stripe__ и создающий платежные формы для товаров и заказов. На текущий момент реализовано:
- Реализованы модели __Stripe__ и __Order__ в models.py
- Получение HTML страниц со списком товаров или заказов, с информацией о выбранном товаре или заказе, об успешной оплате или прерывания оплаты
- Получение __Stripe Session Id__ для оплаты выбранного Item через метод __GET__ по адресу _/buy/{id}_
- Вынос environment variables в файл __.env__ (предоставлен)
- Очищен код с помощью линтеров black и isort
- Настроена __Django Admin панель__ для просмотра, создания, редактирования и удаления данных моделей
- Контейнеризация приложения через __docker__
- Запуск приложения на удаленном сервере (демонстрация по запросу)

# Технологии
Сервис разработан с использованием Django, Django Rest Framework, библиотеки stripe.<br/>
В качестве БД использовался PostgreSQL. Для обеспечения корректной связи Django и PostgreSQL использовалась библиотека psycopg2-binary.<br/>
Также проект и БД были обернуты в Docker-контейнеры и запускаются при помощи docker compose<br/>

# Запуск
Для запуска контейнера с приложением необходимо:<br/>
Скачать репозиторий
```
git clone https://github.com/mabredin/ranks_test_task.git
```
Перейти в папку ranks_test_task/src/
```
cd ranks_test_task/src/
```
__*Если запуск производится на сервере и используется публичный ip, необходимо добавить его в .env в ALLOWED_HOSTS через запятую__<br/>

Запустить контейнер
```
make docker-up
```
Проверить результат (по желанию)
```
docker ps
```
Успешный результат команды представлен на рисунке ниже:
![](https://github.com/mabredin/ranks_test_task/assets/62469376/e295555a-98e1-4ad7-bef6-ad75c7d50f80)

# Заполнение данных
Для заполнения данных необходимо выполнить несколько шагов:<br/>
- Сделать миграции
```
docker compose run web python manage.py migrate
или
sudo docker compose run web python manage.py migrate
```

- Создать пользователя для доступа к административной панели Django
```
docker compose run web python manage.py createsuperuser
или
sudo docker compose run web python manage.py createsuperuser
```

- Ввести данные пользователя.
- В браузере перейти по адресу _0.0.0.0:8000/admin_ или _<server_ip>:8000/admin_
- Войти под созданным пользователем и создать товары (заказы).
- Снова перейти по адресу _0.0.0.0:8000/_ или _<server_ip>:8000/_
- Сервис готов.

# Пример работы
Страница с информацией о товаре<br/><br/>
![](https://github.com/mabredin/ranks_test_task/assets/62469376/8800056b-9a73-4098-a69a-c8e18a4236eb)

Страница оплаты товара<br/><br/>
![](https://github.com/mabredin/ranks_test_task/assets/62469376/9700f01f-3abb-480f-974c-6ce3516734ce)

Страница с информацией о заказе<br/><br/>
![](https://github.com/mabredin/ranks_test_task/assets/62469376/a125a099-f47f-453d-aa0c-29ceb93bf4d4)

Страница оплаты заказа<br/><br/>
![](https://github.com/mabredin/ranks_test_task/assets/62469376/68fa6a06-198f-4d90-a02b-98555a2f7c9d)

# Примечание
_Так как проект представляет собой выполнение тестового задания, в репозитории присутствуют файлы .env, Makefile и requirements_dev.txt_<br/>
