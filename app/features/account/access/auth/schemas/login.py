from app.toolbox import BaseSchema,PasswordMixin,BaseReadSchema

# ================================LOGIN===========================

class LoginBase(BaseSchema,PasswordMixin):
    login: str  

class LoginSchema(LoginBase):
    pass

class LoginResponse(LoginBase):
    pass
   