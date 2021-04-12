<h2>Username and password proxy authentication with Selenium Chrome</h2>

**Note: At the time of writing this proxy authentication method works only while running a Selenium in headful mode**
 
To authenticate proxies with username and password on Selenium the most common approach on various programming languages is to write a custom extension which would handle the proxy connection. Such an extension is shown in extension.py example.

The proxies function in the provided extension.py file can be imported and easily used in any project as given in the main.py example.
The  function expects 4 values: **username**, **password**, **endpoint** and **port**.

`proxies_extension = proxies(username, password, endpoint, port)`

The extension is then added using the `add_extension` method:

`chrome_options.add_extension(proxies_extension)`

This example can be easily adapter for use in other programming languages as well as supported webdrivers.
