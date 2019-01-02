#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# class GameRole:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self, p):
#         p.hp = p.hp - self.ad
#         print("%s 攻击 %s, %s 掉了 %s 血，还剩%s血" % (self.name, p.name, p.name, self.ad, p.hp))


# p1 = GameRole('盖伦', 20, 500)
# p2 = GameRole('亚索', 50, 200)
# p1.attack(p2)
# print(p2.hp)

# 组合 ： 给一个类的对象封装一个属性，这个属性是另一个类的对象

# class GameRole:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self, p):
#         p.hp = p.hp - self.ad
#         print("%s 攻击 %s, %s 掉了 %s 血，还剩%s血" % (self.name, p.name, p.name, self.ad, p.hp))
#
# class Weapon:
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#     def fight(self,p1,p2):
#         p2.hp = p2.hp - self.ad
#         print('%s 用%s 打了 %s ，掉了%s 血，还剩 %s 血' % (p1.name, self.name, p2.name, self.ad, p2.hp))
# p1 = GameRole('ace', 20, 500)
# p2 = GameRole('斯巴达国', 50, 200)
# axe = Weapon('三板斧', 60)
# broadsword = Weapon('屠龙宝刀', 100)
# axe.fight(p1,p2)
# broadsword.fight(p2,p1)
# axe.fight(p1,p2)
# broadsword.fight(p2,p1)

class GameRole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p):
        p.hp = p.hp - self.ad
        print("%s 攻击 %s, %s 掉了 %s 血，还剩%s血" % (self.name, p.name, p.name, self.ad, p.hp))

    def arm_weapon(self, wea):
        self.wea = wea


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad
    def fight(self,p1,p2):
        p2.hp = p2.hp - self.ad
        print('%s 用%s 打了 %s ，掉了%s 血，还剩 %s 血' % (p1.name, self.name, p2.name, self.ad, p2.hp))
p1 = GameRole('ace', 20, 500)
p2 = GameRole('斯巴达国', 50, 200)
axe = Weapon('三板斧', 60)
broadsword = Weapon('屠龙宝刀', 100)
p1.arm_weapon(axe)
# print(p1.wea.name)
# print(p1.wea.ad)
p1.wea.fight(p1,p2)