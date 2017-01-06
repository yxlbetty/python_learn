# _*_ coding: utf-8 _*_
# 给 car 赋值为100 
cars = 100
space_in_a_car = 4 # 给space_in_a_car 赋值为4
drivers = 30 # 给drivers赋值为30
passengers = 90 # 给passengers 赋值 90
cars_not_driven = cars - drivers # 没有司机的车的数量为所有车减去有人的
cars_driven = drivers # 有人开的车的数量等于司机数量
carpool_capacity = cars_driven * space_in_a_car # 承载能力
average_passengers_per_car = passengers / cars_driven # 每个车的平均载人数量

# 用 python 当计算器玩玩
i = 3
j = 4
g = 5

print "There are",cars, "cars available." 
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity,"people toaday."
print "we have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."
print i + g 
print i - (j * g)
