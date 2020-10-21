# 饥荒联机版玩家追踪

帮一个朋友追踪一个饥荒骗子的动向，利用 `Github Actions`，每5-10min执行一次，只要该玩家在线，就会发邮件提醒

## 使用方法

`fork` 到自己仓库后，在 `Settings` -> `Secrets` 中添加以下值

| Name | Descrip |  Value举例 |  
| --- | --- | --- |
| `QQ_NUMBER` | 你的QQ号 | `1209626343`
| `QQ_SMPT_PASSWD` | 你的QQ邮箱的SMTP密码 | `dxxdasdcxfeghbvb5xz` |
| `TARGET_STEAM_ID` | 要追踪的人STEAM ID | `76561198204009266` |
| `TOKEN` | Klei Token 获取方法见下文 | `pcl-usc^KU_aUxMQjy7^DontStarveTogether^rCT`<br>`aArNuSx3tPzjquadxMQ/hs6j+InnOvHPWeO6EW6Y=` |
| `TO_MAIL` | 要通知的邮箱 | `1209626343@qq.com` |

添加完成后如下图

![](/img/1.png)

## 获取 `TOKEN`

打开饥荒联机版，在如下界面的控制台内输入 `print(TheFrontEnd:GetAccountManager():GetToken())`，然后别关游戏，打开 `文档\Klei\DoNotStarveTogether\client_log.txt`，在最下面可以找到类似 `pcl-usc^KU_aUxMQjy7^DontStarveTogether^rCTaArNuSx3tPzjquadxMQ/hs6j+InnOvHPWeO6EW6Y=` 的字段就是 `TOKEN`

该方法获得的 `TOKEN` 几小时候后会失效，可以向 Klei 索取永久的 `TOKEN`

![](/img/2.png)

设置好后打开，修改 `.github/workflows/main.yml`，找到下面的段落，将 `#` 号去掉即可(如果有 `#` 号的话）

```
on:
  push:
    branches: main
  #schedule:
  #- cron: "*/5 * * * *"
```
注： `fork` 到自己仓库后需要手动 `commit` 后 `cron` 人物才生效
