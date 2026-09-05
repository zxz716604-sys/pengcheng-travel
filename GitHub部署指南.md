# 彭城七里徐州旅游攻略 - GitHub Pages 部署指南

## 快速部署步骤（约5分钟）

### 第一步：创建 GitHub 仓库

1. 打开 https://github.com/new
2. 仓库名填写：`pengcheng-travel`
3. 选择 **Public**（公开）
4. **不要**勾选 "Initialize this repository with a README"
5. 点击 **Create repository**

### 第二步：本地推送代码

1. 打开命令提示符（CMD）或 PowerShell
2. 进入项目目录：
   ```
   cd e:\彭城七里徐州旅游攻略
   ```
3. 添加 GitHub 远程仓库：
   ```
   git remote add origin https://github.com/你的用户名/pengcheng-travel.git
   ```
4. 推送到 GitHub：
   ```
   git push -u origin master
   ```
5. 输入你的 GitHub 用户名和密码（或个人访问令牌）

### 第三步：开启 GitHub Pages

1. 进入你的 GitHub 仓库页面
2. 点击 **Settings**（设置）
3. 左侧菜单点击 **Pages**
4. 在 **Source** 下选择 **master** 分支
5. 点击 **Save**
6. 等待1-2分钟，你的网站就会上线！

### 第四步：获取访问链接

部署成功后，你会得到一个永久公网链接：
```
https://你的用户名.github.io/pengcheng-travel/
```

---

## 生成新的二维码

部署成功后，用这个公网链接生成新的二维码：

```
https://你的用户名.github.io/pengcheng-travel/
```

用微信扫描这个链接，就可以随时随地访问了！

---

## 常见问题

### Q: 推代码时提示认证失败？
**A:** 使用 GitHub 个人访问令牌（Personal Access Token）代替密码：
1. 打开 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 点击 "Generate token"
5. 复制令牌，推代码时作为密码使用

### Q: GitHub Pages 部署失败？
**A:** 
1. 检查代码是否有语法错误
2. 确保图片路径正确（使用相对路径）
3. 点击仓库的 Actions 标签查看错误日志

### Q: 如何更新网站？
**A:** 修改本地文件后，执行：
```
git add .
git commit -m "更新内容"
git push
```

---

## 文件清单

项目包含以下文件：
- `index.html` - 主页面
- `nfc-start.html` - NFC启动页
- `图片/` - 景点和图片
- `美食/` - 美食图片
- `截图/` - 页面截图
- `README.md` - 项目说明

---

**祝部署顺利！**
