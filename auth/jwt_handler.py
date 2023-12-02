import time
from datetime import datetime
from fastapi import HTTPException, status
from jose import jwt, JWTError
from settings.app_settings import get_settings
 

settings = get_settings()
def create_access_token(user:str)->str:
    payload = {'user':user,
               'expires':time.time()+ 3600}
    token = jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
    return token

def verify_access_token(token:str)->dict:
    try:
        data = jwt.decode(token, settings.SECRET_KEY,algorithms=["HS256"])
        expires = data.get('expires')
        if expires is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="No access token supplied")
        if datetime.utcnow() > datetime.utcfromtimestamp(expires):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!"
            )  
        return data          
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token"
        )
