from client import get_client
from logging_config import setup_logger

logger = setup_logger()


def place_market_order(symbol, side, quantity):
    try:
        client = get_client()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(
            f"MARKET ORDER | {side} | {symbol} | Qty={quantity}"
        )

        return order

    except Exception as e:
        logger.error(str(e))
        raise


def get_balance():
    try:
        client = get_client()

        balances = client.futures_account_balance()

        for asset in balances:
            if asset["asset"] == "USDT":
                return asset["balance"]

    except Exception as e:
        logger.error(str(e))
        raise   

def get_positions():
    try:
        client = get_client()

        positions = client.futures_position_information()

        active_positions = []

        for pos in positions:

            if float(pos["positionAmt"]) != 0:

                active_positions.append({
                    "symbol": pos["symbol"],
                    "quantity": pos["positionAmt"],
                    "entry_price": pos["entryPrice"]
                })

        return active_positions

    except Exception as e:
        logger.error(str(e))
        raise   

def place_limit_order(symbol, side, quantity, price):
    try:
        client = get_client()

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(
            f"LIMIT ORDER | {side} | {symbol} | Qty={quantity} | Price={price}"
        )

        return order

    except Exception as e:
        logger.error(str(e))
        raise    

def cancel_order(symbol, order_id):
    try:
        client = get_client()

        result = client.futures_cancel_order(
            symbol=symbol,
            orderId=order_id
        )

        logger.info(
            f"ORDER CANCELLED | {symbol} | {order_id}"
        )

        return result

    except Exception as e:
        logger.error(str(e))
        raise   