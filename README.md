# CWPayDemo
公司做了一个支付的项目，自己把问题总结一下。也希望能给大家一些帮助

##微信支付
> 微信支付比较坑的是之前找的demo有些问题，是V2的版本，导致一直寻找APP_KEY，最后发现在V3的版本中这个已经取消了，所以浪费一点时间。<

###微信申请过程
* 创建微信应用,[微信开发平台](https://open.weixin.qq.com/),创建应用之后就是开通微信支付的权限了，这里需要一些材料和时间。
* 审核成功之后呢，微信会发送一个邮件，图片里面包括需要的信息，APPID以及PARTNER_ID，按照流程设置api密钥就可以了。
![image](https://github.com/wei18810109052/CWPayDemo/blob/master/src/QQ20151124-0.png)
设置api密钥需要安装证书，按照上面操作就好了，设置32位密码，可以[百度一下](http://www.baidu.com)32位密码生成器。 这里我随便搜了一个[密码链接](http://dh.mxiaozheng.cn/CipherMaker)

现在就得到了三个参数，`APPI_ID`,`PARTNER_ID`,`PARTNER_KEY`，这三个参数就够了。
[微信开发文档](https://pay.weixin.qq.com/wiki/doc/api/index.html)，根据文档开发，就好了。

注意的地方:添加的库文件

* `Security.framework`
* `libiconv.tbd`
* `SystemConfiguration.framework`
* `CoreGraphics.Framework`
* `libsqlite3.tbd`
* `CoreTelephony.framework`
* `libstdc++.tbd`
* `libz.tbd`




##支付宝
>支付宝开发，也遇到一个坑，就是之前以为支付宝支付，只需要在第三方平台申请就好了，再申请支付宝支付的权限就ok了。申请成功之后，填写之后呢，可以用调起支付宝，但是提示抱歉，该商户未开通支付宝服务，无法付款.查找一些资料后，发现需要开通无线支付的功能才行。签约之后就可以了。

###支付宝申请过程
* 创建支付宝移动应用，在[支付宝开放平台](http://open.alipay.com/platform/home.htm)上面申请。**支付提交之后，不能修改，不能删除，这点比较坑**，只能等待了，大家注意一下。
* 申请完之后，跟微信一下，就是开通移动支付的权限，应该是需要一些资料。这个需要几天吧，我自己也没有提交资料，所以具体的，我也不清楚。
* 再就是需要在[商家服务](https://b.alipay.com/newIndex.htm)里面签约,选择[移动支付](https://b.alipay.com/order/productDetail.htm?productId=2015110218010538) 在线申请。提交资料之后就等待结果

支付宝支付呢，需要三个参数，`partner`和`seller`是一样的。还有一个就是私钥。说说这2个参数。第一个呢，在支付宝应用详情中，移动支付点击查看就可以跳转到商户平台就可以看到了 2088开头的就是。私钥呢，按照支付宝的[文档](http://doc.open.alipay.com/doc2/detail?treeId=58&articleId=103543&docType=1)来，就可以了。生成的密钥用sublime或者记事本打开，去掉头尾就是我们需要的私钥了




---
大家有什么问题和建议可以在留言，我会改进。觉得还不错，给个star吧。