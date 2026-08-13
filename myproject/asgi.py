import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

from django.core.asgi import get_asgi_application

# Сначала полностью инициализируем Django.
django_asgi_app = get_asgi_application()

# Только после этого можно импортировать код,
# который обращается к Django models.
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from strawberry.channels import GraphQLWSConsumer

from messenger.strawberry import schema


graphql_ws_consumer = GraphQLWSConsumer(schema)

application = ProtocolTypeRouter({
    "http": django_asgi_app,

    "websocket": URLRouter([
        path(
            "graphql/subscription/",
            graphql_ws_consumer.as_asgi(schema=schema)
        ),
    ]),
})