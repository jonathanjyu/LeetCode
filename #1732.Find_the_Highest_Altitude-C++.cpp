class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int max_height = 0;
        int tmp = 0;
        for (int i = 0;i < gain.size();i++){
            tmp = tmp + gain[i];
            if (tmp > max_height){
                max_height = tmp;
            }
        }
        return max_height;
    }
};