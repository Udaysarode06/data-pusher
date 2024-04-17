Data Pusher API Collection
1. Accounts
1.1. Create Account
Endpoint: http://localhost:8000/accounts/
Method: POST
Body:
json
Copy code
{
  "email": "example123454@example.com",
  "account_name": "Example Account",
  "website": "https://www.google.com",
  "account_id": "12345678abc"
}
1.2. List Accounts
Endpoint: http://localhost:8000/accounts/
Method: GET
1.3. Retrieve Account
Endpoint: http://localhost:8000/accounts/12345678abc
Method: GET
1.4. Update Account
Endpoint: http://localhost:8000/accounts/12345678abc/
Method: PUT
Body:
json
Copy code
{
  "email": "example12@example.com",
  "account_name": "Updated Account1",
  "website": "https://www.updatedexample.com",
  "account_id":"12345678abc"
}
1.5. Delete Account
Endpoint: http://localhost:8000/accounts/12345678abc/
Method: DELETE
2. Destinations
2.1. Create Destination
Endpoint: http://localhost:8000/destinations/
Method: POST
Body:
json
Copy code
{
  "account": "12345678abc",
  "url": "https://google.com/",
  "http_method": "POST",
  "headers": {
    "APP_ID": "12345678abc",
    "APP_SECTET": "e7tcC1rQD8-vqmLTQX95ARTObLWtS6wXrM9UZmPxT6o",
    "ACTION": "account.update",
    "Content-Type": "application/json",
    "Accept": "*"
  }
}
2.2. List Destinations
Endpoint: http://localhost:8000/destinations/
Method: GET
2.3. Get Destinations for Account
Endpoint: http://localhost:8000/accounts/12345678abc/destinations/
Method: GET
2.4. Update a particular Destination
Endpoint: http://localhost:8000/destinations/15/
Method: PUT
Body:
json
Copy code
{
  "url": "https://google.com/",
  "http_method": "PUT",
  "headers": {
    "APP_ID": "1234APPID1234",
    "APP_SECRET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s",
    "ACTION": "user.update",
    "Content-Type": "application/json",
    "Accept": "*"
  }
}
2.5. Delete a particular Destination
Endpoint: http://localhost:8000/destinations/16/
Method: DELETE
3. Incoming Data
3.1. Receive Incoming Data
Endpoint: http://localhost:8000/server/incoming_data/
Method: POST
Authentication: Bearer Token
Token: CL-X-TOKEN
Headers:
makefile
Copy code
<app_secret_token>
CL-X-TOKEN: yYgot9WVh30ndFc4EUqJSuyfxfcPnDSUTl3ox4isPrg
Body:
json
Copy code
{
  "name": "John Doe",
  "email": "john@example.com"
}
