// Two sum (https://leetcode.com/problems/two-sum/description/)

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * compare function for qsort
 */
int compare(const void *a, const void *b) {
   return ( *(int*)a - *(int*)b );
}

/**
 * Two sum solution 1 
 * ordering input array + left and right pointers to find sum
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    int* result = (int*)malloc(sizeof(int) * 2);

    // sort in ascending order 
    qsort(nums, numsSize, sizeof(int), compare); 

    int l = 0;  
    int r = numsSize-1; 

    int curr_sum = 0;

    while (l != r) {
        curr_sum = nums[l] + nums[r];

        if (curr_sum == target){
            result[0] = l;
            result[1] = r;
            return result;
        }
        else if (curr_sum > target){
            r -= 1;
        }
        else if (curr_sum < target){
            l += 1;
        }
    }

    return result;
}

int main() {

    // int nums[] = {15,11,7,2};
    // int numsSize =  sizeof(nums) / sizeof(int);
    // int target = 9;

    int nums[] = {3,2,4};
    int numsSize =  sizeof(nums) / sizeof(int);
    int target = 6;

    // int nums[] = {3,3};
    // int numsSize =  sizeof(nums) / sizeof(int);
    // int target = 6;

    int returnSize = 2;

    int* result = twoSum(nums, numsSize, target, &returnSize);

    printf("[%d,%d]\n", result[0], result[1]);

    free(result);

    return 0;
}
