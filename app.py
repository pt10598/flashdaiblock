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
            body {
                background: #ffffff;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
            }
            .image-container {
                max-width: 90vw;
                max-height: 90vh;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
                border-radius: 18px;
                overflow: hidden;
                background: #ffffff;
                line-height: 0;
                transition: box-shadow 0.2s ease;
            }
            .image-container:hover {
                box-shadow: 0 12px 28px rgba(0, 0, 0, 0.08);
            }
            .image-container img {
                display: block;
                width: auto;
                height: auto;
                max-width: 100%;
                max-height: 90vh;
                object-fit: contain;
                border-radius: 18px;
            }
            
            /* 底部白色區域的標示 */
            .footer {
                position: fixed;
                bottom: 20px;
                left: 0;
                right: 0;
                text-align: center;
                color: #888888;
                font-size: 13px;
                letter-spacing: 0.3px;
                background: #ffffff;
                padding: 12px 0;
                border-top: 1px solid #eeeeee;
            }
            .footer span {
                color: #ff4444;
                font-weight: bold;
            }
            
            @media (max-width: 600px) {
                .footer {
                    font-size: 11px;
                    padding: 8px 0;
                }
            }
        </style>
    </head>
    <body>
        <div class="image-container">
            <img src="/static/image.png" alt="已封鎖">
        </div>
        <div class="footer">
            ⛔ <span>已封鎖</span> · 此內容已被限制存取
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
