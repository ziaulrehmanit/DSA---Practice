class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int number = 0;

        for (int i=0; i<nums.size(); i++)
        {
            if (nums[i]!=0)
            {
                int temp=nums[number];
                nums[number]=nums[i];
                nums[i]=temp;
                number++;
            }
        }
    }
};
