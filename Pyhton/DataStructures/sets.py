students_trial_course = {"ram", "sham", "radha", "mahesh", "magesh"}
students_bought_course = {"radha", "magesh"}
students_showed_interest  = {"ram", "sham", "radha"}

students_showed_interest.add("ganesh")
students_showed_interest.add("ganesh")
students_showed_interest.add("ganesh")

#Who tried but didn't buy? (difference)

target1 = students_trial_course - students_bought_course
print(target1)

# Who bought but didn’t take trial?
talk_to = students_bought_course - students_trial_course
print(talk_to)

#Who tried and also showed interest?
sales_list = students_trial_course & students_showed_interest
print(sales_list)
