# 如何推送笔记到github
1. 步骤一：在本地初始化Git仓库
   > `cd 项目路径`
   > `git init`
2. 步骤二：添加文件并提交到暂缓区
   > `git add .` 提交所有文件
   > `git add git.md` 提交某个文件
   > `git commit -m "提交git.md"` 评论信息
3. 步骤三：连接远程仓库
   > * 第一次提交:
   > `git remote add origin https://github.com/你的用户名/你的仓库名.git` 
   > * 已经设置过origin:
   > `git remote set-url origin https://github.com/你的用户名/你的仓库名.git`   
4. 步骤四：推送到github远程仓库
   > * 推送到main分支：
   > `git push -u origin main`
   > * `git status` 可以查看改动
5. 一些配置
   > * 设置Git的用户名和邮箱，一般在`git init`后会用
   > `git config --global user.name "昵称"`
   > `git config --global user.email "邮箱"`
   > * 设置代理
   > `git config --global http.proxy http://127.0.0.1.7890`
6. 一些疑问
   > * 修改过的仓库内容如何重新push
   >    ```
   >    git add 文件名
   >    git commit -m "说明"
   >    git push
   >    ```
   >    1. 第一次`git remote add origin https://github.com/Zhiyehhh/cainiaocangku.git`
   告诉Git这个本地仓库对应的远程仓库是origin,对应着那个地址
   >    2. 第一次`git push -u origin main`
   把 main 分支默认绑定到 origin 的 main 分支上
   >    3. 查看当前仓库绑定的远程仓库
   >    `git remote -v`
