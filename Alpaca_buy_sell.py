import alpaca_trade_api as tradeapi
import config


class AlpacaBuySell:

    def __init__(self, symbol=None, qty=10, order_type='market', time_in_force='gtc'):
        self.base_url = config.BASE_URL
        self.api_key_id = ''  # put your api key of the account you want to trade on
        self.api_secret = ''  # put your secret key of the account you want
        # to trade on
        self.symbol = symbol  # Ticker symbol of the stock
        self.qty = qty  # number of shares
        self.order_type = order_type  # Order type
        self.time_in_force = time_in_force  # Time in force

    def api_call(self):  # This function uses api call to get to the endpoint from which user can buy/sell stocks
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )

        return api

    def naked_buy_order(self):  # Place a naked buy order
        # lace a naked buy order i.e. place a market buy order without any limit or stop sell order
        naked_buy_order = AlpacaBuySell(self.symbol).api_call().submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='buy',
            type=self.order_type,
            time_in_force=self.time_in_force,
            order_class='simple',
        )

        return naked_buy_order

    def buy(self, limit, stop):  # Place market buy order with limit and stop (OCO) orders
        #  place market order along with take profit and stop limit order
        api_buy = AlpacaBuySell(self.symbol).api_call().submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='buy',
            type=self.order_type,
            time_in_force=self.time_in_force,
            order_class='bracket',
            take_profit=dict(limit_price=limit),
            stop_loss=dict(stop_price=stop)
        )

        return api_buy

