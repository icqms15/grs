# -*- coding: utf-8 -*-
''' Best buy or sell '''
# Copyright (c) 2012 Toomore Chiang, http://toomore.net/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class BestFourPoint(object):
    """ 四大買點組合 """
    def __init__(self, data):
        self.data = data

    def bias_ratio(self, positive_or_negative=False):
        """ 判斷乖離 """
        return self.data.ckMAO(self.data.MAO(3, 6)[0],
                               pm=positive_or_negative)[0]

    def check_plus_bias_ratio(self):
        """ 正乖離扣至最大 """
        return self.bias_ratio(True)

    def check_mins_bias_ratio(self):
        """ 負乖離扣至最大 """
        return self.bias_ratio()

    ##### 四大買點 #####
    def best_buy_1(self):
        """ 量大收紅 """
        result = self.data.value[-1] > self.data.value[-2] and \
                 self.data.price[-1] > self.data.openprice[-1]
        return result

    def best_buy_2(self):
        """ 量縮價不跌 """
        result = self.data.value[-1] < self.data.value[-2] and \
                 self.data.price[-1] > self.data.price[-2]
        return result

    def best_buy_3(self):
        """ 三日均價由下往上 """
        return self.data.MA(3)[1] == 1

    def best_buy_4(self):
        """ 三日均價大於六日均價 """
        return self.data.MA(3)[0][-1] > self.data.MA(6)[0][-1]

    ##### 四大賣點 #####
    def best_sell_1(self):
        """ 量大收黑 """
        result = self.data.value[-1] > self.data.value[-2] and \
                 self.data.price[-1] < self.data.openprice[-1]
        return result

    def best_sell_2(self):
        """ 量縮價跌 """
        result = self.data.value[-1] < self.data.value[-2] and \
                 self.data.price[-1] < self.data.price[-2]
        return result

    def best_sell_3(self):
        """ 三日均價由上往下 """
        return self.data.MA(3)[1] == -1

    def best_sell_4(self):
        """ 三日均價小於六日均價 """
        return self.data.MA(3)[0][-1] < self.data.MA(6)[0][-1]

    def best_four_point_to_buy(self):
        """ 判斷是否為四大買點 """
        result = []
        if self.check_mins_bias_ratio() and \
            (self.best_buy_1() or self.best_buy_2() or self.best_buy_3() or \
             self.best_buy_4()):
            if self.best_buy_1():
                result.append(self.best_buy_1.__doc__.strip().decode('utf-8'))
            if self.best_buy_2():
                result.append(self.best_buy_2.__doc__.strip().decode('utf-8'))
            if self.best_buy_3():
                result.append(self.best_buy_3.__doc__.strip().decode('utf-8'))
            if self.best_buy_4():
                result.append(self.best_buy_4.__doc__.strip().decode('utf-8'))
            result = ', '.join(result)
        else:
            result = False
        return result

    def best_four_point_to_sell(self):
        """ 判斷是否為四大賣點 """
        result = []
        if self.check_plus_bias_ratio() and \
            (self.best_sell_1() or self.best_sell_2() or self.best_sell_3() or \
             self.best_sell_4()):
            if self.best_sell_1():
                result.append(self.best_sell_1.__doc__.strip().decode('utf-8'))
            if self.best_sell_2():
                result.append(self.best_sell_2.__doc__.strip().decode('utf-8'))
            if self.best_sell_3():
                result.append(self.best_sell_3.__doc__.strip().decode('utf-8'))
            if self.best_sell_4():
                result.append(self.best_sell_4.__doc__.strip().decode('utf-8'))
            result = ', '.join(result)
        else:
            result = False
        return result

    def best_four_point(self):
        """ 判斷買點或賣點 """
        buy = self.best_four_point_to_buy()
        sell = self.best_four_point_to_sell()
        if buy:
            return True, buy
        if sell:
            return False, sell
