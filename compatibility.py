compatible = {
    'O+': '''Minor antigen discrepancies (e.g., Kell, Duffy, etc.) may lead to delayed hemolytic attacks. Recipients might experience mild allergic reactions and fever due to interactions with donor WBCs.''',
    'O-': '''Minor antigen discrepancies (e.g., Kell, Duffy, etc.) may lead to delayed hemolytic attacks. Recipients might experience mild allergic reactions and fever due to interactions with donor WBCs.''',
    'A+': '''Recipients may experience mild allergies. Minor antigens like Lewis may lead to hemolytic reactions.''',
    'A-': '''Recipients may experience mild allergies. Minor antigens like Lewis may lead to hemolytic reactions.''',
    'B+': '''Variation in antigens like MNS may lead to hemolytic reactions and allergic responses.''',
    'B-': '''Variation in antigens like MNS may lead to hemolytic reactions and allergic responses.''',
    'AB+': '''Rh antigen discrepancies may lead to allergic reactions and fever in recipients.''',
    'AB-': '''Rh antigen discrepancies may lead to allergic reactions and fever in recipients.'''
}

all_blood_groups = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']

recievers = {
    'O+': ['O+', 'O-'],
    'O-': ['O-'],
    'A+': ['A+', 'A-', 'O+', 'O-'],
    'A-': ['A-', 'O-'],
    'B+': ['B+', 'B-', 'O+', 'O-'],
    'B-': ['B-', 'O-'],
    'AB+': all_blood_groups,
    'AB-': ['A-', 'B-', 'AB-', 'O-']
}

def compatiblity_checking(donor_blood_group, receiver_blood_group):
    donor_blood_group = donor_blood_group.upper()
    receiver_blood_group = receiver_blood_group.upper()

    possible_donors = recievers.get(receiver_blood_group)

    if possible_donors is None:
        return ["Invalid receiver blood group."]
    
    if donor_blood_group in possible_donors:
        description = compatible.get(receiver_blood_group, "No additional information.")
        return ['Compatible', description]
    else:
        return ["Not Compatible"]