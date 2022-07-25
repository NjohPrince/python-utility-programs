import webbrowser  # webbrowser module

f = open('20-mini-projects-in-python/mini_web_page/helloworld.html', 'w')

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Page Created Using Python</title>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            width: 100%;
            min-height: 100vh;
            display: flex;
            display: -ms-flexbox;
            align-items: center;
            justify-content: center;
            background: #000;
        }
        h1 {
            color: #fff;
            font-size: 50px;
        }
    </style>
</head>
<body>
    <h1>Hello World... Python is Fun!!!</h1>
</body>
</html>
"""

# write html conten tto html file
f.write(html_doc)
f.close()

# opening the web page -will use your default browser
webbrowser.open_new_tab(
    '20-mini-projects-in-python\mini_web_page\helloworld.html')
