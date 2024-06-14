将上一代FJE重构为迭代器 +策略模式。

使用python fje.py [-h] -f FILE -s {tree,rectangle} -i ICON [-c CONFIG] 运行。

使用示例：
扑克+树形：
python fje.py -f test.json -s tree -i poker-face -c config.txt
扑克+矩形：
python fje.py -f test.json -s rectangle -i poker-face -c config.txt
自定义图标+树形：
python fje.py -f test.json -s tree -i new-icon-family -c config.txt
自定义图标+矩形：
python fje.py -f test.json -s rectangle -i new-icon-family -c config.txt
