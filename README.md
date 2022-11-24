# StripeTestProject

## 🛠 Использованные технологии:
*   python
*   Django
*   stripe
*   environ
*   Docker


 ## 🚲 Для запуска приложения нужно:

1) Создайте stripe аккаунт по ссылке https://dashboard.stripe.com/register
2) В stripe dashboard выберите вкладку developers (справа сверху) и там перейдите в API keys
3) Скопируйте ващи ключи от API в файл env.env и переименуйте его в .env
4) Создайте образ Docker при помощи комманды docker build .
5) Запустите контейнер докер с приложением коммандой docker run --publish 8000:8000 {container_id}

## 🌐 Urls:
* /admin - админка с возможностью добавления товаров в бд, чтобы в нее войти нужно создать суперюзера коммандой python manage.py createsuperuser или воспользуйтес уже созданным (name: rudique, password: 1234)
* /item/{item_id} - страничка, которая показывает товар с item_id из базы данных, с дальнейшей возможностью купить его
* /buy/{item_id} - страничка оформления покупки товара с item_id 

