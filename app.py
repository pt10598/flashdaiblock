from flask import Flask, send_from_directory, send_file
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
            * { margin: 0; padding: 0; box-sizing: border-box; }
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
                object-fit: cover;
                display: block;
            }
            .overlay {
                position: fixed;
                bottom: 30px;
                left: 0;
                right: 0;
                text-align: center;
                color: #ffffff;
                font-family: system-ui, -apple-system, sans-serif;
                font-size: 14px;
                text-shadow: 0 2px 20px rgba(0,0,0,0.9);
                background: rgba(0,0,0,0.4);
                padding: 12px 20px;
                backdrop-filter: blur(4px);
                border-top: 1px solid rgba(255,255,255,0.1);
                border-bottom: 1px solid rgba(255,255,255,0.1);
                margin: 0 auto;
                width: fit-content;
                max-width: 90%;
                border-radius: 8px;
                pointer-events: none;
            }
            .overlay span {
                color: #ff4444;
                font-weight: bold;
            }
            @media (max-width: 600px) {
                .overlay {
                    font-size: 12px;
                    padding: 10px 16px;
                    bottom: 20px;
                }
            }
        </style>
    </head>
    <body>
        <img class="fullscreen-image" src="/static/image.png" alt="已封鎖">
        <div class="overlay">
            ⛔ <span>已封鎖</span> · 此內容已被限制存取
        </div>
    </body>
    </html>
    '''

# 新增一個備用路由，直接提供圖片
@app.route('/image')
def serve_image():
    return send_file('static/image.png', mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
