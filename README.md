# video to gif（七牛）

本代码使用 ffmpeg，可将视频文件转换为 gif  图片。

# 构建镜像

进入该目录，然后运行以下命令，获得名为 ffmpeg:gif-v5 的 docker 镜像

```
make build
```

# 验证镜像功能

## 运行镜像

```
make debug
```

## 推送镜像

```
make publish
```

## 发布镜像

```
make release
```

## 部署镜像

在七牛自定义数据处理控制台手动部署