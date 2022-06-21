class DataFunctions:

    def price_calculation(self, prices):
        average_price = sum(prices) / len(prices)
        lowest_price = min(prices)
        highest_price = max(prices)
        price_calc = {'avg': average_price, 'low': lowest_price, 'high': highest_price}

        return price_calc

    def price_output(self, calc_res):
        print('avg: ', calc_res['avg'])
        print('min: ', calc_res['low'])
        print('max: ', calc_res['high'])
