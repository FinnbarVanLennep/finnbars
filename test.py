
def between(test_obj, old_loc, new_loc):
    if (test_obj >= old_loc and test_obj <= new_loc) or (test_obj <= old_loc and test_obj >= new_loc):
        return True
    else: return False

if between(6,1,5):
    print(between(6,1,5))

print(between(6,1,5))