//
//  ViewController.m
//  CWPayDemo
//
//  Created by weiwei on 15/11/24.
//  Copyright © 2015年 weiwei. All rights reserved.
//

#import "ViewController.h"
#import "WXApi.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    
    // Do any additional setup after loading the view, typically from a nib.
}


#warning URL配置
- (IBAction)weixinAction:(id)sender {
    
    NSString *url = @"http://localhost:9192";
    NSURLRequest *requst = [NSURLRequest requestWithURL:[NSURL URLWithString:url]];
    
    NSURLResponse *response = nil;
    NSError *error = nil;
    NSData *data = [NSURLConnection sendSynchronousRequest:requst returningResponse:&response error:&error];
    NSDictionary *dict = nil;
    if (data != nil) {
        dict = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableContainers error:nil];
    }
    
    NSLog(@"data--%@",dict);
    NSLog(@"error--%@",error);
    NSLog(@"response--%@",response);
    
    dict = @{@"package":@"Sign=WXPay",
             @"noncestr":@"w0bMY5v6TND24RWE",
             @"partnerid":@"1900000109",
             @"timestamp":@"1448383074",
             @"sign":@"76B7DDB56ACC08842AFFA2DE075B3422",
             @"appid":@"wxd930ea5d5a258f4f",
             @"prepayid":@"wx201511250037547fa52afa040298474210"};
    
    NSMutableString *stamp  = [dict objectForKey:@"timestamp"];
    
    NSString *APP_ID = [dict objectForKey:@"appid"];
    [WXApi registerApp:APP_ID];

    
    //调起微信支付
    PayReq* req             = [[PayReq alloc] init];
    req.openID              = [dict objectForKey:@"appid"];
    req.partnerId           = [dict objectForKey:@"partnerid"];
    req.prepayId            = [dict objectForKey:@"prepayid"];
    req.nonceStr            = [dict objectForKey:@"noncestr"];
    req.timeStamp           = stamp.intValue;
    req.package             = [dict objectForKey:@"package"];
    req.sign                = [dict objectForKey:@"sign"];
    
    [WXApi sendReq:req];
    
}

- (void)requestWeiXinData
{
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
