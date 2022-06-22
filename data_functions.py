import pandas as pd

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

    def data_packing(self, *args):
        data_list = []
        for i in range(len(args[0])):
            data_list.append([args[0][i], args[1][i], args[2][i]])

        return data_list

    def data_collection(self, *args):
        data_pack = self.data_packing(args)
        df = pd.DataFrame(data_pack, columns=['Price', 'Route Time', 'Way'])
        df.to_html('apart_data.html')
        df.to_csv('apart_data.csv')

        return df

