profile = {'First Name' : 'Darryl', 'Last Name' : 'Diapolet', 'Age' : 25 }

def get_first_name():
    return profile['First Name']

def get_last_name():
    return profile['Last Name']

def get_age():
    return profile['Age']

def get_full_name():
    return get_first_name() + ' ' + get_last_name()

print("Hi, My name is " + get_full_name() + ". I am %d" % profile['Age'] + " years old.")


def update_age(profile, value):
    profile['Age'] = value;
    return profile['Age']

print("Updated Age", update_age(profile, 26))

def add_new_entry(profile, index, value):
    profile[index] = value;
    return profile

def remove_entry(profile, index):
    del profile[index];
    return profile

def clear_profile(profile):
    profile.clear();
    return profile

print("Added School", add_new_entry(profile, 'School', 'UIC'))
print("Remove Age", remove_entry(profile, 'Age'))
print("Clear Profile", clear_profile(profile))
