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

    def buy_and_stop_order(self, stop):  # Place buy with stop loss order
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )
        # place market order along with take profit and stop limit order
        api_buy = api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='buy',
            type=self.order_type,
            time_in_force=self.time_in_force,
            order_class='oto',
            stop_loss=dict(stop_price=stop)
        )

        return api_buy

    def stop_limit_buy_order(self, limit_price, stop_price):
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )
        # place market order along with take profit and stop limit order
        api_buy = api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='buy',
            type=self.order_type,
            time_in_force=self.time_in_force,
            order_class='oto',
            stop_loss=dict(stop_price=stop_price, limit_price=limit_price)
        )

    def stop_limit_sell_order(self, limit, stop):  # place market sell order take profit and stop limit order
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )
        # place market sell order take profit and stop limit order

        api_stop_limit_sell = api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='sell',
            type='limit',
            time_in_force=self.time_in_force,
            order_class='oco',
            take_profit=dict(limit_price=limit),
            stop_loss=dict(stop_price=stop)
        )

        return api_stop_limit_sell

    def stop_limit_buy_order_without_making_a_market_buy(self, limit, stop):  # Place stop and limit (OCO) orders
        # without placing a buy order for this to work one must have a open naked buy order
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )

        api_buy = api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='buy',
            type='limit',
            time_in_force=self.time_in_force,
            order_class='oco',
            take_profit=dict(limit_price=limit),
            stop_loss=dict(stop_price=stop)
        )

    def market_sell(self):  # Redundant function due to some dependancy I did not remove it but you can use short
        # sell instead of this function
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )
        # place market order along with take profit and stop limit order
        api_sell = api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='sell',
            type='market',
            time_in_force=self.time_in_force,
            # limit_price = limit
        )

        return api_sell

    def short_sell(self):
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )
        # place market order along with take profit and stop limit order
        api_sell = api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='sell',
            type='market',
            time_in_force=self.time_in_force,
            # limit_price = limit
        )

        return api_sell

    def limit_sell(self, limit):
        api = tradeapi.REST(
            base_url=self.base_url,
            key_id=self.api_key_id,
            secret_key=self.api_secret
        )
        # place market order along with take profit and stop limit order
        api_sell = api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side='sell',
            type='limit',
            time_in_force=self.time_in_force,
            limit_price=limit
        )

        return api_sell