class Solution {
public:

	int mod = 1e9 + 7;

    int countHousePlacements(int n) {
    	// Only consider one side of the road because the other side is the same;
    	// For example: n=1 then that slot can be a space or a house, and when the road extends (n=2) then the following slot can be a house if the previous one is a space and it can be a space no matter what is the previous one
    	// Therefore, whenever the road extends 1 unit, the number of ways to build a house equals to the previous number of space and the number of ways for a space equals to the total number of ways of the previous rounds
    	// To get the answer, I will loop though n times with the initial case is n=1, with the number of ways to build a house is 1 and the number of ways for a empty space is also 1
    	// The final answer is total^2 because the number of ways to construct 2 sides are the same and there are total^2 combinations
    	long long houseNo = 1, spaceNo = 1; 
    	long long total = houseNo+spaceNo;
    	for (int i = 1; i < n; i++) {
    		houseNo = spaceNo;
    		spaceNo = total;
    		total = (houseNo+spaceNo)%mod;
    	}
    	return (total*total)%mod;
    }
};