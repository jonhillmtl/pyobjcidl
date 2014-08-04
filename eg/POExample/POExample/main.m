//
//  main.m
//  POExample
//
//  Created by Jon Hill on 2014-08-04.
//  Copyright (c) 2014 Jon Hill. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "POExample.h"

int main(int argc, const char * argv[])
{
    NSString *pluginPath = [[NSBundle mainBundle] pathForResource:@"POExample" ofType:@"plugin"];
    NSBundle *pluginBundle = [NSBundle bundleWithPath:pluginPath];
    
    Class pyClass = [pluginBundle classNamed:@"POExample"];
    POExample * wrapper = [[pyClass alloc] init];
    NSLog(@"POExample %@", wrapper);
    
    @autoreleasepool {
        
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}

