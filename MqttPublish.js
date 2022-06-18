const core = require('@huaweicloud/huaweicloud-sdk-core');
const iotda = require("@huaweicloud/huaweicloud-sdk-iotda");
const ak = "<ak>";
const sk = "<sk>";

const endpoint = "https://iotda.cn-north-4.myhuaweicloud.com";
const project_id = "<project id>";

const credentials = new core.BasicCredentials()
                     .withAk(ak)
                     .withSk(sk)
                     .withProjectId(project_id)
const client = iotda.IoTDAClient.newBuilder()
                            .withCredential(credentials)
                            .withEndpoint(endpoint)
                            .build();
const request = new iotda.CreateCommandRequest();
request.deviceId = "xyzer";
const body = new iotda.DeviceCommandRequest();
body.withParas({"time":{"data":Date.now()}});
body.withCommandName("posttime");
request.withBody(body);
const result = client.createCommand(request);
result.then(result => {
    console.log("JSON.stringify(result)::" + JSON.stringify(result));
}).catch(ex => {
    console.log("exception:" + JSON.stringify(ex));
});