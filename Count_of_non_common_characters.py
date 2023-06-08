def count_non_common_characters(s1,s2):
    s1_lower=s1.lower()
    s2_lower=s2.lower()
    
    set1=set(s1_lower)
    set2=set(s2_lower)
    non_common_characters=set1.union(set2)-set1.intersection(set2)
    count=0
    for char in non_common_characters:
        if char.isalnum():
            count+=1
    return count
    
s1=input()
s2=input()
result=count_non_common_characters(s1,s2)
print(result)