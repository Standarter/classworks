#print(len(list(filter(lambda x: 800 <= x <= 1500,list(set([int("1" + str("{0:b}").format(n) + "10" if n % 2 == 0 else "11" + str("{0:b}").format(n) + "0", 2) for n in range(0, 1000)]))))))
#print(max([n for n in range(1000, 1, -1) if (int("10" + "{0:b}".format(n)[2:] + "0" if "{0:b}".format(n).count("1") % 2 == 0 else "11" + "{0:b}".format(n)[2:] + "1", 2) < 35)]))
#print(min([n for n in range(1000, 1, -1) if (int("10" + "{0:b}".format(n)[2:] + "0" if "{0:b}".format(n).count("1") % 2 == 0 else "11" + "{0:b}".format(n)[2:] + "1", 2) >= 16)]))