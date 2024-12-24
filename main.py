from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5020))
    # 5020 là port mặc định, thay đổi thành bất kỳ port nào cũng được
    # khi run docker thì dùng lệnh  'docker run -p {port mình muốn ở local của mình khi chạy docker}:{là port setup ở hàng trên} -d'
    app.run(debug=True, host='0.0.0.0', port=port)