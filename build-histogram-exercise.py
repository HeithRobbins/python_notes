"""jordans solution"""

"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

# sales = {
#   'google': 20,
#   'facebook': 42,
#   'twitter': 10,
#   'offline': 12,
# }

# print('g ' + sales['google'] * '$')
# print('f ' + sales['facebook'] * '$')
# print('t ' + sales['twitter'] * '$')
# print('o ' + sales['offline'] * '$')




'''daniels solution'''

sales = {
  'google': 20,
  'facebook': 42,
  'twitter': 10,
  'offline': 12,
}

def histogram(sales_data):
    for company, sales in sales_data.items():
        print(company[0], sales * '$')
        
        
histogram(sales)
    











# companies = {
#     'google': 4,
#     'facebook': 8,
#     'twitter': 12,
#     'snapchat':6,
# }

# def get_dat_doh():
#     print(companies)
#     container = []
#     for key, value in companies.item():
#         print(companies["google"]) 


# get_dat_doh()
# print(get_dat_doh)