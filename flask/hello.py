from flask import Flask

#创建flask的应用对象
#__name__表示当前的模块名字
#              模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path="/python",  #访问静态资源的url前缀，默认值是static
            static_folder="static",  #静态文件的目录，默认就是static
            template_folder="templates",  #模板文件的目录，默认是templates
            )

@app.route("/")
def index():
    return "hello flask"
if __name__ == '__main__':
    app.run()