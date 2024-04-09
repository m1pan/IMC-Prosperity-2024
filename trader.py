from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string
import numpy as np

class Trader:
    
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

		# Orders to be placed on exchange matching engine
        result = {}

        '''AMETHYST'''
        order_depth: OrderDepth = state.order_depths["AMETHYST"]
        orders: List[Order] = []
        position = state.position["AMETHYST"] # size of position in this product

        print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))

        if len(order_depth.sell_orders) != 0 and len(order_depth.buy_orders) != 0:
            best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
            best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]

            # if sell price is lower than buy price, then buy and sell
            if int(best_ask) < int(best_bid):
                size = min(-best_ask_amount, best_bid_amount)
                print("BUY", str(size) + "x", best_ask)
                orders.append(Order("AMETHYST", best_ask, size))
                orders.append(Order("AMETHYST", best_bid, -size))


        
        result["AMETHYST"] = orders

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
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData