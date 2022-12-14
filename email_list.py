# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
# generate a list that contains complete email addresses (e.g. diana.prince@gmail.com)

def email_list(domains):
    emails = []
    for users in domains:
        for user in domains[users]:
            emails.append("{}@{}".format(user,users))
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))