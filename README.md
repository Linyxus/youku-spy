## Youku Spy

## 使用

只要在安装了Python3的环境中执行就行了。

-   `tools.py`是辅助库，执行它会有运行一段测试代码，测试api-key是否还有效。
-   `main.py`是主程序，执行它会自动抓取优酷热播榜单上的视频信息。

数据已经抓取完毕，保存在data.csv与data.json中。代码中的api-key已确认无效，若要再次抓取，请自行获取新的api-key。

## 关于数据

-   data.json中的数据未经处理，存在无效数据（api-key在抓取过程中失效，为优酷保护机制，没有解决，所以后半部分都是`null`），并且存在乱码问题，但是有类别信息，若有能力自行处理。
-   data.csv中的数据已经经过简单处理，去除了无效数据，但是丢弃了类别信息。csv格式理论上可以用excel直接打开，并转换为xls格式。由于内容为我生成的，数据格式可能不符，若excel无法识别，文件内容中的数据格式也十分简明，自行读取并处理也不是难事。