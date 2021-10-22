values1 = (1,3,"hello")
str1 = "abc %d,  xyz %d,  %s world" 
print(str1 % values1)

values2 = {'title':'极客起源', 'url':'https://geekori.com', 'company':'欧瑞科技'}

str2 = """
<html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8" /> 
    <head>
    <body>
        <h1>{title}</h1>
        <a href="{url}">{company}</a>
    </body>
</html>
"""
print(str2.format_map(values2))

