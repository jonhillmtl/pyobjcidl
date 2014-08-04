//
//  POCAppDelegate.m
//  POExample
//
//  Created by Jon Hill on 2014-08-04.
//  Copyright (c) 2014 Jon Hill. All rights reserved.
//

#import "POCAppDelegate.h"
#import "POExample.h"

@implementation POCAppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    NSString *pluginPath = [[NSBundle mainBundle] pathForResource:@"POExample" ofType:@"plugin"];
    NSBundle *pluginBundle = [NSBundle bundleWithPath:pluginPath];
    
    Class pyClass = [pluginBundle classNamed:@"POExample"];
    POExample * wrapper = [[pyClass alloc] init];
    NSLog(@"POExample %@", wrapper);
}

@end
