# HNG12  1ST Task: Public API

A simple API that returns email, datetime, and GitHub repo URL.

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/4lphav01d/hng0api.git
   ```
2. Install Dependencies 
    ```
    pip install -r requirements.txt
    ```
3. Run Locally 
   ```
   python app.py
   ```


   ## API DOCUMENTATION
   Endpoint: 
   ```GET https://hng0api.pythonanywhere.com```

   ## JSON RESPONSE: 
 ```
  {
  "email": "daniel.chukwu@miva.edu.ng",
  "current_datetime": "2024-02-20T14:30:00Z",
  "github_url": "https://github.com/4lphav01d/hng0api.git"
    }
 ```