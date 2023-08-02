from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def read_excel_data():
    # 엑셀 파일에서 데이터를 읽어옵니다. 예시로 'data.xlsx' 파일을 사용합니다.
    df = pd.read_excel('data.xlsx')
    return df.to_dict(orient='records')

@app.route('/')
def display_data():
    # 웹 페이지 템플릿에 데이터를 전달하여 표시합니다.
    data = read_excel_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
