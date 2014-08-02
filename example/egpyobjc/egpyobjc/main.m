//
//  main.m
//  egpyobjc
//
//  Created by Jon Hill on 8/2/2014.
//  Copyright (c) 2014 jonhill. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "1.h"

int main(int argc, const char * argv[])
{
    POExample * poe = [POExample new];
    [poe one_arg_int];
    
    @autoreleasepool {
        
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}

