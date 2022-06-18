
# coding: utf-8
import numpy as np
import time
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkiotda.v5.region.iotda_region import IoTDARegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *

if __name__ == "__main__":
    ak = "<ak>"
    sk = "<sk>"
    project_id = "<project id>"


    credentials = BasicCredentials(ak, sk) \

    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IoTDARegion.value_of("cn-north-4")) \
        .build()
    time_array = []
    for i in range(100):
        if i%10==0:
            time.sleep(4)
        try:
            request = CreateCommandRequest()
            request.device_id = "xyzer"
            request.body = DeviceCommandRequest(
                paras={"time":{"data":time.time()*1000}},
                command_name="posttime"
            )
            response = client.create_command(request)
            time_array.append(int(response.response['time']))
            print(f"花费的时间: {response.response['time']} ms")
        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)
    if len(time_array)!=0:
        print(f"请求的次数：{len(time_array)},花费的平均时间：{sum(time_array)/len(time_array)} ms; 方差为{np.var(time_array)}")