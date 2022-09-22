# 项目结构
项目总目录：运行`django-admin startproject db-project`得来

`/backend`：为django的app，在项目根目录中运行`django-admin startapp backend`得来

`/frontend`：为vue3项目，在项目根目录中运行`vue create frontend -n`得来（`-n`参数表示不自动添加.git）

# 项目安排
俺现在还是很不太懂这种搭配前后端怎么分工合作，再等等qwq

# 软件版本
### 后端相关
- python 3.10.6
- pip 22.2.1
- django 4.1.1 （根据官网提示下载的，`pip install Django==4.1.1`；`python -m django --version`查看）

### 前端相关
- node.js v16.17.0 （官网下载的包再添加环境变量；`node -v`查看）
- npm 8.15.0 （node.js的包管理软件，应该自带；`npm -v`查看）
- cnpm （按菜鸟教程所说搞了个cnpm，[使用淘宝 NPM 镜像](https://www.runoob.com/nodejs/nodejs-npm.html#taobaonpm)）
~~- @vue/cli 5.0.8 （官方命令行工具，应该是接着用了`cnpm install -g @vue/cli`装的；`vue --version`或`vue -V`查看）~~
- vue 3.2.39 （应该是使用`cnpm install vue@next`装的vue3；`npm list vue`查看）
- vite 3.1.3（新型前端构建工具，pycharm终端输入`npm init vite@latest frontend -- --template vue`，按提示安装`create-vite@latest`，再按提示完成`cd frontend`、`npm install`即安装完毕，`vite -v`查看）

### 数据库相关
- MySQL: 装了一堆，主要的都是8.0 


# 运行方法

- 后端：直接点击run
- 前端：进入`/frontend`目录，在终端输入`npm run dev`（别忘记ctrl-c，再输入Y停止）