
# Similarity Check System

## 项目介绍

该项目是一个基于 **Django** 和 **Vue 3** 构建的相似度检测系统，主要用于学生作业提交的相似度检测与分析。系统分为**学生端**和**教师端**，其中学生端用于提交作业、查看作业成绩、查看推荐练习题等功能，而教师端则用于发布题目、管理班级、查看作业相似度等。

项目的代码托管在 GitHub 上，访问链接：[Graduation Project - GitHub](https://github.com/RuiqiYing/CodeSimility)

## 技术栈

- **后端**：Django
- **前端**：Vue 3
- **数据库**：SQLite
- **其他**：Vue Router, Vuex, Axios

## 安装与运行

### 后端安装与配置

1. 克隆项目：
   ```bash
   git clone https://github.com/RuiqiYing/Graduation-project_YingRuiqi.git
   cd Graduation-Project/code/BackEnd
   ```

2. 安装 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行数据库迁移：
   ```bash
   python manage.py migrate
   ```

4. 启动 Django 服务：
   ```bash
   python manage.py runserver
   ```

### 前端安装与配置

1. 在 `code/FrontEnd` 目录下，使用以下命令安装前端依赖：
   ```bash
   npm install
   ```

2. 启动 Vue 3 开发服务器：
   ```bash
   npm run serve
   ```

### 项目结构

#### 后端

```
code/
  BackEnd/
    ├── .idea/                 # IDE 配置文件
    ├── similarity/            # 后端主要代码
    ├── db.sqlite3             # SQLite 数据库
    ├── manage.py              # Django 项目管理文件
```

#### 前端

```
code/
  FrontEnd/
    ├── src/
    │   ├── assets/           # 静态资源
    │   ├── components/       # 公共组件
    │   ├── Home/             # 教师端与学生端复用页面
    │   ├── Student/          # 学生端页面
    ├── public/
    ├── package.json          # 前端依赖配置
    ├── vue.config.js         # Vue 配置文件
```

### 功能说明

#### 学生端

- **登录/注册**：
  - 使用手机号作为用户ID，注册时需要填写密码和基本信息。
- **主页面**：
  - 推荐练习题和作业管理。
- **作业管理**：
  - 显示未完成和已提交的作业，支持查看答案。
- **个人信息管理**：
  - 修改昵称、个性签名、查看做题数量等。

#### 教师端

- **登录/注册**：
  - 根据按钮区分教师或学生，进入不同页面
- **班级与作业管理**：
  - 可以发布题目，查看班级整体作业相似度。
  - 提供不同的算法选项，查看不同作业题目之间的相似度。
- **个人信息管理**：
  - 修改昵称、个性签名、查看发布题目的数量等。

## 项目流程

### 学生端流程

1. **登录/注册**：输入手机号和密码进行登录，注册时需要填写必要的个人信息。
2. **作业管理**：学生可以查看自己未完成的作业，也可以查看已提交的作业的答案。
3. **个人中心**：学生可以修改个人信息，查看个人做题历史。

### 教师端流程

1. **登录/注册**：教师使用自己的账户登录，可以管理班级。
2. **发布题目**：教师可以在自己的班级内发布题目，并查看班级的相似度。
3. **查看作业相似度**：教师可以使用不同算法查看作业的相似度分布，并对比不同学生的作业相似度。

## 可视化功能

- **相似度分析**：
  - 显示作业之间的相似度，支持柱状图和饼状图展示相似度的分布。
  - 提供详细的作业对比和相似度分析。
