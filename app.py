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
                overflow: hidden;  /* 移除滾動條 */
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
                object-fit: cover;  /* 圖片填滿整個畫面，可能裁切 */
                display: block;
            }
            /* 如果不想裁切圖片，改用 contain（完整顯示但可能有黑邊） */
            /*
            .fullscreen-image {
                width: 100vw;
                height: 100vh;
                object-fit: contain;
                background: #000000;
            }
            */
            
            /* 封鎖標示 - 浮在圖片上方 */
            .overlay {
                position: fixed;
                bottom: 30px;
                left: 0;
                right: 0;
                text-align: center;
                color: #ffffff;
                font-family: system-ui, -apple-system, sans-serif;
                font-size: 14px;
                letter-spacing: 0.5px;
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
                pointer-events: none;  /* 讓點擊穿透 */
            }
            .overlay span {
                color: #ff4444;
                font-weight: bold;
            }
            
            /* 手機優化 */
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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
