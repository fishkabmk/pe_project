from flask_jsonrpc import JSONRPC
from flask_jsonrpc.exceptions import InvalidParamsError, JSONRPCError

from config import settings

jsonrpc = JSONRPC(service_url='/api/beer')


@jsonrpc.method()
def buyBeer(beer_name: str, quantity: int) -> bool:
    result = False
    # Можем выкидывать различные исключения, если нам это нужно
    if beer_name == "baltika":
        raise JSONRPCError(message='AAAAAAAAAAAAAAAAAAAA, do not buy baltika')
    if beer_name in ["klinskoe","strelts"]:
        result = True
    if quantity <= 0:
        result = False
    return result
