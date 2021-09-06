"""
1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
   1.1. Adding the values in dictionary
   1.2. Updating the values in dictionary
   1.3. Accessing the value in dictionary
   1.4. Create a nested loop dictionary
   1.5. Access the values of nested loop dictionary
   1.6. Print the keys present in a particular dictionary
   1.7. Delete a value from a dictionary
"""

dict={
    101:"siva",
    102:"prasad",
    103:"satish",
    104:"venkatesh",
    105:"vamsi",
}

#Adding the value in dictionary
dict[106]="raghu"
print(dict)
#Updating the value in dictionary
dict[101]="SIVA"
print(dict)
#Accessing the value in dictionary
print(dict.get(103))
#Print the keys present in a particular dictionary
print(dict.keys())
#Delete a value from a dictionary
d=dict.pop(106)
print(d)
print(dict)

#Create a nested loop dictionary
#Access the values of nested loop dictionary

def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key, ":", value)

nested_dictionary = {"dict1": {"a": 1},"dict2": {"b": 2}}

get_all_values(nested_dictionary)


