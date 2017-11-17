def highest_affinity(site_list, user_list, time_list):
    user2site = dict()
    for site, user in zip(site_list, user_list):
        if user not in user2site:
            user2site[user] = []
        if site not in user2site[user]:
            user2site[user].append(site)

    #affinity2user is a map from affinity to a set of users
    affinity2user = dict()
    for user in user2site:
        user2site[user].sort()

    for user in user2site:
        sites = user2site[user]
        for i in range(len(sites) - 1):
            for j in range(i + 1, len(sites)):
                affinity = (sites[i], sites[j])
                if affinity not in affinity2user:
                    affinity2user[affinity] = set()
                affinity2user[affinity].add(user)

    max_count = 0
    max_affinity = ()

    for affinity in affinity2user:
        users = affinity2user[affinity]
        if len(users) > max_count:
            max_count = len(users)
            max_affinity = affinity

    return max_affinity

def nothing1():
    pass

def nothing2():
    pass

def nothing3():
    pass

def nothing4():
    pass

def nothing5():
    pass

def nothing6():
    pass

def nothing7():
    pass

def nothing8():
    pass

def nothing9():
    pass

def nothing10():
    pass

def nothing11():
    pass

def nothing12():
    pass

def nothing13():
    pass

def nothing14():
    pass

def nothing15():
    pass

def nothing16():
    pass

def nothing17():
    pass

def nothing18():
    pass

def nothing19():
    pass

def nothing20():
    pass

def nothing21():
    pass

def nothing22():
    pass

def nothing23():
    pass

def nothing24():
    pass

def nothing25():
    pass

def nothing26():
    pass

def nothing27():
    pass

def nothing28():
    pass

def nothing29():
    pass

def nothing30():
    pass

def nothing31():
    pass

def nothing32():
    pass