<h1>Username and password proxy authentication with Selenium Chrome</h1>
**Note: At the time of writing this proxy authentication method works only while running a Selenium in headful mode**
 
To authenticate proxies with username and password on Selenium the most common approach on various programming languages is to write a custom extension which would handle the proxy connection.

The proxies function in the provided extension.py file can be imported and easily used in any project as given in the main.py example.
The  function expects 4 values: **username**, **password**, **endpoint** and **port**.

The extension is added using the `add_extension` method.