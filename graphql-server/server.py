import json
from datetime import datetime
from random import shuffle
from hashlib import md5
import logging

from ariadne import (
    MutationType,
    QueryType,
    SubscriptionType,
    load_schema_from_path,
    make_executable_schema,
) 
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from broadcaster import Broadcast
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

COLORS = [
    "#dc2626",
    "#ea580c",
    "#d97706",
    "#ca8a04",
    "#65a30d",
    "#16a34a",
    "#059669",
    "#0d9488",
    "#0891b2",
    "#0284c7",
    "#2563eb",
    "#4f46e5",
    "#7c3aed",
    "#9333ea",
    "#c026d3",
    "#db2777",
    "#e11d48",
]
shuffle(COLORS)


def time_now():
    return datetime.now().isoformat()

def str_to_color(src_str):
    str_hash = md5((src_str * 5).encode("utf-8")).hexdigest()
    hash_values = (str_hash[:8], str_hash[8:16], str_hash[16:24])
    color_index = sum(int(value, 16) % 256 for value in hash_values) % len(COLORS)
    return COLORS[color_index]

pubsub = Broadcast("redis://redis:6379")

history = [
    {
        "sender": "System",
        "color": "#64748b",
        "message": f"Inicio del Chat",
        "timestamp": time_now(),
    },
]

type_defs = load_schema_from_path("schema.graphql")

query = QueryType()

@query.field("history")
def resolve_history(*_):
    return history[-10:] 

mutation = MutationType()

@mutation.field("reply")
async def resolve_reply(*_, **message):
    message["color"] = str_to_color(message["sender"])
    if message["sender"] == "Servidor":
        message["color"] = "#000000"
    message["timestamp"] = time_now()
    history.append(message)
    logging.info(f"---------------------> reply: {history}")
    await pubsub.publish(channel="chatroom", message=json.dumps(message))

    return True

subscription = SubscriptionType()

@subscription.source("message")
async def source_message(_, info):
    async with pubsub.subscribe(channel="chatroom") as subscriber:
        async for event in subscriber:
            message = json.loads(event.message)
            if "politics" in message["message"].lower():
                continue

            yield message

@subscription.field("message")

def resolve_message(event, info):
    return event

schema = make_executable_schema(type_defs, query, mutation, subscription)
graphql = GraphQL(
    schema=schema,
    debug=False,
    websocket_handler=GraphQLTransportWSHandler(),
)

app = Starlette(
    debug=False,
    on_startup=[pubsub.connect],
    on_shutdown=[pubsub.disconnect],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/graphql", graphql)
app.add_websocket_route("/graphql", graphql)
