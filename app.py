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
                background: #0a0a12;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                font-family: system-ui, -apple-system, sans-serif;
            }
            .container {
                background: #14141f;
                padding: 24px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.8);
                border: 1px solid #2a2a3e;
                max-width: 95vw;
            }
            img {
                max-width: 85vw;
                max-height: 80vh;
                border-radius: 12px;
                display: block;
                box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            }
            .footer {
                color: #555577;
                text-align: center;
                margin-top: 14px;
                font-size: 13px;
                letter-spacing: 0.3px;
                border-top: 1px solid #1e1e32;
                padding-top: 12px;
            }
            .footer span {
                color: #ff4444;
                font-weight: bold;
            }
            @media (max-width: 600px) {
                .container {
                    padding: 12px;
                }
                img {
                    max-width: 90vw;
                    max-height: 70vh;
                }
                .footer {
                    font-size: 11px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="/static/your_image.jpg" alt="已封鎖">
            <div class="footer">
                ⛔ <span>已封鎖</span> · 此內容已被限制存取
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)