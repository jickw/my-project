#!/usr/bin/env python
# -*- encoding: utf-8 -*-

money = 10000
rate = 0.131
total_month = 36
invest_months = 36
circle = total_month/invest_months


for i in range(int(circle)):
    money = money * rate * invest_months / 12 + money
    print(money)

