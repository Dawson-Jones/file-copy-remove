## 抓图并转移
### 配置文件
```python
PATH_A = '/home/ubuntu/Pictures/A'
PATH_B = '/home/ubuntu/Pictures/B'
PATH_C = '/home/ubuntu/Pictures/C'
RATE = 90
```
- PATH_A  
    小图存放的文件地址, 当在图片存于该地址把小图存放于\<PATH_C> *小图与大图的区别在于大图名称没有'_'*
- PATH_B  
    存放OK和NG的图片地址, 当大图存放于OK中有\<RATE>的概率删除位于C中的小图
- PATH_C  
    存放小图的路径

> **注意**: 在windows中请使用下划线代替反下划线

**使用下划线**
```python
PATH_A = 'E:/pj_picture/A'
PATH_B = 'E:/pj_picture/B'
PATH_C = 'E:/pj_picture/C'
```

~~**使用反下划线**~~
```python
PATH_A = 'E:\pj_picture\A'
PATH_B = 'E:\pj_picture\B'
PATH_C = 'E:\pj_picture\C'
```