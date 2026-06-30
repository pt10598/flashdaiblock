from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def show_image():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>已封鎖</title>
        <style>
            * { 
                margin: 0; 
                padding: 0; 
                box-sizing: border-box; 
            }
            html, body {
                width: 100%;
                height: 100%;
                overflow: hidden;
                background: #000000;
            }
            body {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .fullscreen-image {
                width: 100vw;
                height: 100vh;
                object-fit: contain;  /* 完整顯示圖片，不裁切 */
                display: block;
                background: #000000;
            }
        </style>
    </head>
    <body>
        <img class="fullscreen-image" src="/static/your_image.jpg" alt="已封鎖">
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
