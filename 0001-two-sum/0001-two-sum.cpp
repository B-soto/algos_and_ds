using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //Iterate over loop
//         #crate a hashmap to store the number and the index where it is located
//         # As we iterate over thel oop, Suptract currint num from target. Check to see if coresponding pair is in dictionary. If so, Return that dictionary index(value)
//         # and return current index 
        unordered_map<int,int> numMap;
        vector<int> rtn_index;
        
        for (int i = 0; i < nums.size(); i++) {
            auto new_target = target - nums[i];
            if (numMap.find(new_target) != numMap.end()){
                rtn_index.push_back(i);
                rtn_index.push_back(numMap[new_target]);
                return rtn_index;
            }else{
                cout << nums[i] << ':' << i << endl;
                numMap.insert({nums[i], i});
               
            
            }
          
        }
        
        for (const auto& pair : numMap) {
            cout << pair.first << pair.second << endl;
        }
        return rtn_index;
    }
};