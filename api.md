## 0 命名规则
1.命名的方式为 当前页面/[对象]/功能。如login/login表示login页面的login功能  
2.使用HTTP自身的方法区分增删改查资源。  
 GET：查询，POST：新增，PUT：更新，DELETE：删除  
（这个我之前理解错了，不是用这些去表示请求的方法的）。  
如user/GET/users 表示在用户页面获取所有用户的信息  
3.返回值为json：
JsonResponse({'request': SUCCESS_DATA, 'result': result})  
其中request域存放着该次请求的成功与否以及相关信息，reslut域则为数据库的一些返回值

## 1 现有命名
### login页面

| 功能 | 接口名       | 前端传递参数       | 后端返回参数（不包含request） |
| ---- | ------------ | ------------------ | ----------------------------- |
| 登录 | login/login  | CodeName, Password | token                         |
| 注册 | login/enroll | 单个用户所有信息   |                               |

### index主页
即小夏画的那两个页面   

|功能 | 接口名  |  前端传递参数|后端返回参数（不包含request）|  |
|:---:|:---:|:---:|:---:|
|获取所有用户信息| index/user/|token|所有用户所有信息|
|获取单个用户信息| index/user/GET/user|token|单个用户所有信息|
|修改用户属性| index/user/PUT/user|token，单个用户所有信息|
|删除用户| index/user/DELETE/user|token，删除用户的用户名||
|同意注册申请|index/application/consent|token，申请用户用户名|
|拒绝注册申请|index/application/reject|token，申请用户用户名|
|修改等待队列的属性|index/application/PUT/application|token,待修改用户的所有信息||

### message页面

| 功能 | 接口名 | 前端传递参数 | 后端返回参数 |
| ---- | ------ | ------------ | ------------ |
|      |        |              |              |

