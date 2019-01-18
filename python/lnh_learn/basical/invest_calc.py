#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# money = 10000
# rate = 0.131
# total_month = 36
# invest_months = 36
# circle = total_month/invest_months
#
#
# for i in range(int(circle)):
#     money = money * rate * invest_months / 12 + money
#     print(money)

# 目标计算
# increase_money = 60000
# target_money = 1200000
# total_money = 150000
# money_rate = 0.128
# year = 0
# while total_money < target_money:
#     year += 1
#     total_money = total_money + increase_money + total_money * money_rate
#     print("第%s年的总收益为%s" % (year,total_money))


# 年化收益计算
# init_money = 10000
# total_year = 25
# inv_rate = 0.1
# for i in range(total_year):
#     init_money = init_money*(1+inv_rate)
#     print(init_money)

# 递增年化收益计算
init_money = 150000
per_year_money = 30000
total_year = 30
inv_rate = 0.12
add_money = 20000
for i in range(5):
    init_money = init_money*(1+inv_rate) + per_year_money
    print("第%d年资产%d: " % (i+1, init_money))
    print("第%d年 年储蓄 %d：" % (i+1, per_year_money))
    per_year_money += add_money

inv_rate = 0.18
for i in range(15):
    init_money = init_money*(1+inv_rate) + per_year_money
    print("第%d年资产%d: " % (i+1, init_money))
    print("第%d年 年储蓄 %d：" % (i+1, per_year_money))
    per_year_money += add_money

