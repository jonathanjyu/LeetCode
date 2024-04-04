class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> numsmap;
        for (int i = 0; i<nums.size() ; i++){
            if (numsmap.count(target-nums[i])){
                return {i,numsmap[target-nums[i]]};
            }
            else{
                numsmap[nums[i]] = i;
            }
        }
        return {};
    }
};