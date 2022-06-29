from blog.models import users,posts

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
    return wrapper
session={}
def authentication(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user

#print(authentication(username="akhil",password="Password@123"))

class LoginView:
    def post(self,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authentication(username=username,password=password)
        if user:
            session["user"]=user[0]

        print(session)

class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts

log_in=LoginView()
log_in.post(username="akhil",password="Password@123")

all_post=PostListView()
print(all_post.get())



