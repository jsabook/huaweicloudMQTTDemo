# 华为云MQTT实验
MQTT分为设备与应用。即设备注册，应用发布信息给设备。
文件说明：
+ 设备
    + MqttDemo.js 
+ 应用（下面两者的区别，一个是py，一个是nodejs）
    + mqttPublish.py
    + mqttPublish.js
# 运行
环境依赖部署
```
npm install
pip3 install -r requirements.txt
```
代码缺省值填写
代码中需要填写一些认证信息

+ 应用：ak,sk 与 project_id 
+ 设备：serverUrl，device_id和secret 

# 运行设备
```
node MqttDemo.js 
```
显示注册成功

# 运行应用
这里提供了两个不同语言的应用
运行python
```
python mqttPublish.py
```
或者运行Nodejs应用
```
node mqttPublish.js
```
