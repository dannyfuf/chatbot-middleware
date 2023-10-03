from pydantic import BaseModel

import telegram.handlers.client, telegram.handlers.help
import telegram.handlers.register, telegram.handlers.login
import telegram.handlers.render, telegram.handlers.market, telegram.handlers.market

client = telegram.handlers.client.client

class Render(BaseModel):
    user_id: str
    auth_token: str

class MarketPlace(BaseModel):
    auth_token: str
    action: str
    action_item: str
    action_amount: str

class Farm(BaseModel):
    auth_token: str
    action: str
    action_item: str
    action_amount: str