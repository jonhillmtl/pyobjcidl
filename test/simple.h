#import <Foundation/Foundation.h>

@interface POSimple : NSObject
    
@property NSInteger simple_int;
@property (strong, nonatomic) NSString * simple_string;
@property (strong, nonatomic) NSDictionary * simple_dict;
@property (strong, nonatomic) NSMutableDictionary * simple_mutable_dict;
@property (strong, nonatomic) NSArray * simple_array;
@property (strong, nonatomic) NSMutableArray * simple_mutable_array;
@property BOOL simple_boolean;

@end
