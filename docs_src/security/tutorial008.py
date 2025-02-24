from fastapi import FastAPI, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader

# Replace with your actual API key, ideally injected as an Environment Variable
# or stored in a secure DB.
API_KEY = "mysecretapikey"

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME)

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# Apply it for all endpoints
app = FastAPI(dependencies=[Depends(verify_api_key)])

# Apply it for specific endpoints
@app.get("/secure-data")
def secure_endpoint(api_key: str = Depends(verify_api_key)):
    return {"message": "You have access to secure data"}
