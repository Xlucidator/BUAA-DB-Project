# 一些出现的问题及解决方法


## 0 关于npm

有时候缺少一些插件需要安装，发现直接用`npm xxx`会报错，认为我的python源码有的地方少了括号等奇怪问题。这种时候用`cnpm xxx`即可解决。

## 1 关于router

在加入`router`之后，发现`App.vue`中的内容会被执行两次。一开始还以为是`mount`了两次，或者是`<router-view>`标签被放在了什么循环里导致执行了两次。后来认真阅读了所有涉及到`App.vue`的程序，在`/router/index.js`中发现了可疑语句。也就是说，`App.vue`被启动了之后，还被当成了组件，于是内容就出现了两次。

![image-20220923104526275](problems/image-20220923104526275.png)

```javascript
const routes = [
    {
        path: '/',
        //component: App,               // 这一行删去即可
        children: [...]
        ...
    }
```

## 关于运行

输入`npm run dev` 后报错 `'vite' 不是内部或外部命令,也不是可运行的程序 或批处理文件`。

解决方法：https://blog.csdn.net/m0_55070913/article/details/123374448，即删除`node_modules`目录和`package-lock.json`文件，重新`npm install`。










