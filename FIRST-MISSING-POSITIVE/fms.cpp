class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int sm = 1;

        while(true) {
            if (s.find(sm) == s.end()){
                return sm;
            }
            sm ++;
        }
    }
};