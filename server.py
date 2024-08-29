from flask import Flask, request, jsonify
from captcha import slider_validation
app = Flask(__name__)


@app.route('/api/login', methods=['GET'])
def get_data():
    # 获取请求中的 JSON 数据
    url = request.args.get("url")
    token = slider_validation(url)
    # 这里可以添加处理 URL 的逻辑
    # 示例：假设我们只是返回一些静态数据
    if token and token != "":
        response_data = {
            'url_received': url,
            'token': token,
            "code": 200,
        }
    else:
        response_data = {
            'url_received': url,
            "code": -1,
        }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, port=5245)