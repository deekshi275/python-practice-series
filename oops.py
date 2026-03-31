# #-----------------single level------------------------
#
# class animal:
#     def  breath(self):
#         print('breathing')
#
# class dog(animal):
#     def bark(self):
#         print('baRKING')
#
# d = dog()
# d.breath()
# d.bark()




# #-----------------multilevel ------------------------
#
# class animal:
#     def  breath(self):
#         print('breathing')
#
# class dog(animal):
#     def bark(self):
#         print('barking')
# class puppy(dog):
#     def whine(self):
#         print('whining')
# p = puppy()
# p.breath()
# p.bark()
# p.whine()


#-----------------hierarchical ------------------------

# class animal:
#     def  breath(self):
#         print('breathing')
#
# class dog(animal):
#     def bark(self):
#         print('barking')
#
# class cat(animal):
#     def meow(self):
#         print('meow')
#
# class bird(animal):
#     def chirp(self):
#         print('chik chik')
# d = dog()
# d.breath()
# c = cat()
# c.breath()
# b = bird()
# b.breath()

# #-----------------hybrid ------------------------
#
# class animal:
#     def  breath(self):
#         print('breathing')
#
# class dog(animal):
#     def bark(self):
#         print('barking')
#
# class pupy(dog):
#     def whine(self):
#         print('whine')
#
# class bird(animal):
#     def chirp(self):
#         print('chik chik')
# p = pupy()
# p.breath()
# p.whine()
# p.bark()



#-----------------multipal ------------------------
#
# class swimabels:
#     def swim(self):
#         print('swiming')
#
# class flayable:
#     def fly(self):
#         print('flying')
# class duck(swimabels,flayable):
#     pass
#
# d = duck()
# d.swim()
# d.fly()