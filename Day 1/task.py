#დავალება:

#მომხმარებელს შეეკითხეთ ხელფასი

#თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?

#თუ 1000----10000 -ია , დაუპრინტეთ you mid

#თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

salary_score = float(input("შეიყვანე ხელფასი: "))

if salary_score>=10000:
    print("შენი ხელფასია: " + str(salary_score) + " გოა-ში სწავლობდი")
elif salary_score > 1000 and salary_score < 10000:
    print("შენი ხელფასია: " + str(salary_score) + " you mid")
elif salary_score < 1000:
    print("შენი ხელფასია: " + str(salary_score) + " შემოსულიყავი გოაში, მატრიცელო")