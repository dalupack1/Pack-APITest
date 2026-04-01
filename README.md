Thank you for the opportunity
API Tests Cases 

1.Verify all breeds endpoint returns 200  
BSend GET request to /breeds  
Expected: Status code 200  

2.Verify response is not empty  
AValidate response contains data  
Expected: Data list length > 0  

3.Verify breed contains name attribute  
Check first breed object  
Expected: name field exists  

4.Verify breed contains life span  
Validate attributes include life span  
Expected: life field exists  

5.Verify invalid endpoint returns 404  
Send request to /invalid  
Expected: Status code 404  

6,Verify response time is under 2 seconds  
Measure API response time  
Expected: < 4 seconds  

UI test cases 

7.Verify website loads successfully  
Open homepage  
Expected: Page title contains "Dog"  

8.Verify page contains content  
Inspect page body  
Expected: Text contains "Dog" 

 
