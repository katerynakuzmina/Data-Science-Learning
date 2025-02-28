# class User:
#      def __init__(self, username, email):
#          self.username = username
#          self.email = email

# class AdminUser(User):
#     def __init__(self, username, email, role):
#         super().__init__(username, email)
#         self.role = role
#         self.is_admin = True

# my_admin = AdminUser('admin123', 'admin@admin.com', 'Administrator')
# print(my_admin)
# print(type(my_admin))
# print(isinstance(my_admin, AdminUser))
# print(isinstance(my_admin, User))
# print(isinstance(my_admin, object))

# print(my_admin.__dict__)

# my_user = User('bob234', 'bob@bob.com')
# print(my_user.__dict__)

# print(User.__subclasses__())
# print(object.__subclasses__())



# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

# class Post:
#     def __init__(self, title, content, author):
#         self.title = title
#         self.content = content
#         self.author = author

# class Forum:
#     def __init__(self):
#         self.users = []
#         self.posts = []

#     def register_user(self, username, email):
#         user = User(username, email)
#         self.users.append(user)
#         return user

#     def create_post(self, title, content, author):
#         post = Post(title, content, author)
#         self.posts.append(post)
#         return post
    
#     def find_user_by_username(self, username):
#         for user in self.users:
#             if user.username == username:
#                 return user

#     def find_user_by_email(self, email):
#         for user in self.users:
#             if user.email == email:
#                 return user
            
#     def find_post_by_author(self, author):
#         found_posts = []
#         for post in self.posts:
#             if post.author == author:
#                 found_posts.append(post)
#         return found_posts

# forum = Forum()

# katya = forum.register_user('katya123', 'katya@gmail.com')
# alice = forum.register_user('alice123', 'alia@gmail.com')

# print(forum.users)

# forum.create_post("My first post", "Post Content", katya)
# print(forum.posts)

# #Do NOT use this way to search. USE function find_post_by_author
# # print(forum.posts[0].title)
# # print(forum.posts[0].content)
# # print(forum.posts[0].author.username)
# # print(forum.posts[0].author.email)

# print(forum.find_user_by_username('admin123')) # None
# print(forum.find_user_by_username('alice123'))
# print(forum.find_user_by_username('alice123').email) # alia@gmail.com
# print(forum.find_user_by_email('alia@gmail.com').username)

# forum.create_post("Second Post", "Post post content", katya)
# print(forum.posts)
# posts_list = forum.find_post_by_author(katya)
# print(posts_list[1].title)
# found_posts_titles = [post.title for post in posts_list]
# print(found_posts_titles)

# #Find user by email and find all posts by that user
# user_email = 'katya@gmail.com'
# found_user = forum.find_user_by_email(user_email)
# if found_user:
#     print(forum.find_post_by_author(found_user))
# else: 
#     print(f"User with email {user_email} doesn't exist")




#Encapsulation

# class Email:
#     def __init__(self, sender, recipient, subject, body):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = body

#     def send_email(self):
#         #Login related to sending email
#         pass

#     def read_email(self):
#         #Login related to reading email
#         pass


#Inheritance

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start(self):
#         # Code to start the vehicle
#         pass

#     def stop(self):
#         # Code to stop the vehicle
#         pass


# class Car(Vehicle):
#     def __init__(self, make, model, doors_qty):
#         super().__init__(make, model)
#         self.doors_qty = doors_qty

#     def lock_doors(self):
#         # Logic to lock doors
#         pass

#     def unlock_doors(self):
#         # Logic to unlock doors
#         pass

#Polytmorphism
# import math

# class Shape:
#     def calc_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calc_area(self):
#         return math.pi * pow(self.radius, 2)
        
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calc_area(self):
#         return self.width * self.height

# shapes = [Circle(5), Rectangle(10, 2), Circle(7), Rectangle(25, 15)]

# for shape in shapes:
#     print(shape.calc_area())


#Abstraction
# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def process_payment(self):
#         pass


# class CreditCardPayment(Payment):
#     pass


# class StripePayment(Payment):
#     def process_payment(self):
#         pass


# class PayPalPayment(Payment):
#     def process_payment(self):
#         pass

