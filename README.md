# QQ机器人

基于QQ官方机器人+Nonebot实现的一个简单Demo

## 快速开始
先去QQ开放平台创建一个官方机器人 [操作指引](https://bot.q.qq.com/wiki)
```
git clone https://github.com/stozn/qq-bot
cd qq-bot
conda create -n qq-bot python=3.12 -y
conda activate qq-bot
pip install -r requirements.txt
# 修改 env.prod.example 中的 id, token, secret, 并重命名为 .env.prod
python main.py
```