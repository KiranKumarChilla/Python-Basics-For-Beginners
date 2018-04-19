
# coding: utf-8

# # Python For Data Science
# 
# “Torture the data, and it will confess to anything.”
# – Ronald Coase
# 
# Grateful to Mr.Guido van Rossum, Creator of Python who made our lifes easy.
# 
# This Notebook mainly focus on python data structures and various operations that can be performed.
# 
# ## Data Structures
# Broadly Python Data Structures is classfied in to Primitive and Non primitive types
# 
# Primitive Data Structures:
# 1. Integer
# 2. Float
# 3. String
# 4. Boolean
# 
# Non Primitive Data Structures:
# 1. Array
# 2. List
# 3. Tuple
# 4. Set
# 5. Dictionary
# 6. File
#  
#  Adding to this, we also have Queues, Stacks, Graph datastructures, etc..,
# 
# Topics covered:
# 1. Integer
# 2. Float
# 3. String 
# 4. Boolean
# 5. List
# 6. Tuple
# 7. Sets
# 8. Conversions between List, Tupple, set
# 9. Dictionary
# 10. Dictionary from list,tuple and set
# 
# Will soon post the new files with topics including files, Numpy, Pandas, list comprehensions, loops, functions, lambda, classes, exception handling etc.., 

# ## General

# In[16]:


print("PythonNotes1")


# In[219]:


a = 12
print("value of a is", a)


# In[17]:


## To find data type of variable


# In[18]:


x = 2
y = "python"


# In[19]:


type(x)


# In[20]:


type(y)


# In[21]:


# to find more information about any datastructure.Use, help("data structure name")
help(int)


# ## Integer

# In[22]:


int_1 = 2
int_2 = 4


# In[23]:


# basic arithmetic operations


# In[24]:


# addition
result = int_1+int_2
print("value of int_1 + int_2 is","\t", result)
# subtraction
result = int_1-int_2
print("value of int_1 - int_2 is","\t", result)
# multiplication
result =int_1*int_2
print("value of int_1 * int_2 is","\t", result)
# Division
result =int_1/int_2
print("value of int_1 / int_2 is","\t", result)


# In[25]:


# To calculate power
result = 2**4
print("value of 2 to the power 4 is"," ",result)


# In[26]:


# To find absolute value of a integer
x = -2
result = abs(x)
print("absolute value of x(-2) is"," ", result)


# ## Float

# In[27]:


float_1 = 2.0
float_2 = 4.0


# In[28]:


#Basic Arithmetic operations
# addition
result = float_1+float_2
print("value of float_1 + float_2 is","\t", result)
# subtraction
result = float_1-float_2
print("value of float_1 - float_2 is","\t", result)
# multiplication
result = float_1*float_2
print("value of float_1 * float_2 is","\t", result)
# Division
result = float_1/float_2
print("value of float_1 / float_2 is","\t", result)


# In[29]:


# To calculate power to the float value
result = 2.3**4
print("value of 2.3 to the power 4 is"," ",result)


# In[30]:


# To find absolute value of a float value
x = -2.5
result = abs(x)
print("absolute value of x(-2.5) is"," ", result)


# #### round(x, n) x denotes the float varibale, n denotes the number of decimal places: to limit the value to limited number of decimal places

# In[31]:


round(1.1234,3)


# ## String

# In[32]:


S_1 = 'passionate about data science'
S_2 = 'machine learning'
S_3 = S_1


# In[33]:


#to find length of string
len(S_1)


# In[34]:


#print
print("first element of string S_1 is"," ",S_1[0])
print("first 10 elements of string S_1 is"," ",S_1[0:10])
print("last 10 elements of string S_1 is"," ",S_1[-10:])
print("Last element of string S_1 is"," ",S_1[-1])


# In[35]:


#concatinating two strings
S = S_1 + S_2
print("concatenated string for S_1 and S_2 is", S)


# In[36]:


#to convert entire string to upper case and lower case
S_temp = "UPPER and lower"
print("Upper case version of S_temp string is:", S_temp.upper())
print("lower case version of S_temp string is:", S_temp.lower())


# In[37]:


#strip() to remove spaces betwen start and ends is
S_temp = "     UPPER and lower  "
print("input string is: ", S_temp)
print("after removing space on both ends is", S_temp.strip())


# #### split(delimiters) :returns a list of substrings seperated by delimiters(specific characters/ tab space. etc..,)

# In[39]:


S_2 = "passionate"+"\t"+"about"+"\t"+"datascience"
S_2


# In[40]:


S_2.split("\t")


# In[41]:


S_1.split(" ")


# In[42]:


'passionate about data   science'.split()


# In[43]:


##splitlines: to split lines in string


# In[44]:


S_4 = 'python \n data science'
S_4.splitlines()


# In[45]:


# to capitalize the first character
S_1.capitalize()


# In[46]:


S_1.casefold()


# In[47]:


# centre(n,s); where n is the total length of string we are expecting; s is string that needs to be appended on eithe side if 
# given string size is less than n


# In[48]:


S_1.center(40,"a")


# In[49]:


S_1.center(10,"a")


# In[50]:


# starts with(x) will check if string starts with subbstring x or not


# In[51]:


S_3.startswith("passionate")


# In[52]:


# ends with(x)  will check if string ends with substring x or not


# In[53]:


S_1.endswith("ce")


# In[54]:


S_1.endswith("switch")


# In[55]:


#expandtabs(x) will increase the existing the tab space in the string by x times
S_3 = "testing"+"\t"+ "expandtabs"


# In[56]:


S_3.expandtabs(4)


# In[57]:


S_3.expandtabs(16)


# In[58]:


#find(x) gives the first location where x is encountered in given string


# In[59]:


S_1.find("e")


# In[60]:


S_1.find("s")


# In[61]:


S1 = '{} {}'.format('one', 'two')


# In[62]:


S1


# In[63]:


#to check if a string contains only numeric characters
S_1.isnumeric()


# In[64]:


#isspace(): to check if a given string contains only spaces


# In[65]:


S_1.isspace()


# In[66]:


S_3 = " "


# In[67]:


S_3.isspace()


# In[68]:


#zfil(n): to append the string with "0" if string size is less than n
S_1.zfill(40)


# In[69]:


#swapcase(): it converts capitals to small letters and small letters to capitals
S_4 = 'Capitals'
S_4.swapcase()


# In[70]:


## type conversion


# In[71]:


string_t = "123"
int_t = int(String_t)
int_t


# In[72]:


int_t = "456"
string_t = str(int_t)
string_t


# ## Boolean

# In[73]:


# 1 represents boolean true value and 0 represents boolean false value


# In[74]:


bool(1)


# In[75]:


bool(0)


# ## Non Primitive Data structures
# ### Note: 
#   List => [] => mutable
#   
#   Tupple => ()=>immutable
#   
#   Set => { } =>mutable, no duplicates;

# ## List

# In[76]:


list_1 = [1,2,3,4]
list_2 = [10,20]


# In[77]:


## accessing elements


# In[78]:


list_p = ["ab", "cdef", ["a","b"]]
print("element at list_p[0] is:", list_p[0])
print("element at list_p[0] is:", list_p[0][1])
print("element at list_p[2] is:", list_p[2])
print("element at list_p[2][0] is:", list_p[2][0])


# In[79]:


## copy


# In[80]:


list_3 = list_1.copy()


# In[81]:


list_3


# ### extend vs append: In extend, you can only add a list; In append, you can add an individual element or a list

# In[82]:


#extend
list_1.extend(list_3)


# In[83]:


list_1


# In[84]:


## append


# In[85]:


list_1 = [1, 2, 3, 4]
list_1


# In[86]:


list_1.append(5)


# In[87]:


list_1


# In[88]:


list_1.append(list_3)


# In[89]:


list_1


# In[90]:


list_3


# In[91]:


## index(n): it returns the location of element n


# In[92]:


list_1.index(1)


# In[93]:


list_1.index(3)


# In[94]:


## insert(i, n); inserts element n at index i 


# In[95]:


list_1 = [1, 2, 3, 4]


# In[96]:


list_1.insert(2,6)


# In[97]:


list_1


# ## tuple
# It is immutable; once values are assigned, you cannot add new values

# In[229]:


tuple_1 = (1, 2, 3, 4, 3)
tuple_2 = (10, 20)


# In[225]:


len(tuple_1)


# In[ ]:


## count(x) gives number of times element x is repeated in  the given tupple


# In[230]:


tuple_1.count(3)


# In[ ]:


# index(x) gives the index of first occurence of element x in given tupple


# In[231]:


tuple_1.index(3)


# ### pop vs remove 
# pop() removes the first element; remove(x) deletes the element x

# In[98]:


## pop


# In[99]:


list_1.pop()


# In[100]:


list_1


# In[101]:


list_1.pop()


# In[102]:


## remove


# In[103]:


list_1.remove(6)


# In[104]:


list_1


# In[105]:


##reverse


# In[106]:


list_1


# In[107]:


list_1.reverse()


# In[108]:


list_1


# ## Sets

# In[109]:


set_1 = {1, 2, 3, 4}
set_2 = {10, 20}


# In[110]:


#accessing elements
# set doessnot support indexing
print(set_1)


# In[111]:


#add


# In[112]:


set_1.add(2)


# In[113]:


set_1


# In[114]:


set_1.add(5)


# In[115]:


set_1


# ### Copy

# In[116]:


set_3 = set_1.copy()


# In[117]:


set_3


# In[118]:


set_3.add(6)


# In[119]:


set_3


# In[120]:


set_1


# In[121]:


set_1.add(7)


# In[122]:


set_1


# In[123]:


set_3


# ### difference

# In[124]:


set_1.difference(set_3)


# In[125]:


set_2.difference(set_1)


# ### difference_update

# In[126]:


set_1.difference_update(set_2)


# In[127]:


set_1


# In[128]:


set_2


# In[129]:


set_1.difference_update(set_3)


# In[130]:


set_1


# In[131]:


set_3


# ### discard

# In[132]:


set_1.discard(1)


# In[133]:


set_1


# In[134]:


set_1.discard(7)


# In[135]:


set_1


# ### add

# In[136]:


set_1 = set_3


# In[137]:


set_1


# In[138]:


set_1.add(2)


# In[139]:


set_3


# In[140]:


set_1.add(20)


# In[141]:


set_3


# ### Intersection

# In[142]:


set_1.intersection(set_3)


# In[143]:


set_1.intersection(set_2)


# ### Intersection_update

# In[144]:


set_1.intersection_update(set_2)


# In[145]:


set_1


# In[146]:


set_2


# ### isdisjoint

# In[147]:


set_1.isdisjoint(set_3)


# In[148]:


set_1.isdisjoint(set_2)


# In[149]:


set_4 = set_1


# In[150]:


set_1.isdisjoint(set_4)


# In[151]:


set_5 ={ 'A', 'B'} 


# In[152]:


set_1.isdisjoint(set_5)


# ### issubset

# In[153]:


set_1.issubset(set_2)


# In[154]:


set_1.issubset(set_5)


# In[155]:


set_1


# In[156]:


set_5


# ### Clear

# In[157]:


set_1.clear()


# In[158]:


set_2.clear()


# In[159]:


set_1


# In[160]:


set_2


# ## Conversions Among List, Set, Tuple

# In[161]:


list_1 = [1,2,3]


# In[162]:


##List to tuple


# In[163]:


tuple_1 = tuple(list_1)


# In[164]:


tuple_1


# In[165]:


##tuple to list


# In[166]:


list_2 = list(tuple_1) 


# In[167]:


list_2


# In[168]:


##set to list


# In[169]:


set_1 = {1,2,3,4}


# In[170]:


list_2 = list(set_1)


# In[171]:


list_2


# In[172]:


##set to tuple


# In[173]:


tuple_2 = tuple(set_1)


# In[174]:


tuple_2


# In[175]:


##list to set


# In[176]:


set_2 = set(list_2)


# In[177]:


set_2


# In[178]:


##list to tuple


# In[179]:


set_2 = set(tuple_2)


# In[180]:


set_2


# ## Operations on Dictionary

# In[181]:


dict_1 = {"subject":"machine learning", "group":"Data Science"}


# In[182]:


##The beauty of dictionary is you can  choose input keys from different data typesy


# In[183]:


dict_2 ={1:"AI", "Time": 12,"Students":["Jak", "Ram","emily"]}


# In[184]:


dict_2.get(1)


# In[185]:


print(dict_2.get("a")) # since there is no record that exists with key value "a"


# In[186]:


## items - to view the dictionary in more understandable way


# In[187]:


dict_1


# In[188]:


dict_1.items()


# In[189]:


## copy


# In[190]:


dict_3 = dict_1.copy()


# In[191]:


dict_3


# In[192]:


## update- to add additional key value pairs to the existing dictionary


# In[193]:


dict_temp = {"students":20, "req":"passion"} 


# In[194]:


dict_1.update(dict_temp)


# In[195]:


dict_1


# In[196]:


## clear - to empty the contents


# In[197]:


dict_temp.clear()


# In[198]:


dict_temp


# ### pop and pop item => pop will remove the record you specify; whereas popitem will by default deletes the first key value pair

# In[199]:


dict_1


# In[200]:


dict_1.pop("subject")


# In[201]:


dict_1.pop("req")


# In[202]:


dict_1


# In[203]:


dict_1.popitem()


# ## dictionary from list,tuple and set
# dict(zip(X, Y)): it creates a dictionary where elements in X are keys and elements in Y are values; X,Y  can be either list or tuple or set

# In[204]:



list_1 = [1, 2, 3]


# In[205]:


list_2 = ['a', 'b', 'c']


# In[206]:


dict_1 = dict(zip(list_1, list_2))


# In[207]:


dict_1


# In[208]:


tuple_1 = ('d', 'e', 'f')


# In[209]:


dict_1 = dict(zip(list_1, tuple_1))


# In[210]:


set_1 = {'g', 'h', 'i', 'j'}


# In[211]:


dict_1 = dict(zip(set_1, list_1))


# In[212]:


dict_1


# In[213]:


dict_1 = dict(zip(list_1, set_1))


# In[214]:


## What if we try to use X and Y with different number of elements


# In[215]:


list_1 = [1, 2, 3, 4]
set_1 = {"a", "b"}
dict_1 = dict(zip(list_1, set_1))


# In[216]:


dict_1


# In[217]:


list_1 = [1, 2]
set_1 = {"a", "b", "c", "d"}
dict_1 = dict(zip(list_1, set_1))


# In[218]:


dict_1


# ### Any Questions or suggestions, shoot me an email @ kirankchilla2@gmail.com
# ## Thank You
