# d = {
#     "personal_info": {
#         "name": "nicholas becker",
#         "pets": [{"dogs","new puppy"}]
#     {"location": [{"concord","california"}]
#
#
#     }
# }
#
# print(d["personal_info"]["name"])
p = [{
    'name': "Nickbecker",
    'age':  15
},
{
    'name': "Adam Braus",
    'age':  29
},
{
    'name': "Jon Boy",
    'age':  45
}]
def names_ages(people):
    adults_arr=[]
    for p in people:
        if p["age"] >= 18:
            adults_arr.append(p)

    return adults_arr

f = names_ages(p)
print(f)
