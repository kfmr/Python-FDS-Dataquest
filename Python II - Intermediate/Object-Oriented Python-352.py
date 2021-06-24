## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
print(type(l))
print(type(s))
print(type(d))

## 3. Defining a Class ##

# instanciar uma classe
class MyClass:
    pass

## 4. Instantiating a Class ##

class MyClass:
    pass
# instacia de um objeto da classe
my_instance = MyClass()
print(type(my_instance))

## 5. Creating Methods ##

class MyClass:
    # definição do método da classe 
    def first_method():
        return "This is my first method"
    
my_instance = MyClass()

## 6. Understanding 'self' ##

class MyClass:
    # self = faz referencia ao proprio objeto
    # self representa a propria instância - is the instance itself
    def first_method(self):
        return "This is my first method"

my_instance = MyClass()

result = my_instance.first_method()
print(result)

## 7. Creating a Method That Accepts an Argument ##

class MyClass:
    # a cada definição de métodos e atributos, é necessário passar o argumento self ("phantom argument") que é o proprio objeto
    def first_method(self):
        return "This is my first method"
    
    def return_list(self,input_list):
        return input_list
    
my_instance = MyClass()
result = my_instance.return_list([1,2,3])
        

## 8. Attributes and the Init Method ##

class MyList:
    def __init__(self, initial_data):
        self.data = initial_data
        
        
my_list = MyList([1, 2, 3, 4, 5])
print(my_list.data)

## 9. Creating an Append Method ##

class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        
    # Recreate the functionality of the list.append() from the built-in Python list class.
    def append(self, new_item):
        self.data = self.data + [new_item]
    
my_list = MyList([1, 2, 3, 4, 5])
print(my_list.data)
my_list.append(6)
print(my_list.data)

## 10. Creating and Updating an Attribute ##

class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calcula o tamanho inicial da lista passada como argumento no initial_data
        self.length = 0
        for item in self.data:
            self.length += 1

            # recria o append ao adicionar o novo elemento a ultima posição da lista
    def append(self, new_item):
        self.data = self.data + [new_item]
        # Update the length here
        self.length +=1
        
my_list = MyList([1, 1, 2, 3, 5])
print(my_list.length)
my_list.append([9,0])
print(my_list.data)
print(my_list.length)