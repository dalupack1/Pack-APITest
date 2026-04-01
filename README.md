API Tests Cases 

Verify all breeds endpoint returns 200  

Send GET request to /breeds  

Expected: Status code 200  

Verify response is not empty  

Validate response contains data  

Expected: Data list length > 0  

Verify breed contains name attribute  

Check first breed object  

Expected: name field exists  

Verify breed contains life span  

Validate attributes include life span  

Expected: life field exists  

Verify invalid endpoint returns 404  

Send request to /invalid  

Expected: Status code 404  

Verify response time is under 2 seconds  

Measure API response time  

Expected: < 4 seconds  

UI test cases 

Verify website loads successfully  

Open homepage  

Expected: Page title contains "Dog"  

Verify page contains content  

Inspect page body  

Expected: Text contains "Dog" 

 
