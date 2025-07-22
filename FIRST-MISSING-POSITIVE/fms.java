class Solution {
        public int firstMissingPositive(int[] nums) {
            Set<Integer> s = Arrays.stream(nums).boxed().collect(Collectors.toSet());
            int sm = 1;
            while (true){
                if(!s.contains(sm)){
                    return sm;
                }
                sm++;
            }

        }
    }