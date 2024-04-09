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
        acceptable_price = 10  # Participant should calculate this value
        print("Acceptable price : " + str(acceptable_price))
        print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))

        if len(order_depth.sell_orders) != 0:
            best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
            if int(best_ask) < acceptable_price:
                print("BUY", str(-best_ask_amount) + "x", best_ask)
                orders.append(Order("AMETHYST", best_ask, -best_ask_amount))

        if len(order_depth.buy_orders) != 0:
            best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
            if int(best_bid) > acceptable_price:
                print("SELL", str(best_bid_amount) + "x", best_bid)
                orders.append(Order("AMETHYST", best_bid, -best_bid_amount))
        
        result["AMETHYST"] = orders

        '''STARFRUIT'''
        order_depth: OrderDepth = state.order_depths["STARFRUIT"]
        orders: List[Order] = []
        position = state.position["STARFRUIT"]
        acceptable_price = 10
        print("Acceptable price : " + str(acceptable_price))
        print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
        
        if len(order_depth.sell_orders) != 0:
            best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
            if int(best_ask) < acceptable_price:
                print("BUY", str(-best_ask_amount) + "x", best_ask)
                orders.append(Order("STARFRUIT", best_ask, -best_ask_amount))
        
        if len(order_depth.buy_orders) != 0:
            best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
            if int(best_bid) > acceptable_price:
                print("SELL", str(best_bid_amount) + "x", best_bid)
                orders.append(Order("STARFRUIT", best_bid, -best_bid_amount))
        
        result["STARFRUIT"] = orders
        

        # String value holding Trader state data required. 
            # It will be delivered as TradingState.traderData on next execution.
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData