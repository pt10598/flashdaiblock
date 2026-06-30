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
            /* 完全重置 */
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
            
            /* 方法1: 使用背景圖片（最簡單） */
            body {
                background-image: url('/static/image.png');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            
            /* 封鎖標示 */
            .overlay {
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                color: #ffffff;
                font-family: system-ui, -apple-system, sans-serif;
                font-size: 14px;
                text-shadow: 0 2px 20px rgba(0,0,0,0.9);
                background: rgba(0,0,0,0.5);
                padding: 12px 24px;
                backdrop-filter: blur(4px);
                border-radius: 8px;
                white-space: nowrap;
                z-index: 10;
                pointer-events: none;
                border: 1px solid rgba(255,255,255,0.1);
            }
            .overlay span {
                color: #ff4444;
                font-weight: bold;
            }
            
            @media (max-width: 600px) {
                .overlay {
                    font-size: 11px;
                    padding: 8px 16px;
                    bottom: 20px;
                    white-space: normal;
                }
            }
        </style>
    </head>
    <body>
        <div class="overlay">
            ⛔ <span>已封鎖</span> · 此內容已被限制存取
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
