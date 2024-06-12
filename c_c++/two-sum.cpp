// Two sum (https://leetcode.com/problems/two-sum/description/)

#include <cstdio>
#include <unordered_map>
#include <vector>

class Solution {
    public:
        std::vector<int> twoSum(std::vector<int> &nums, int target) {
            std::vector<int> result;
            std::unordered_map<int, int> map;

            for (int i = 0; i < nums.size(); i++) {
                /*printf("i: %d, nums[i]: %d\n", i, nums[i]);*/

                if (map.find(nums[i]) != map.end()) {
                    result.push_back(i);
                    result.push_back(map[nums[i]]);
                    return result;
                }

                map.insert({target - nums[i], i});
            }

            return result;
        }
};

int main() {


    std::vector<int> nums = {3,2,4};
    int target = 6;

    /*std::vector<int> nums = {3,3};*/
    /*int target = 6;*/

    /*std::vector<int> nums = {15,11,7,2};*/
    /*int target = 9;*/

    Solution solution;

    std::vector<int> result = solution.twoSum(nums, target);
    
    printf("[%d,%d]\n", result[0], result[1]);

    return 0;
}
