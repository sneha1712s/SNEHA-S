my_dict = {'apple':10,'banana':20,'angel':30,'balaji':40,'chennai':100,'zebra':120}

for key,value in my_dict.items():
    if key[2].lower()=='l':
        print(f"rhe value of '{key}' is {value}")
