# family = ["xatuna", "dima", "niko"]
# family_age = [53, 54, 13 ]
# sentence = "My moms name is: {} and age is: {}, My fathers name is: {} and age is: {}, My name is: {} and age is: {}"
# full_sentence = sentence.format(family[0],family_age[0],family[1],family_age[1],family[2],family_age[2])
# print(full_sentence)
# moms_age = 53
# fathers_age = 54 
# my_age = 13

# family = ["xatuna", "dima", "niko"]
# moms_new_age = 63
# fathers_new_age = 64
# my_new_age = 23
# new_family_age = [63, 64, 23]
# sentence = "My moms name is: {} and new_age is: {}, My fathers name is: {} and new_age is: {}, My name is: {} and new_age is: {}"
# full_sentence = sentence.format(family[0],new_family_age[0],family[1],new_family_age[1],family[2],new_family_age[2])
# print(full_sentence)
x = [2, 4, 6, 2, 4, 7, 2, 9]  #ამ სიის გამოყენებით დაწერეთ კოდი რომელიც წაშლის ორივე ოთხიანს სიიდან
for i in x:
     if(i == 4):
         x.remove(i)

print(x)


# for i in x:
#     if (i == 2):
#         x.remove(i)
# print(x)


