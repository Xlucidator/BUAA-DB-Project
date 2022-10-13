## 0 命名规则
1.命名的方式为 当前页面/[对象]/功能。如login/login表示login页面的login功能  
2.使用HTTP自身的方法区分增删改查资源。  
 GET：查询，POST：新增，PUT：更新，DELETE：删除  
（这个我之前理解错了，不是用这些去表示请求的方法的）。  
如user/GET/users 表示在用户页面获取所有用户的信息  
3.待完善

## 1 现有命名
### login页面
login/login 登录
login/enroll 注册

### index主页
即小夏画的那两个页面  
index/application/reject 拒绝申请
index/application/consent 同意申请
index/user/GET/users  # 用户界面，获取所有用户信息
index/user/PUT/user  # 修改用户属性
index/user/DELETE/user  # 删除用户
