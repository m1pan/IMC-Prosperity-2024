from datamodel import OrderDepth, UserId, TradingState, Order, Trade
from typing import List, Dict
import string
import numpy as np

class Trader:

    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

		# Orders to be placed on exchange matching engine
        result = {}
        LIMIT = 20
        traderData: Dict[str, Dict] = state.traderData

        # AMETHYSTS
        symbol = state.listings["AMETHYSTS"].symbol
        order_depth: OrderDepth = state.order_depths[symbol]
        orders: List[Order] = []
        position: int = int(state.position["AMETHYSTS"]) # size of position in this product

        print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " 
              + str(len(order_depth.sell_orders)))

        if abs(position) <= LIMIT:
            if len(order_depth.sell_orders) != 0 and len(order_depth.buy_orders) != 0:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]

                # if sell price is lower than buy price, then buy and sell ; market neutral
                if int(best_ask) < int(best_bid):
                    size = min(-best_ask_amount, best_bid_amount)
                    print("BUY", str(size) + "x", best_ask)
                    orders.append(Order(symbol, best_ask, size))
                    orders.append(Order(symbol, best_bid, -size))
                # deviation of bid and ask from 1000
                ask_diff = 1000 - best_ask
                bid_diff = best_bid - 1000
                # if ask price is lower than 1000, buy
                if ask_diff > 0:
                    size = ask_diff/5 * (LIMIT - position)
                    print("BUY", str(ask_diff) + "x", size)
                    orders.append(Order(symbol, best_ask, size))

                # if bid price is higher than 1000, sell
                if bid_diff > 0:
                    size = bid_diff/5 * (LIMIT + position)
                    print("SELL", str(bid_diff) + "x", size)
                    orders.append(Order(symbol, best_bid, -size))
                
        traderData['own trade'][state.timestamp] = (state.own_trades[symbol])
        traderData['market trade'][state.timestamp] = ( state.market_trades[symbol])



        
        result[symbol] = orders

        # '''STARFRUIT'''
        # order_depth: OrderDepth = state.order_depths["STARFRUIT"]
        # orders: List[Order] = []
        # position = state.position["STARFRUIT"]
        # acceptable_price = 10
        # print("Acceptable price : " + str(acceptable_price))
        # print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
        
        # if len(order_depth.sell_orders) != 0:
        #     best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
        #     if int(best_ask) < acceptable_price:
        #         print("BUY", str(-best_ask_amount) + "x", best_ask)
        #         orders.append(Order("STARFRUIT", best_ask, -best_ask_amount))
        
        # if len(order_depth.buy_orders) != 0:
        #     best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
        #     if int(best_bid) > acceptable_price:
        #         print("SELL", str(best_bid_amount) + "x", best_bid)
        #         orders.append(Order("STARFRUIT", best_bid, -best_bid_amount))
        
        # result["STARFRUIT"] = orders


        # String value holding Trader state data required. 
            # It will be delivered as TradingState.traderData on next execution.
        # traderData = "SAMPLE" 
        
		# 		# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData