import talib # Technical analysis library

'''This code takes trades based on EMA(exponential moving average)
When small moving average crosses big moving average above, The algorithm goes long in that stock
and if small EMA crosses big EMA below than algorithm goes short in that stock

This algorithm takes porfolio balance and risk in account and this algorithm is optimized based on stock volatility
and difference in big and small EMA 
So, This algorithm has tew major factors on which it can be tuned'''


def initialize(context):
    """
    To run this algorithm you have to copy and paste this algorithm in
    Quantopian research environment (You can paste it in the note book and hit back test)
    """
    context.flag = 0
    context.flag_I_am_here = 0
    context.Roku = sid(39840)

    schedule_function(check_bands, time_rules.every_minute())


def check_bands(context, data):

    flag = context.flag
    Roku = context.Roku
    flag_I_am_here = context.flag_I_am_here

    cur_price = data.current(Roku, 'price')

    prices_20 = data.history(Roku, 'close', 100, '1d')
    EMA_20days_result = talib.EMA(prices_20, timeperiod=20)

    prices_70 = data.history(Roku, 'close', 100, '1d')
    EMA_70days_result = talib.EMA(prices_70, timeperiod=70)

    # ------------------------------------------------
    # stocks = symbols('AAPL', 'QQQ')
    # period = 50
    # timeframe = 30
    # timeframe_unit = 'T'
    # bars_1m = period*timeframe
    # timeframe_string = str(timeframe) + timeframe_unit
    # # ------------------------------------------------

    diff = EMA_20days_result[-1] - EMA_70days_result[-1]
    diff_old = EMA_20days_result[-2] - EMA_70days_result[-2]
    diff_EMA_20 = EMA_20days_result[-1] - EMA_20days_result[-2]
    diff_EMA_20_old = EMA_20days_result[-2] - EMA_20days_result[-3]

    if diff > 0 and diff_old < 0 and context.portfolio.positions[Roku].amount == 0 and flag == 0:
        print("buy")
        order(Roku, (cur_price * 100),
              style=StopLimitOrder((cur_price + (cur_price * 0.75)), (cur_price - (cur_price * 0.5))))
        flag = 1
        # buy_price
    elif diff < 0 and diff_old > 0 and context.portfolio.positions[Roku].amount != 0:
        print("sell")

        order_target(Roku, 0)

    elif diff > 0.6 and context.portfolio.positions[Roku].amount == 0 and diff_EMA_20 > 0.02:
        print("buy more!")
        print(diff_EMA_20_old)
        print('diff')
        print(diff)
        order(Roku, (cur_price * 100),
              style=StopLimitOrder((cur_price + (cur_price * 0.5)), (cur_price - (cur_price * 0.5))))

    elif diff < 0:
        if context.portfolio.positions[Roku].amount != 0:
            print("Liquidate")
            order_target(Roku, 0)

    elif diff < 0 and diff_EMA_20 < 0.05 and context.portfolio.positions[Roku].amount != 0:
        print("I am here")
        print(diff_EMA_20_old)
        print('diff')
        print(diff)
        order_target(Roku, 0)

    record(Roku=data.current(Roku, 'price'),
           cur_price=cur_price,
           ema_20=EMA_20days_result[-1],
           ema_70=EMA_70days_result[-1])
