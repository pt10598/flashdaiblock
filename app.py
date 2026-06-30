from flask import Flask, send_from_directory, send_file
import os

app = Flask(__name__)

@app.route('/')
def show_image():
    # 檢查圖片是否存在
    img_path = 'static/image.png'
    img_exists = os.path.exists(img_path)
    img_size = os.path.getsize(img_path) if img_exists else 0
    
    # 列出 static 資料夾內容
    static_files = os.listdir('static') if os.path.exists('static') else []
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>已封鎖 - 診斷模式</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                background: #ffffff;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                font-family: system-ui, sans-serif;
                padding: 20px;
            }}
            .info-box {{
                background: #f5f5f5;
                padding: 30px;
                border-radius: 12px;
                max-width: 500px;
                width: 100%;
                margin-bottom: 20px;
                border: 1px solid #ddd;
            }}
            .info-box h2 {{
                color: #333;
                margin-bottom: 15px;
                font-size: 18px;
            }}
            .info-item {{
                padding: 8px 0;
                border-bottom: 1px solid #eee;
                color: #555;
            }}
            .info-item:last-child {{
                border-bottom: none;
            }}
            .status-ok {{ color: #22aa44; font-weight: bold; }}
            .status-error {{ color: #ff4444; font-weight: bold; }}
            
            .image-container {{
                max-width: 90vw;
                max-height: 85vh;
                border-radius: 18px;
                overflow: hidden;
                background: #ffffff;
                line-height: 0;
                box-shadow: 0 8px 20px rgba(0,0,0,0.05);
            }}
            .image-container img {{
                display: block;
                width: auto;
                height: auto;
                max-width: 100%;
                max-height: 85vh;
                object-fit: contain;
            }}
            .footer {{
                position: fixed;
                bottom: 20px;
                left: 0;
                right: 0;
                text-align: center;
                color: #888888;
                font-size: 13px;
                background: #ffffff;
                padding: 12px 0;
                border-top: 1px solid #eeeeee;
            }}
            .footer span {{ color: #ff4444; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="info-box">
            <h2>📁 診斷資訊</h2>
            <div class="info-item">
                圖片檔案: 
                <span class="{'status-ok' if img_exists else 'status-error'}">
                    {'✅ 存在' if img_exists else '❌ 不存在'}
                </span>
            </div>
            <div class="info-item">
                圖片大小: 
                <span class="{'status-ok' if img_size > 0 else 'status-error'}">
                    {img_size} bytes {'✅' if img_size > 0 else '❌'}
                </span>
            </div>
            <div class="info-item">
                static/ 資料夾內容: 
                <span class="{'status-ok' if static_files else 'status-error'}">
                    {', '.join(static_files) if static_files else '❌ 空的或不存在'}
                </span>
            </div>
            <div class="info-item">
                圖片路徑: 
                <span style="font-family: monospace; font-size: 12px;">/static/image.png</span>
            </div>
        </div>
        
        <div class="image-container">
            <img src="/static/image.png" alt="已封鎖">
        </div>
        
        <div class="footer">
            ⛔ <span>已封鎖</span> · 此內容已被限制存取
        </div>
    </body>
    </html>
    '''

# 額外路由：直接提供圖片
@app.route('/static/image.png')
def serve_image():
    return send_file('static/image.png', mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
